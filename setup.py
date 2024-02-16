from setuptools import setup, find_packages

setup(
    name="catzilla",
    description="A CLI based app to interact with Gunadarma's Catzilla RaspberryPi 4 Robot system"
    version="0.0.2",
    packages=find_packages(["cli"]),
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "catzilla = cli.main:cli",
        ],
    },
)
