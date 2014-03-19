""" Exporter Program """

from StringIO import StringIO
import numpy as np

class Exporter(object):
    """ Class Exporter """

    def __init__(self, dataset):
        self.dataset = dataset


class BaseTextExporter(Exporter):
    """docstring for BaseTextExporter"""

    def __str__(self):
        # For instance
        return self.text()

    def metadata_to_text(self):
        """This writes the metadata to a given file"""
        return "Meta data text"


    def data_to_text(self):
        """ This writes the data to a given file """
        return "Data text"

    def text(self):
        return self.metadata_to_text() + "\n" + self.data_to_text()

    def write(self, file_handler, *args, **kwargs):
        file_handler.write(self.text(), *args, **kwargs)  
    
    def save(self, filename, *args, **kwargs):
        with open(filename, 'w') as file_handler:
            self.write(file_handler, *args, **kwargs)


class BasePlotExporter(Exporter):
    """docstring for BasePlotExporter"""

    def plot(self, axis, *args, **kwargs):
        # Cases for error bars and labels
        axis.plot(self.dataset.x, self.dataset.y, *args, **kwargs)


class CSVExporter(BaseTextExporter):
    """Saving to CSV file"""

    def metadata_to_text(self):
        """This writes the metadata to a given csv file"""
        return "# {0}".format(self.dataset.metadata)

    def data_to_text(self):
        """ This writes the data to a given csv file """
        s = StringIO("")
        np.savetxt(s, np.column_stack((self.dataset.x, self.dataset.y)))
        s.seek(0)
        return s.read()
        

class AvivExporter(CSVExporter):
    """"""

    def metadata_to_text(self):
        """This writes the metadata to a given csv file"""
        text = "data_name something"
        for key in self.dataset.metadata:
            text += "\n_{key}_ {value}".format(
                key=key,
                value=self.dataset.metadata[key]
            )
        return text

    def data_to_text(self):
        """ This writes the data to a given csv file """
        return "_data_\n" + super(AvivExporter, self).data_to_text()
