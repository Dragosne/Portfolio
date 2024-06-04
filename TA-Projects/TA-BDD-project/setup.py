from setuptools import setup, find_packages

setup(
    name="BDD-tmta19",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "requests",
        "behave",
    ],
)
