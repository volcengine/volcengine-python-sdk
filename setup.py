# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "volcengine-python-sdk"
VERSION = "1.0.31"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

setup(
    name=NAME,
    version=VERSION,
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    description='Volcengine SDK for Python',
    license="Apache License 2.0",
    platforms='any',
    url='https://github.com/volcengine/volcengine-python-sdk',
)
