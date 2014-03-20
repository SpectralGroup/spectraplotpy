Reference
=========

Dataset Module
--------------

The dataset module defines the datastructure shared among the **spectraplotpy**
classes, you need to implement a similar interface in order to leverage the class.

.. autoclass:: spectraplotpy.Dataset
   :members:        

Importer Module
---------------

The importer module provides functionalities to parse imput from several file types,
it also allows you to easyly create new importers fro your own formats subclasing the
`Importer` class and overriding some methods.

.. autoclass:: spectraplotpy.Importer
   :members:

.. autoclass:: spectraplotpy.AvivImporter
   :members:

.. autoclass:: spectraplotpy.MosImporter
   :members:

