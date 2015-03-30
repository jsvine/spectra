import sys
from setuptools import setup, find_packages

setup(
    name="spectra",
    version="0.0.6",
    description="Color scales and color conversion made easy for Python.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3"
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
    install_requires=[
        "numpy",
        "networkx",
        "colormath",
    ],
    tests_require=[],
    test_suite="test"
)
