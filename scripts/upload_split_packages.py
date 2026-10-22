#!/usr/bin/env python3
"""Upload split-package wheels in two phases: upload sweep, then reconcile.

Phase 1 uploads every missing wheel once without blocking per-file on index
visibility; phase 2 verifies visibility across the index and re-uploads any
gaps. Each file is attempted at most --max-attempts times. Already-published
files are skipped by filename, so the command is safe to resume.
"""

import argparse
import email
import subprocess
import sys
import time
import zipfile
from pathlib import Path

import requests
from packaging.requirements import Requirement


def log(message, error=False):
    stream = sys.stderr if error else sys.stdout
    print("[{}] {}".format(time.strftime("%H:%M:%S"), message), file=stream, flush=True)


def canonicalize(name):
    return name.lower().replace("_", "-").replace(".", "-")


def wheel_metadata(path):
    with zipfile.ZipFile(path) as archive:
        metadata_path = next(
            name for name in archive.namelist() if name.endswith(".dist-info/METADATA")
        )
        parsed = email.message_from_bytes(archive.read(metadata_path))
    dependencies = {
        canonicalize(Requirement(requirement).name)
        for requirement in parsed.get_all("Requires-Dist", [])
    }
    return canonicalize(parsed["Name"]), parsed["Version"], dependencies


def remote_digest(session, index_url, name, version, filename):
    response = session.get(
        "{}/pypi/{}/{}/json".format(index_url.rstrip("/"), name, version),
        timeout=30,
    )
    if response.status_code == 404:
        return None
    response.raise_for_status()
    for artifact in response.json().get("urls", []):
        if artifact["filename"] == filename:
            return artifact["digests"]["sha256"]
    raise RuntimeError(
        "{} {} exists without expected file {}".format(name, version, filename)
    )


def ordered_wheels(wheel_dir):
    wheels = {}
    versions = set()
    for path in wheel_dir.glob("*.whl"):
        name, version, dependencies = wheel_metadata(path)
        if name in wheels:
            raise ValueError("duplicate distribution: {}".format(name))
        versions.add(version)
        wheels[name] = (version, path, dependencies)
    if len(versions) != 1:
        raise ValueError("all wheels must use one version: {}".format(sorted(versions)))

    local_names = set(wheels)
    pending = {
        name: dependencies & local_names
        for name, (_, _, dependencies) in wheels.items()
    }
    ordered = []
    published = set()
    while pending:
        ready = sorted(
            name for name, dependencies in pending.items()
            if dependencies <= published
        )
        if not ready:
            raise ValueError(
                "wheel dependency cycle: {}".format(
                    ", ".join(sorted(pending))
                )
            )
        for name in ready:
            version, path, _ = wheels[name]
            ordered.append((name, version, path))
            published.add(name)
            del pending[name]
    return ordered


def visibility_state(session, index_url, name, version, filename):
    """目标文件在索引上的状态：present / absent / unknown（查询失败）。"""
    try:
        digest = remote_digest(session, index_url, name, version, filename)
    except requests.RequestException:
        return "unknown"
    except RuntimeError:
        # 版本已存在但缺少该文件：需要补传。
        return "absent"
    return "present" if digest is not None else "absent"


def twine_upload(args, name, path):
    """上传一次，返回分类：ok / rate_limited / name_conflict / error。"""
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "twine",
            "upload",
            "--skip-existing",
            "--repository",
            args.repository,
            str(path),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    output = completed.stdout or ""
    if completed.returncode == 0:
        return "ok", output
    lowered = output.lower()
    if "429" in output or "too many requests" in lowered:
        return "rate_limited", output
    if "too similar" in lowered or (
        "400" in output and "existing project" in lowered
    ):
        return "name_conflict", output
    return "error", output


