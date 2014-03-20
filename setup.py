"""
This is a basic setuptools file.
"""

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    """
    Unit test wrapper for the PyTest, including coverage repport
    """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--cov', 'spectraplotpy', 'test/'] #['--cov spectraplotpy tests/']
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name="spectraplotpy",
    version="0.0.1",
    packages=find_packages(),
    scripts=[],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "sphinx"
    ],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.md'],
        # And include any *.msg files found in the 'hello' package, too:
        #'hello': ['*.msg'],
    },

    # Project uses pytest for the tests

    tests_require=[
        'pytest',
        'pytest-cov',
        'mock'
    ],
    
    cmdclass={
        'test': PyTest
    },

    # metadata for upload to PyPI
    author="SpectralGroup",
    author_email="odarbelaeze@gmail.com",
    description="A spectrum manipulation library",
    license="DBAA",
    keywords="spectrum ploting 2D",

    # project home page, if any
    url="https://github.com/odarbelaeze/spectraplotpy",   

    # could also include long_description, download_url, classifiers, etc.
)
