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


def distribution_name(module):
    if module == "volcenginesdkcore":
        return "volcenginesdk-core"
    return MANIFEST["distribution_prefix"] + module[len(PREFIX):]


def meta_requirement(module):
    requirement = "{}=={}".format(distribution_name(module), VERSION)
    python_requires = MANIFEST["python_requires"].get(module)
    if python_requires and python_requires.startswith(">="):
        requirement += "; python_version >= '{}'".format(python_requires[2:])
    return requirement


setup(
    name="volcengine-python-sdk",
    version=VERSION,
    install_requires=[meta_requirement(module) for module in MANIFEST["modules"]],
    packages=[],
    description="Volcengine SDK for Python (all services)",
    long_description=open(os.path.join(ROOT, "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="volc-engine",
    author_email="volc-sdk-team@bytedance.com",
    license="Apache License 2.0",
    platforms="any",
    url="https://github.com/volcengine/volcengine-python-sdk",
    python_requires=MANIFEST["python_requires"]["default"],
    options={"bdist_wheel": {"universal": True}},
    extras_require={
        "ark": [
            "volcenginesdk-arkruntime=={}; python_version >= '3.10'".format(VERSION)
        ]
    },
)
