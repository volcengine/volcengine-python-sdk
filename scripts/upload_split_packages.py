#!/usr/bin/env python3
"""Upload split-package wheels with hash-checked resume support."""

import argparse
import email
import hashlib
import subprocess
import sys
import time
import zipfile
from pathlib import Path

import requests
from packaging.requirements import Requirement


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


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as artifact:
        for chunk in iter(lambda: artifact.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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


def wait_until_visible(session, args, name, version, path, local_digest):
    for attempt in range(1, args.visibility_attempts + 1):
        try:
            digest = remote_digest(
                session,
                args.index_url,
                name,
                version,
                path.name,
            )
        except requests.RequestException:
            digest = None
        if digest == local_digest:
            return
        if digest is not None:
            raise RuntimeError(
                "remote hash mismatch for {}: local={}, remote={}".format(
                    path.name, local_digest, digest
                )
            )
        if attempt < args.visibility_attempts:
            time.sleep(args.visibility_delay)
    raise RuntimeError("uploaded file is not visible: {}".format(path.name))


def upload_wheel(session, args, position, total, name, version, path):
    local_digest = sha256(path)
    try:
        digest = remote_digest(session, args.index_url, name, version, path.name)
    except requests.RequestException as exc:
        raise RuntimeError("cannot query {}: {}".format(name, exc))
    if digest is not None:
        if digest != local_digest:
            raise RuntimeError(
                "remote hash mismatch for {}: local={}, remote={}".format(
                    path.name, local_digest, digest
                )
            )
        print("[{}/{}] verified existing {}".format(position, total, name), flush=True)
        return False

    for attempt in range(1, args.max_attempts + 1):
        print(
            "[{}/{}] uploading {} (attempt {})".format(
                position, total, name, attempt
            ),
            flush=True,
        )
        completed = subprocess.run(
            [
                sys.executable,
                "-m",
                "twine",
                "upload",
                "--repository",
                args.repository,
                str(path),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        if completed.returncode == 0:
            wait_until_visible(
                session,
                args,
                name,
                version,
                path,
                local_digest,
            )
            print("[{}/{}] published {}".format(position, total, name), flush=True)
            return True
        if "429" not in completed.stdout or attempt == args.max_attempts:
            print(completed.stdout, file=sys.stderr)
            if "429" in completed.stdout:
                print(
                    "new-project limits may require waiting for the hourly window; "
                    "rerun this command to resume with hash verification",
                    file=sys.stderr,
                )
            raise subprocess.CalledProcessError(completed.returncode, completed.args)
        print(
            "rate limited while uploading {}; retrying in {} seconds".format(
                name, args.retry_delay
            ),
            flush=True,
        )
        time.sleep(args.retry_delay)
    return False


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wheel_dir", type=Path)
    parser.add_argument("--repository", default="testpypi")
    parser.add_argument("--index-url", default="https://test.pypi.org")
    parser.add_argument("--pace", type=float, default=4.0)
    parser.add_argument("--retry-delay", type=float, default=30.0)
    parser.add_argument("--max-attempts", type=int, default=1)
    parser.add_argument("--visibility-attempts", type=int, default=10)
    parser.add_argument("--visibility-delay", type=float, default=2.0)
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        wheels = ordered_wheels(args.wheel_dir)
        if not wheels:
            raise ValueError("no wheels found in {}".format(args.wheel_dir))
        session = requests.Session()
        uploaded = 0
        for position, (name, version, path) in enumerate(wheels, 1):
            was_uploaded = upload_wheel(
                session,
                args,
                position,
                len(wheels),
                name,
                version,
                path,
            )
            if was_uploaded:
                uploaded += 1
                if position < len(wheels):
                    time.sleep(args.pace)
        print(
            "verified {} wheels; uploaded {} new files".format(len(wheels), uploaded)
        )
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print("error: {}".format(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