def upload_all(args, wheels, session):
    """先全量上传一遍，再统一可见性校验并查漏补缺。

    每个文件总尝试次数不超过 args.max_attempts；名称冲突不可重试。
    返回 (present, fatal)。
    """
    total = len(wheels)
    attempts = {name: 0 for name, _, _ in wheels}
    fatal = {}
    present = set()

    def classify():
        """刷新索引状态，返回需要补传的 (name, version, path) 列表。"""
        pending = []
        for name, version, path in wheels:
            if name in present or name in fatal:
                continue
            state = visibility_state(
                session, args.index_url, name, version, path.name
            )
            if state == "present":
                present.add(name)
            elif state == "absent":
                pending.append((name, version, path))
            # "unknown" 留到下一轮再判定，避免误补传。
        return pending

    def attempt(name, path):
        attempts[name] += 1
        log(
            "uploading {} (attempt {}/{})".format(
                name, attempts[name], args.max_attempts
            )
        )
        result, output = twine_upload(args, name, path)
        if result == "name_conflict":
            fatal[name] = "name_conflict"
            log("fatal: {} name blocked on index".format(name), error=True)
            log(output.strip(), error=True)
            return result
        if result == "rate_limited":
            log("rate limited while uploading {}".format(name), error=True)
        elif result == "error":
            log(output.strip(), error=True)
        return result

    # Phase 1：跳过索引上已存在的文件，其余全部上传一遍（不阻塞等可见性）。
    initial_pending = classify()
    log(
        "{} wheels: {} already present, {} to upload".format(
            total, total - len(initial_pending), len(initial_pending)
        )
    )
    saw_rate_limit = False
    for index, (name, _, path) in enumerate(initial_pending, 1):
        if attempt(name, path) == "rate_limited":
            saw_rate_limit = True
        if index < len(initial_pending):
            time.sleep(args.pace)

    # Phase 2：统一可见性校验 + 查漏补缺。
    for round_number in range(2, args.max_attempts + 1):
        delay = args.retry_delay if saw_rate_limit else args.visibility_delay
        saw_rate_limit = False
        log("waiting {}s before verify round {}".format(delay, round_number))
        time.sleep(delay)
        missing = [
            item for item in classify()
            if attempts[item[0]] < args.max_attempts
        ]
        if not missing:
            break
        log(
            "verify round {}: {} file(s) not yet visible, retrying".format(
                round_number, len(missing)
            )
        )
        for index, (name, _, path) in enumerate(missing, 1):
            if attempt(name, path) == "rate_limited":
                saw_rate_limit = True
            if index < len(missing):
                time.sleep(args.pace)

    # 终态复核，给索引最后一点刷新时间。
    time.sleep(args.visibility_delay)
    classify()
    return present, fatal


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wheel_dir", type=Path)
    parser.add_argument("--repository", default="testpypi")
    parser.add_argument("--index-url", default="https://test.pypi.org")
    parser.add_argument("--pace", type=float, default=4.0)
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=60.0,
        help="seconds to wait before a verify round after a 429",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=3,
        help="max upload attempts per file across sweep and reconcile",
    )
    parser.add_argument(
        "--visibility-delay",
        type=float,
        default=10.0,
        help="seconds to wait for index propagation before each verify round",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        wheels = ordered_wheels(args.wheel_dir)
        if not wheels:
            raise ValueError("no wheels found in {}".format(args.wheel_dir))
        session = requests.Session()
        started = time.time()
        present, fatal = upload_all(args, wheels, session)
        missing = sorted(
            name for name, _, _ in wheels
            if name not in present and name not in fatal
        )
        elapsed = time.time() - started
        log(
            "done in {:.0f}s: {} present, {} missing, {} blocked".format(
                elapsed, len(present), len(missing), len(fatal)
            )
        )
        for name in sorted(fatal):
            log("blocked: {}".format(name), error=True)
        for name in missing:
            log("missing: {}".format(name), error=True)
        return 0 if not missing and not fatal else 1
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        log("error: {}".format(exc), error=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
