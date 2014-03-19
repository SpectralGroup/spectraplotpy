spectraplotpy
=============

A spectrum manipulation library.

Getting started
---------------

*spectraplotpy* helps you with common task when analaysing spectral data,
it provides functionalities for reading and writing several data formats,
process and plot several kinds of spectra.

In order to install the library you download this repository and build the
package with setup tools,

    $ git clone https://github.com/odarbelaeze/spectraplotpy.git
    $ cd spectraplotpy
    $ python setup.py install

Loading a generic spectrum from an Aviv formated file:

    from spectraplotpy import AvivImporter
    from spectraplotpy import Spectrum
    a = AvivImporter('filename')
    s = Spectrum(a.dataset)

Plotting the spectrum with the default plot settings,

    import matplotlib.pyplot as plt
    s.plot(plt)
    plt.show()

Exporting the spectrum to a CSVFile:

    from spectraplotpy import CSVExporter
    csve = CSVExporter(s.dataset)
    csve.save('myspectrum.csv')


Development setup
-----------------

The basic dependencies to develop the project are,

    matplotlib
    scipy
    numpy
    pytest # For testing
    sphinx # For documentation
    pylint # For pep-8 compilance

    $ pip install matplotlib scipy numpy pytest sphinx pylint

In order to develop using virtual env, within your virtual env just call

    $ python setup.py develop

this will allow you to do `import spectraplotpy` anywhere in your filesystem.

Testing
-------

Once you get everything set up, you can run the tests using,

    python setup.py test

Before you do a pull request make sure your code agrees with pylint
(as far as possible) and passes all tests.

In order to run the tests for the `Importer` classes you'll need to
provide some sample data available trough the trello board.
