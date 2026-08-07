#!/usr/bin/env python3
"""Verify an installed Volcengine SDK split-package release."""

import argparse
import importlib
import json
import sys
from pathlib import Path

try:
    from importlib import metadata
except ImportError:  # pragma: no cover - Python < 3.8
    import importlib_metadata as metadata


MODULE_PREFIX = "volcenginesdk"
META_DISTRIBUTION = "volcengine-python-sdk"


def distribution_name(module, manifest):
    if module == "volcenginesdkcore":
        return "volcenginesdk-core"
    return manifest["distribution_prefix"] + module[len(MODULE_PREFIX):]


def is_supported(python_requires):
    if not python_requires or not python_requires.startswith(">="):
        return True
    required = tuple(int(part) for part in python_requires[2:].split("."))
    current = sys.version_info[:len(required)]
    return current >= required


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--expect-meta", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    failures = []
    imported = 0

    if args.expect_meta:
        installed_version = metadata.version(META_DISTRIBUTION)
        if installed_version != args.version:
            failures.append(
                "{} version is {}, expected {}".format(
                    META_DISTRIBUTION, installed_version, args.version
                )
            )

    default_python_requires = manifest["python_requires"]["default"]
    for module in manifest["modules"]:
        python_requires = manifest["python_requires"].get(
            module,
            default_python_requires,
        )
        if not is_supported(python_requires):
            continue

        distribution = distribution_name(module, manifest)
        try:
            installed_version = metadata.version(distribution)
            if installed_version != args.version:
                raise RuntimeError(
                    "installed version is {}, expected {}".format(
                        installed_version, args.version
                    )
                )
            imported_module = importlib.import_module(module)
            if not getattr(imported_module, "__file__", None):
                raise RuntimeError("import has no module file")
            imported += 1
        except Exception as exc:
            failures.append("{}: {}".format(module, exc))

    if failures:
        for failure in failures:
            print("error: {}".format(failure), file=sys.stderr)
        return 1

    print(
        "verified {} SDK modules at version {} on Python {}.{}.{}".format(
            imported,
            args.version,
            sys.version_info[0],
            sys.version_info[1],
            sys.version_info[2],
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
