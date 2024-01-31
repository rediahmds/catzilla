from setuptools import setup

setup(
    name='catzilla',
    version='0.0.1',
    py_modules=['catzilla'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'catzilla = catzilla:cli',
        ],
    },
)