# coding: utf-8

import json
import os
from io import open

from setuptools import setup


ROOT = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(ROOT, "split-packages.json")) as manifest_file:
    MANIFEST = json.load(manifest_file)

VERSION = os.environ.get("VOLCENGINE_SDK_BUILD_VERSION", MANIFEST["version"])
PREFIX = "volcenginesdk"


def _load_modules_state():
    """模块清单：优先读构建方写入的 split-modules.json（stage 目录无源码目录，
    也读不到各服务 split-package.json，故 python_requires 一并由该文件携带）；
    否则扫描仓内 volcenginesdk* 目录（不含 excluded_modules）。"""
    modules_file = os.path.join(ROOT, "split-modules.json")
    if os.path.isfile(modules_file):
        with open(modules_file) as f:
            state = json.load(f)
        return state["modules"], state.get("python_requires", {})
    excluded = set(MANIFEST.get("excluded_modules", {}))
    modules = sorted(
        name
        for name in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, name))
        and name.startswith(PREFIX)
        and name not in excluded
    )
    return modules, {}


MODULES, STAGED_PYTHON_REQUIRES = _load_modules_state()


def discover_modules():
    return MODULES


def distribution_name(module):
    if module == "volcenginesdkcore":
        return "volcenginesdk-core"
    overrides = MANIFEST.get("distribution_name_overrides", {})
    if module in overrides:
        return overrides[module]
    return MANIFEST["distribution_prefix"] + module[len(PREFIX):]


def service_python_requires(module):
    """构建 stage 中已由 split-modules.json 携带的，直接用；否则读取服务自带的
    split-package.json 声明的 python_requires；缺失回退默认值。"""
    if module in STAGED_PYTHON_REQUIRES:
        return STAGED_PYTHON_REQUIRES[module]
    service_meta_path = os.path.join(ROOT, module, "split-package.json")
    if os.path.isfile(service_meta_path):
        with open(service_meta_path) as service_meta_file:
            service_meta = json.load(service_meta_file)
        if "python_requires" in service_meta:
            return service_meta["python_requires"]
    return MANIFEST["default_python_requires"]


def meta_requirement(module):
    requirement = "{}=={}".format(distribution_name(module), VERSION)
    python_requires = service_python_requires(module)
    if python_requires and python_requires.startswith(">="):
        requirement += "; python_version >= '{}'".format(python_requires[2:])
    return requirement


setup(
    name="volcengine-python-sdk",
    version=VERSION,
    install_requires=[meta_requirement(module) for module in discover_modules()],
    packages=[],
    description="Volcengine SDK for Python (all services)",
    long_description=open(os.path.join(ROOT, "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="volc-engine",
    author_email="volc-sdk-team@bytedance.com",
    license="Apache License 2.0",
    platforms="any",
    url="https://github.com/volcengine/volcengine-python-sdk",
    python_requires=MANIFEST["default_python_requires"],
    options={"bdist_wheel": {"universal": True}},
)
