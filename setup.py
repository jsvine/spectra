import sys, os
from setuptools import setup, find_packages
import subprocess

NAME = "spectra"
HERE = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(HERE, NAME, "_version.py")) as f:
    exec(f.read(), {}, version_ns)

with open(os.path.join(HERE, "requirements.txt")) as f:
    reqs = f.read().strip().split("\n")

setup(
    name=NAME,
    version=version_ns["__version__"],
    description="Color scales and color conversion made easy for Python.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    keywords="color colors colorspace scale spectrum",
    author="Jeremy Singer-Vine",
    author_email="jsvine@gmail.com",
    url="http://github.com/jsvine/spectra",
    license="MIT",
    packages=find_packages(exclude=["test",]),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=reqs,
    tests_require=[],
    test_suite="test"
)
