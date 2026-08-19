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


def discover_modules(manifest):
    """扫描仓内 volcenginesdk* 目录得出模块清单（与 build_split_packages 一致）。"""
    root = Path(__file__).resolve().parents[1]
    excluded = set(manifest.get("excluded_modules", {}))
    return sorted(
        path.name
        for path in root.iterdir()
        if path.is_dir()
        and path.name.startswith(MODULE_PREFIX)
        and path.name not in excluded
    )


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
    parser.add_argument(
        "--package",
        dest="packages",
        action="append",
        help="module or distribution to verify; repeatable. Default: all modules",
    )
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

    modules = discover_modules(manifest)
    if args.packages:
        module_by_distribution = {
            distribution_name(module, manifest): module for module in modules
        }
        selected = []
        for item in args.packages:
            if item in modules:
                selected.append(item)
            elif item in module_by_distribution:
                selected.append(module_by_distribution[item])
            elif item == META_DISTRIBUTION:
                continue
            else:
                failures.append("unknown package: {}".format(item))
        if failures:
            for failure in failures:
                print("error: {}".format(failure), file=sys.stderr)
            return 1
    else:
        selected = modules

    default_python_requires = manifest.get("default_python_requires", ">=2.7")
    for module in selected:
        # 服务自带的 split-package.json 声明 python_requires（缺失回退默认值）
        service_meta_path = (
            Path(__file__).resolve().parents[1] / module / "split-package.json"
        )
        python_requires = default_python_requires
        if service_meta_path.is_file():
            service_meta = json.loads(service_meta_path.read_text(encoding="utf-8"))
            python_requires = service_meta.get("python_requires", default_python_requires)
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
