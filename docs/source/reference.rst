Reference
=========

**spectraplotpy** is made up of four decoupled building blocks, the first one is
the :ref:`dataset`, the :ref:`importers`, the :ref:`spectra` and the :ref:`exporters`.

The :ref:`importers` take data from several different formated files, and populate a
:ref:`dataset`, then the the :ref:`dataset` can be passed around to the :ref:`spectra`
in order to do some processing and plotting or directly to the :ref:`exporters`.


.. _dataset:

Dataset
-------

The dataset module defines the datastructure shared among the **spectraplotpy**
classes, you need to implement a similar interface in order to leverage the class.

.. autoclass:: spectraplotpy.Dataset
    :members:

The users are encouraged to directly access the data members of this class, and
is up to them to keep the data consistently.

.. code:: python

    import spectrapotpy as spp
    import numpy as np

    ds = spp.Dataset()
    ds.x = np.arrange(0, np.pi, 1000)
    ds.y = np.sin(x)


.. _importers:

Importers
---------

The importers functionalities to parse input from several file types,
it also allows you to easily create new importers for your own formats 
subclasing the `Importer` class and overriding some methods.

.. autoclass:: spectraplotpy.Importer
    :members:

The library provides several importer for several formats, and the users
are encouraged to create their own.

.. autoclass:: spectraplotpy.AvivImporter
    :members:

.. autoclass:: spectraplotpy.MosImporter
    :members:

Examples
........

Importing from an Aviv file,

.. code:: python

    import spectraplotpy as spp
    avii = AvivImporter('filename.cd')
    # then you can access the dataset and pass it around
    print avii.dataset.x, avii,dataset.y


Creating a custom importer,

.. code:: python

    import spectraplotpy as spp

    class XRDPanalithicalImporter(spp.Importer):
        def parse_metadata(self, metadata_txt):
            # override this function to get the
            pass

        def parse_data(self, data_txt):
            # override this to parse your custom data
            pass
    

.. _spectra:

Spectra
-------

The `Spectrum` class provides some functionalities that allow the users to operate
their data in a very intuitive fashion.

.. autoclass:: spectraplotpy.Spectrum
    :members:
    :special-members:

.. _exporters:

Exporters
---------

Much like :ref:`importers`, exporters provide functionality to export
to several file formats, there are text based exporters and plot based
exporters.

.. autoclass:: spectraplotpy.BaseTextExporter
    :members:

.. autoclass:: spectraplotpy.BaseGraphicExporter
    :members:
