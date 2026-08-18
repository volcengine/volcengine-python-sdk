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


def discovered_dependency_graph(manifest):
    modules = set(manifest["modules"])
    return {
        module: imported_sdk_modules(module, modules)
        for module in manifest["modules"]
    }


def declared_dependency_graph(manifest):
    default_dependencies = manifest["default_internal_dependencies"]
    overrides = manifest["internal_dependencies"]
    return {
        module: list(overrides.get(module, default_dependencies))
        for module in manifest["modules"]
    }


def validate_manifest(manifest, verify_imports=False):
    errors = []
    modules = manifest.get("modules", [])
    excluded_modules = set(manifest.get("excluded_modules", {}))

    if manifest.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if modules != sorted(modules):
        errors.append("modules must be sorted")
    if len(modules) != len(set(modules)):
        errors.append("modules contains duplicate entries")
    if "volcenginesdkcore" not in modules:
        errors.append("volcenginesdkcore must be published")

    discovered_modules = {
        path.name
        for path in ROOT.iterdir()
        if path.is_dir() and path.name.startswith(MODULE_PREFIX)
    }
    declared_modules = set(modules) | excluded_modules
    undeclared = sorted(discovered_modules - declared_modules)
    missing = sorted(declared_modules - discovered_modules)
    if undeclared:
        errors.append("undeclared SDK modules: {}".format(", ".join(undeclared)))
    if missing:
        errors.append("manifest modules missing from source: {}".format(", ".join(missing)))

    distributions = [distribution_name(module, manifest) for module in modules]
    if len(distributions) != len(set(distributions)):
        errors.append("multiple modules map to the same distribution")

    external_dependencies = manifest.get("external_dependencies", {})
    unknown_overrides = sorted(set(external_dependencies) - set(modules))
    if unknown_overrides:
        errors.append(
            "dependency overrides reference unknown modules: {}".format(
                ", ".join(unknown_overrides)
            )
        )

    internal_dependencies = manifest.get("internal_dependencies", {})
    default_internal_dependencies = manifest.get("default_internal_dependencies", [])
    unknown_default_dependencies = sorted(
        set(default_internal_dependencies) - set(modules)
    )
    if unknown_default_dependencies:
        errors.append(
            "default internal dependencies reference unknown modules: {}".format(
                ", ".join(unknown_default_dependencies)
            )
        )
    unknown_internal_overrides = sorted(set(internal_dependencies) - set(modules))
    if unknown_internal_overrides:
        errors.append(
            "internal dependency overrides reference unknown modules: {}".format(
                ", ".join(unknown_internal_overrides)
            )
        )
    known_modules = set(modules)
    for module, dependencies in internal_dependencies.items():
        unknown_dependencies = sorted(set(dependencies) - known_modules)
        if unknown_dependencies:
            errors.append(
                "{} references unknown dependencies: {}".format(
                    module, ", ".join(unknown_dependencies)
                )
            )

    python_requires = manifest.get("python_requires", {})
    if "default" not in python_requires:
        errors.append("python_requires.default is required")
    unknown_python_overrides = sorted(
        set(python_requires) - set(modules) - {"default"}
    )
    if unknown_python_overrides:
        errors.append(
            "python_requires references unknown modules: {}".format(
                ", ".join(unknown_python_overrides)
            )
        )

    if errors:
        return errors, {}

    graph = declared_dependency_graph(manifest)
    if verify_imports:
        discovered_graph = discovered_dependency_graph(manifest)
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
    external_requirements = manifest["external_dependencies"].get(
        module,
        manifest["default_product_dependencies"],
    )
    return internal_requirements + external_requirements


def python_requires_for(module, manifest):
    return manifest["python_requires"].get(
        module,
        manifest["python_requires"]["default"],
    )


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


def stage_meta(stage_dir):
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


def resolve_selection(requested, manifest):
    module_by_distribution = {
        distribution_name(module, manifest): module for module in manifest["modules"]
    }
    module_names = set(manifest["modules"])
    if not requested:
        return list(manifest["modules"]) + [META_DISTRIBUTION]

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


def build_packages(args, manifest, graph):
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

    selected = resolve_selection(args.packages, manifest)
    with tempfile.TemporaryDirectory(prefix="volcengine-sdk-split-") as temporary_dir:
        temporary_root = Path(temporary_dir)
        for index, package in enumerate(selected, 1):
            stage_dir = temporary_root / "stage"
            if stage_dir.exists():
                shutil.rmtree(stage_dir)
            stage_dir.mkdir()

            display_name = package
            if package == META_DISTRIBUTION:
                stage_meta(stage_dir)
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

    if args.command == "validate":
        edge_count = sum(len(dependencies) for dependencies in graph.values())
        print(
            "validated {} distributions and {} internal dependency edges".format(
                len(manifest["modules"]), edge_count
            )
        )
        return 0

    if args.command == "list":
        for module in manifest["modules"]:
            print("{}\t{}".format(module, distribution_name(module, manifest)))
        print("-\t{}".format(META_DISTRIBUTION))
        return 0

    if args.command == "build":
        if not args.version:
            args.version = manifest["version"]
        try:
            build_packages(args, manifest, graph)
        except (OSError, subprocess.CalledProcessError, ValueError) as exc:
            print("error: {}".format(exc), file=sys.stderr)
            return 1
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
