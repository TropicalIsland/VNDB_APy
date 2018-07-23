import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vndbwrapper",
    version="0.0.1",
    author="Andrew McLean",
    author_email="andrewmclean5465@gmail.com",
    description="A Python wrapper for the VNDB public database API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TropicalIsland/VNDB_APy/",
    packages=['vndbwrapper'],
    install_requires=[
          'requests',
          ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)