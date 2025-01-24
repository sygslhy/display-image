from setuptools import setup, find_packages

setup(
    entry_points={
        'console_scripts': [
            'yourscript = yourpackage.scripts.yourscript:cli',
        ],
    },
)
