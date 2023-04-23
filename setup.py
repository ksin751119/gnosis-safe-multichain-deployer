"""Python setup.py for gnosis_safe_multichain_deployer package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("gnosis_safe_multichain_deployer", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="gnosis_safe_multichain_deployer",
    version=read("gnosis_safe_multichain_deployer", "VERSION"),
    description="Awesome gnosis_safe_multichain_deployer created by ksin751119",
    url="https://github.com/ksin751119/gnosis-safe-multichain-deployer/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="ksin751119",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["gnosis_safe_multichain_deployer = gnosis_safe_multichain_deployer.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
