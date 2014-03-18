"""
This is a basic setuptools file.
"""

from setuptools import setup, find_packages

setup(
    name = "spectraplotpy",
    version = "0.0.1",
    packages = find_packages(),
    scripts = [],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = [],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.md'],
        # And include any *.msg files found in the 'hello' package, too:
        #'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "SpectralGroup",
    author_email = "odarbelaeze@gmail.com",
    description = "A spectrum manipulation library",
    license = "DBAA",
    keywords = "spectrum ploting 2D",

    # project home page, if any
    url = "https://github.com/odarbelaeze/spectraplotpy",   

    # could also include long_description, download_url, classifiers, etc.
)
