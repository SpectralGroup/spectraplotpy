spectraplotpy
=============

A spectrum manipulation library.

Development setup
-----------------

The basic dependencies to develop the project are,

    matplotlib
    scipy
    numpy
    pytest # For testing
    sphinx # For documentation
    pylint # For pep-8 compilance

In order to develop using virtual env, within your virtual env just call

    python setup.py develop

this will allow you to do `import spectraplotpy` anywhere in your filesystem.

Testing
-------

Once you get everything setted up, you can run the tests using,

    python setup.py test

Before you do a pull request make sure your code agrees with pylint
(as far as possible) and passes all tests.

In order to run the tests for the `Importer` classes you'll need to
provide some sample data available through the google group.
