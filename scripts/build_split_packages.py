#!/usr/bin/env python3
"""Validate and build the Volcengine Python SDK split distributions."""

import argparse
import ast
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "split-packages.json"
META_DISTRIBUTION = "volcengine-python-sdk"
MODULE_PREFIX = "volcenginesdk"
ARTIFACT_SUFFIXES = (".whl", ".tar.gz")
# 体积门禁（ECS 目标）：core + 单产品 wheel 合计 ≤ 15 MB
SIZE_GATE_MODULES = ("volcenginesdkcore", "volcenginesdkecs")
SIZE_GATE_LIMIT_BYTES = 15 * 1024 * 1024


def load_manifest():
    with MANIFEST_PATH.open(encoding="utf-8") as manifest_file:
        return json.load(manifest_file)


def discover_modules(manifest):
    """扫描仓内 volcenginesdk* 目录，排除 excluded_modules 与非包目录。

    模块清单不再由根 manifest 维护（避免并发服务生成时合并冲突），
    每个服务的元数据在其自身目录的 split-package.json 中。
    """
    excluded = set(manifest.get("excluded_modules", {}))
    modules = sorted(
        path.name
        for path in ROOT.iterdir()
        if path.is_dir()
        and path.name.startswith(MODULE_PREFIX)
        and path.name not in excluded
    )
    return modules


def load_service_metadata(module, manifest):
    """读取服务自带的 split-package.json；缺失字段回退根 manifest 默认值。"""
    defaults = {
        "internal_dependencies": list(manifest.get("default_internal_dependencies", [])),
        "external_dependencies": list(manifest.get("default_product_dependencies", [])),
        "python_requires": manifest.get("default_python_requires", ">=2.7"),
    }
    metadata_path = ROOT / module / "split-package.json"
    if not metadata_path.is_file():
        return defaults
    with metadata_path.open(encoding="utf-8") as metadata_file:
        overrides = json.load(metadata_file)
    for key in defaults:
        if key in overrides:
            defaults[key] = overrides[key]
    return defaults


def distribution_name(module, manifest):
    if module == "volcenginesdkcore":
        return "volcenginesdk-core"
    return manifest["distribution_prefix"] + module[len(MODULE_PREFIX):]


def imported_sdk_modules(module, known_modules):
    dependencies = set()
    for source_path in (ROOT / module).rglob("*.py"):
        try:
            tree = ast.parse(source_path.read_bytes(), filename=str(source_path))
        except (SyntaxError, UnicodeDecodeError) as exc:
            raise ValueError("cannot parse {}: {}".format(source_path, exc))

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                imported_names = [node.module]
            else:
                continue

            for imported_name in imported_names:
                imported_module = imported_name.split(".", 1)[0]
                if imported_module in known_modules and imported_module != module:
                    dependencies.add(imported_module)
    return sorted(dependencies)


def discovered_dependency_graph(modules):
    known = set(modules)
    return {module: imported_sdk_modules(module, known) for module in modules}


def declared_dependency_graph(modules, manifest):
    return {
        module: list(load_service_metadata(module, manifest)["internal_dependencies"])
        for module in modules
    }


def validate_manifest(manifest, verify_imports=False):
    errors = []
    excluded_modules = set(manifest.get("excluded_modules", {}))

    if manifest.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if "distribution_prefix" not in manifest:
        errors.append("distribution_prefix is required")
    if "default_python_requires" not in manifest:
        errors.append("default_python_requires is required")

    # 模块清单由目录扫描得出（不再由根 manifest 维护）
    modules = discover_modules(manifest)
    if "volcenginesdkcore" not in modules:
        errors.append("volcenginesdkcore must be published")

    # 每个服务的元数据文件必须存在且字段合法
    metadata = {}
    for module in modules:
        try:
            meta = load_service_metadata(module, manifest)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append("{}: invalid split-package.json: {}".format(module, exc))
            continue
        metadata[module] = meta
        unknown_deps = sorted(set(meta["internal_dependencies"]) - set(modules))
        if unknown_deps:
            errors.append(
                "{} references unknown dependencies: {}".format(
                    module, ", ".join(unknown_deps)
                )
            )

    discovered_modules = {
        path.name
        for path in ROOT.iterdir()
        if path.is_dir() and path.name.startswith(MODULE_PREFIX)
    }
    undeclared = sorted(discovered_modules - set(modules) - excluded_modules)
    if undeclared:
        errors.append("undeclared SDK modules: {}".format(", ".join(undeclared)))

    distributions = [distribution_name(module, manifest) for module in modules]
    if len(distributions) != len(set(distributions)):
        errors.append("multiple modules map to the same distribution")

    if errors:
        return errors, {}

    graph = declared_dependency_graph(modules, manifest)
    if verify_imports:
        discovered_graph = discovered_dependency_graph(modules)
        for module in modules:
            if graph[module] != discovered_graph[module]:
                errors.append(
                    "{} dependencies differ: declared={}, discovered={}".format(
                        module,
                        ",".join(graph[module]),
                        ",".join(discovered_graph[module]),
                    )
                )
    for module, dependencies in graph.items():
        if module != "volcenginesdkcore" and not dependencies:
            errors.append("{} has no SDK dependency".format(module))

    visiting = set()
    visited = set()

    def visit(module, path):
        if module in visiting:
            errors.append("dependency cycle: {}".format(" -> ".join(path + [module])))
            return
        if module in visited:
            return
        visiting.add(module)
        for dependency in graph[module]:
            visit(dependency, path + [module])
        visiting.remove(module)
        visited.add(module)

    for module in modules:
        visit(module, [])

    def reaches_core(module, seen):
        if module == "volcenginesdkcore":
            return True
        if module in seen:
            return False
        return any(reaches_core(dependency, seen | {module}) for dependency in graph[module])

    for module in modules:
        if not reaches_core(module, set()):
            errors.append("{} does not transitively depend on core".format(module))

    total_size = sum(staged_wheel_size(module) for module in SIZE_GATE_MODULES)
    if total_size > SIZE_GATE_LIMIT_BYTES:
        errors.append(
            "size gate: {} + {} wheel estimate {:.1f} MB exceeds {:.0f} MB".format(
                SIZE_GATE_MODULES[0],
                SIZE_GATE_MODULES[1],
                total_size / 1024 / 1024,
                SIZE_GATE_LIMIT_BYTES / 1024 / 1024,
            )
        )

    return errors, graph


