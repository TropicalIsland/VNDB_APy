
from glob import glob
from os.path import basename

from os.path import splitext

from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="vndbwrapper",
    version="0.0.1",
    author="Andrew McLean",
    author_email="andrewmclean5465@gmail.com",
    description="A Python wrapper for the VNDB public database API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TropicalIsland/VNDB_APy/",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)