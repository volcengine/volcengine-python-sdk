#!/usr/bin/env python3
"""Reserve split-package distribution names on (Test)PyPI.

Warehouse 没有显式的"占名"接口：项目名在首次上传时创建。本脚本为每个发行包名
构建并上传一个最小 stub wheel（0.0.1），按 Warehouse 新项目限速分批执行
（默认 ≤4 个/24 小时），支持断点续跑（已存在项目跳过）与跨窗口恢复
（429 或完成一批后睡满一个滚动窗口再重试）。

只能在正式发布窗口外运行。
"""

import argparse
import base64
import hashlib
import json
import subprocess
import sys
import time
import zipfile
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "split-packages.json"
META_DISTRIBUTION = "volcengine-python-sdk"
RESERVED_VERSION = "0.0.1"


def load_manifest():
    with MANIFEST_PATH.open(encoding="utf-8") as manifest_file:
        return json.load(manifest_file)


def load_distributions():
    manifest = load_manifest()
    excluded = set(manifest.get("excluded_modules", {}))
    names = ["volcenginesdk-core"]
    for path in sorted(ROOT.iterdir()):
        if (
            path.is_dir()
            and path.name.startswith("volcenginesdk")
            and path.name not in excluded
            and path.name != "volcenginesdkcore"
        ):
            names.append(
                manifest["distribution_prefix"] + path.name[len("volcenginesdk"):]
            )
    names.append(META_DISTRIBUTION)
    return names


def project_exists(session, index_url, name):
    response = session.get(
        "{}/pypi/{}/json".format(index_url.rstrip("/"), name), timeout=30
    )
    if response.status_code == 200:
        return True
    if response.status_code == 404:
        return False
    response.raise_for_status()


def record_hash(data):
    digest = hashlib.sha256(data).digest()
    return "sha256=" + base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")