def staged_wheel_size(module):
    """估算 wheel 体积：与 wheel 相同的 ZIP_DEFLATED 压缩包内全部文件。"""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for source_path in sorted((ROOT / module).rglob("*")):
            if source_path.is_file():
                archive.write(source_path, source_path.relative_to(ROOT))
        for extra in ("LICENSE.txt", "NOTICE.md"):
            extra_path = ROOT / extra
            if extra_path.is_file():
                archive.write(extra_path, extra)
    return buffer.tell()


def requirements_for(module, version, manifest, graph):
    internal_requirements = [
        "{}=={}".format(distribution_name(dependency, manifest), version)
        for dependency in graph[module]
    ]
    external_requirements = load_service_metadata(module, manifest)[
        "external_dependencies"
    ]
    return internal_requirements + external_requirements


def python_requires_for(module, manifest):
    return load_service_metadata(module, manifest)["python_requires"]


def write_text(path, content):
    path.write_text(content, encoding="utf-8")


def stage_product(module, version, manifest, graph, stage_dir):
    distribution = distribution_name(module, manifest)
    shutil.copytree(ROOT / module, stage_dir / module)
    shutil.copy2(ROOT / "LICENSE.txt", stage_dir / "LICENSE.txt")
    shutil.copy2(ROOT / "NOTICE.md", stage_dir / "NOTICE.md")

    readme = """# {distribution}

This distribution contains the `{module}` import package from the Volcengine
Python SDK. Install `volcengine-python-sdk` to install every service package.
""".format(distribution=distribution, module=module)
    write_text(stage_dir / "README.md", readme)
    write_text(
        stage_dir / "pyproject.toml",
        """[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
""",
    )
    write_text(
        stage_dir / "MANIFEST.in",
        """include LICENSE.txt
include NOTICE.md
include README.md
recursive-include {module} *.proto
""".format(module=module),
    )

    python_requires = python_requires_for(module, manifest)
    universal_wheel = python_requires == ">=2.7"
    setup_source = """# coding: utf-8
from io import open
from setuptools import find_packages, setup

setup(
    name={distribution!r},
    version={version!r},
    description={description!r},
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="volc-engine",
    author_email="volc-sdk-team@bytedance.com",
    url="https://github.com/volcengine/volcengine-python-sdk",
    license="Apache License 2.0",
    license_files=("LICENSE.txt",),
    platforms="any",
    packages=find_packages(include=[{module!r}, {module_prefix!r}]),
    include_package_data=True,
    install_requires={requirements!r},
    python_requires={python_requires!r},
    options={{"bdist_wheel": {{"universal": {universal_wheel!r}}}}},
)
""".format(
        distribution=distribution,
        version=version,
        description="Volcengine {} SDK for Python".format(module[len(MODULE_PREFIX):]),
        module=module,
        module_prefix=module + ".*",
        requirements=requirements_for(module, version, manifest, graph),
        python_requires=python_requires,
        universal_wheel=universal_wheel,
    )
    write_text(stage_dir / "setup.py", setup_source)


def stage_meta(stage_dir, modules, manifest):
    for filename in (
        "LICENSE.txt",
        "MANIFEST.in",
        "NOTICE.md",
        "README.md",
        "pyproject.toml",
        "setup.py",
        "split-packages.json",
    ):
        shutil.copy2(ROOT / filename, stage_dir / filename)
    # 元包 install_requires 需要完整模块清单；stage 目录不含各服务源码目录，
    # 由构建方把扫描出的模块清单写入 stage，setup.py 优先读取。
    with (stage_dir / "split-modules.json").open("w", encoding="utf-8") as modules_file:
        json.dump({"modules": modules}, modules_file)


