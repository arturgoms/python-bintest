from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()

setup(
    name="bintest",
    version="0.2",
    packages=["src"],
    url="https://github.com/arturgoms/python-bintest",
    license="MIT",
    author="Artur Gomes",
    author_email="contato@arturgomes.com.br",
    description="Python library that is a extension of unittest to test binarys using a YAML file",
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.9",
    install_requires=["scripttest"],
)
