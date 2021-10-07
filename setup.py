#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fp:
    install_requires = fp.read().splitlines()

setup(
    name="conwhat", 
    version="0.1",
    author="John David Griffiths",
    author_email="j.davidgriffiths@gmail.com",
    description='python library for connectivity based white matter atlas analysis',
    keywords='white matter, tractography, MRI, DTI, diffusion, python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = install_requires,
    url='https://github.com/griffithslab/conwhat',
    license="BSD (3-clause)",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