def build_staged_package(
    stage_dir,
    output_dir,
    formats,
    version=None,
    no_isolation=False,
    verbose=False,
):
    command = [
        sys.executable,
        "-m",
        "build",
        "--outdir",
        str(output_dir),
    ]
    if no_isolation:
        command.extend(("--no-isolation", "--skip-dependency-check"))
    if "wheel" in formats:
        command.append("--wheel")
    if "sdist" in formats:
        command.append("--sdist")

    environment = os.environ.copy()
    if version is not None:
        environment["VOLCENGINE_SDK_BUILD_VERSION"] = version
    completed = subprocess.run(
        command,
        cwd=str(stage_dir),
        env=environment,
        stdout=None if verbose else subprocess.PIPE,
        stderr=None if verbose else subprocess.STDOUT,
        universal_newlines=True,
    )
    if completed.returncode:
        if completed.stdout:
            print(completed.stdout, file=sys.stderr)
        raise subprocess.CalledProcessError(completed.returncode, command)


def resolve_selection(requested, manifest, modules):
    module_by_distribution = {
        distribution_name(module, manifest): module for module in modules
    }
    module_names = set(modules)
    if not requested:
        return list(modules) + [META_DISTRIBUTION]

    selected = []
    for item in requested:
        if item == META_DISTRIBUTION:
            resolved = META_DISTRIBUTION
        elif item in module_names:
            resolved = item
        elif item in module_by_distribution:
            resolved = module_by_distribution[item]
        else:
            raise ValueError("unknown package: {}".format(item))
        if resolved not in selected:
            selected.append(resolved)
    return selected


def build_packages(args, manifest, graph, modules):
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    existing_artifacts = [
        path for path in output_dir.iterdir()
        if path.name.endswith(ARTIFACT_SUFFIXES)
    ]
    if existing_artifacts:
        raise ValueError(
            "output directory already contains package artifacts: {}".format(output_dir)
        )

    selected = resolve_selection(args.packages, manifest, modules)
    with tempfile.TemporaryDirectory(prefix="volcengine-sdk-split-") as temporary_dir:
        temporary_root = Path(temporary_dir)
        for index, package in enumerate(selected, 1):
            stage_dir = temporary_root / "stage"
            if stage_dir.exists():
                shutil.rmtree(stage_dir)
            stage_dir.mkdir()

            display_name = package
            if package == META_DISTRIBUTION:
                stage_meta(stage_dir, modules, manifest)
                version_override = args.version
            else:
                stage_product(package, args.version, manifest, graph, stage_dir)
                display_name = distribution_name(package, manifest)
                version_override = None

            print("[{}/{}] building {}".format(index, len(selected), display_name), flush=True)
            build_staged_package(
                stage_dir,
                output_dir,
                set(args.formats),
                version=version_override,
                no_isolation=args.no_isolation,
                verbose=args.verbose,
            )

    print("built {} distributions in {}".format(len(selected), output_dir))


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate the manifest and dependency graph")
    subparsers.add_parser("list", help="list module-to-distribution mappings")

    build_parser = subparsers.add_parser("build", help="build split package artifacts")
    build_parser.add_argument(
        "--version",
        help="version for every generated distribution",
    )
    build_parser.add_argument(
        "--output-dir",
        default="dist/split",
        help="artifact directory, relative to the repository root by default",
    )
    build_parser.add_argument(
        "--package",
        dest="packages",
        action="append",
        help="module or distribution to build; repeat to select multiple",
    )
    build_parser.add_argument(
        "--formats",
        nargs="+",
        choices=("wheel", "sdist"),
        default=("wheel", "sdist"),
        help="artifact formats to build",
    )
    build_parser.add_argument(
        "--no-isolation",
        action="store_true",
        help="reuse preinstalled build tools instead of an isolated environment",
    )
    build_parser.add_argument(
        "--verbose",
        action="store_true",
        help="show output from the underlying package builds",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    manifest = load_manifest()
    errors, graph = validate_manifest(
        manifest,
        verify_imports=args.command == "validate",
    )
    if errors:
        for error in errors:
            print("error: {}".format(error), file=sys.stderr)
        return 1

    modules = discover_modules(manifest)

    if args.command == "validate":
        edge_count = sum(len(dependencies) for dependencies in graph.values())
        print(
            "validated {} distributions and {} internal dependency edges".format(
                len(modules), edge_count
            )
        )
        return 0

    if args.command == "list":
        for module in modules:
            print("{}\t{}".format(module, distribution_name(module, manifest)))
        print("-\t{}".format(META_DISTRIBUTION))
        return 0

    if args.command == "build":
        if not args.version:
            args.version = manifest["version"]
        try:
            build_packages(args, manifest, graph, modules)
        except (OSError, subprocess.CalledProcessError, ValueError) as exc:
            print("error: {}".format(exc), file=sys.stderr)
            return 1
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