def build_stub_wheel(name, version, output_dir):
    """构建最小 stub wheel：仅 dist-info，无代码。"""
    underscore = name.replace("-", "_")
    dist_info = "{}-{}.dist-info".format(underscore, version)
    metadata = (
        "Metadata-Version: 2.1\n"
        "Name: {}\n"
        "Version: {}\n"
        "Summary: Name reservation for the Volcengine Python SDK split package {}\n"
        "Author: volc-engine\n"
        "License: Apache License 2.0\n"
        "Description-Content-Type: text/plain\n"
        "\n"
        "This project reserves the distribution name for the Volcengine Python SDK\n"
        "split-package release. Real releases follow the SDK vehicle version.\n".format(
            name, version, name
        )
    ).encode("utf-8")
    wheel = (
        "Wheel-Version: 1.0\n"
        "Generator: reserve_split_packages.py\n"
        "Root-Is-Purelib: true\n"
        "Tag: py2.py3-none-any\n"
    ).encode("utf-8")
    record_entries = [
        ("{}/METADATA".format(dist_info), record_hash(metadata), str(len(metadata))),
        ("{}/WHEEL".format(dist_info), record_hash(wheel), str(len(wheel))),
    ]
    record = "".join(
        "{},{},{}\n".format(path, digest, size)
        for path, digest, size in record_entries
    )
    record += "{}/RECORD,,\n".format(dist_info)

    wheel_path = output_dir / "{}-{}-py2.py3-none-any.whl".format(
        underscore, version
    )
    with zipfile.ZipFile(wheel_path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("{}/METADATA".format(dist_info), metadata)
        archive.writestr("{}/WHEEL".format(dist_info), wheel)
        archive.writestr("{}/RECORD".format(dist_info), record)
    return wheel_path


def save_rate_timestamps(state_path, timestamps):
    state_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = state_path.with_suffix(state_path.suffix + ".tmp")
    temporary_path.write_text(
        json.dumps({"upload_attempts": timestamps}, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary_path.replace(state_path)


def load_rate_timestamps(state_path, window_seconds):
    if not state_path.exists():
        return []
    with state_path.open(encoding="utf-8") as state_file:
        state = json.load(state_file)
    timestamps = state.get("upload_attempts")
    if not isinstance(timestamps, list) or not all(
        isinstance(timestamp, (int, float)) for timestamp in timestamps
    ):
        raise RuntimeError("invalid rate-limit state: {}".format(state_path))
    now = time.time()
    active = sorted(
        float(timestamp)
        for timestamp in timestamps
        if 0 <= now - timestamp < window_seconds
    )
    if active != timestamps:
        save_rate_timestamps(state_path, active)
    return active


def wait_for_rate_slot(args, state_path, timestamps):
    while len(timestamps) >= args.batch_size:
        wait = max(0, timestamps[0] + args.window_seconds - time.time()) + 60
        print(
            "rate window full; sleeping {:.0f}s before next upload".format(wait),
            flush=True,
        )
        time.sleep(wait)
        timestamps[:] = load_rate_timestamps(state_path, args.window_seconds)


def upload_stub(session, args, name, wheel_path):
    """上传 stub wheel。返回 (created, blocked)。

    created=True  项目新创建；
    blocked=True  触发新项目限速，调用方应睡到下一窗口后重试；
    其余错误抛异常。
    """
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "twine",
            "upload",
            "--repository",
            args.repository,
            str(wheel_path),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    if completed.returncode == 0:
        return True, False
    if "429" in completed.stdout or "Too Many Requests" in completed.stdout:
        return False, True
    print(completed.stdout, file=sys.stderr)
    raise RuntimeError("twine upload failed for {}".format(name))


def reserve(args):
    names = load_distributions()
    if args.name:
        unknown_names = sorted(set(args.name) - set(names))
        if unknown_names:
            raise RuntimeError(
                "unknown distribution(s): {}".format(", ".join(unknown_names))
            )
        selected_names = set(args.name)
        names = [name for name in names if name in selected_names]
    session = requests.Session()
    pending = []
    existing = 0
    for name in names:
        if project_exists(session, args.index_url, name):
            existing += 1
            continue
        pending.append(name)
    print(
        "{} distributions: {} already exist, {} to reserve".format(
            len(names), existing, len(pending)
        ),
        flush=True,
    )
    if args.dry_run:
        for name in pending:
            print("would reserve: {}".format(name))
        return 0

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    state_path = Path(args.rate_state)
    timestamps = load_rate_timestamps(state_path, args.window_seconds)
    if args.initial_window_used:
        if timestamps:
            raise RuntimeError(
                "--initial-window-used requires an empty rate-limit state"
            )
        timestamps = [time.time()] * args.initial_window_used
        save_rate_timestamps(state_path, timestamps)
    created = 0
    for name in pending:
        if args.limit and created >= args.limit:
            print("reached --limit {}, stopping".format(args.limit), flush=True)
            break
        wheel_path = build_stub_wheel(name, RESERVED_VERSION, output_dir)
        while True:
            if project_exists(session, args.index_url, name):
                # 可能由其他运行/窗口抢先创建
                print("{} already exists, skipping".format(name), flush=True)
                break
            wait_for_rate_slot(args, state_path, timestamps)
            timestamps.append(time.time())
            save_rate_timestamps(state_path, timestamps)
            _, blocked = upload_stub(session, args, name, wheel_path)
            if not blocked:
                created += 1
                print(
                    "[{}/{}] reserved {}".format(created, len(pending), name),
                    flush=True,
                )
                break
            # 本地状态可能遗漏了其他客户端的上传；429 后保守地重置为满窗口。
            timestamps[:] = [time.time()] * args.batch_size
            save_rate_timestamps(state_path, timestamps)
            print("new-project rate limit hit for {}".format(name), flush=True)
        time.sleep(args.pace)
    print("reserved {} new projects; {} already existed".format(created, existing))
    return 0


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", default="testpypi")
    parser.add_argument("--index-url", default="https://test.pypi.org")
    parser.add_argument(
        "--batch-size",
        type=int,
        default=4,
        help="max new projects per rolling window",
    )
    parser.add_argument(
        "--window-seconds",
        type=float,
        default=86400,
        help="rolling rate-limit window length",
    )
    parser.add_argument("--pace", type=float, default=4.0)
    parser.add_argument("--limit", type=int, default=0, help="reserve at most N new projects (0 = no limit)")
    parser.add_argument(
        "--name",
        action="append",
        help="reserve only this exact manifest distribution name (repeatable)",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output-dir", default="dist/reserve")
    parser.add_argument(
        "--rate-state",
        default="dist/reserve/rate-limit.json",
        help="persistent rolling-window upload-attempt state",
    )
    parser.add_argument(
        "--initial-window-used",
        type=int,
        default=0,
        help="seed an empty rate state with prior attempts in the current window",
    )
    args = parser.parse_args()
    if args.batch_size <= 0:
        parser.error("--batch-size must be greater than zero")
    if args.window_seconds <= 0:
        parser.error("--window-seconds must be greater than zero")
    if not 0 <= args.initial_window_used < args.batch_size:
        parser.error("--initial-window-used must be between 0 and batch-size - 1")
    return args


def main():
    args = parse_args()
    try:
        return reserve(args)
    except (OSError, RuntimeError, requests.RequestException) as exc:
        print("error: {}".format(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
