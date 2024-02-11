from setuptools import setup, find_packages

setup(
    name="catzilla-cli",
    version="0.0.1",
    packages=find_packages(["cli"]),
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "catzilla = cli.main:main",
        ],
    },
)
