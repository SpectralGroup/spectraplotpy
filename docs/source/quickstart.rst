Quick Start
===========

Getting started
---------------

**spectraplotpy** helps you with common task when analaysing spectral data, 
providing functionalities for reading and writing several data formats,
process and plot several kinds of spectra.

In order to install the library, you download this repository and build the
package with setup tools,

.. code::

    $ git clone https://github.com/odarbelaeze/spectraplotpy.git
    $ cd spectraplotpy
    $ python setup.py install

Loading a generic spectrum from an Aviv formated file in the python environment:

.. code:: python

    >>> from spectraplotpy import AvivImporter
    >>> from spectraplotpy import Spectrum
    >>> a = AvivImporter('spectral_data_file_path/filename')
    >>> s = Spectrum(a.dataset)
    
Adding two spectral datasets:

.. code:: python

    >>> a1 = AvivImporter('spectral_data_file_path/filename2')
    >>> s1 = Spectrum(a1.dataset)
    >>> s2 = s.sub(s1)	# s2 = s - s1
    
Plotting the spectrum with the default plot settings,

.. code:: python

    import matplotlib.pyplot as plt
    s.plot(plt)
    plt.show()

Exporting the spectrum to a CSVFile:

.. code:: python

    from spectraplotpy import CSVExporter
    csve = CSVExporter(s.dataset)
    csve.save('myspectrum.csv')
    
Futher operations can be gotten from the detailed documentation.

Development setup (for developer)
---------------------------------

The basic dependencies to develop the project are,

.. code::

    matplotlib
    scipy
    numpy
    pytest # For testing
    sphinx # For documentation
    pylint # For pep-8 compilance

You can install de dependecies through pip,

.. code::

    $ pip install matplotlib scipy numpy pytest sphinx pylint

or just let the setup script to install them for you.

In order to develop using virtual env, within your virtual env just call

.. code::

    $ python setup.py develop

this will allow you to do `import spectraplotpy` anywhere in your filesystem.

Testing
-------

Once you get everything set up, you can run the tests using,

.. code::

    $ python setup.py test

Before you do a pull request make sure your code agrees with pylint
(as far as possible) and passes all tests.

In order to run the tests for the `Importer` classes you'll need to
provide some sample data available trough the trello board.
