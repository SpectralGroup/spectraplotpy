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
        """ This return metadata and data to handler file"""
        return self.metadata_to_text() + "\n" + self.data_to_text()

    def write(self, file_handler, *args, **kwargs):
        """ This write metadata and data to handler file"""
        file_handler.write(self.text(), *args, **kwargs)  
    
    def save(self, filename, *args, **kwargs):
        """ This save metadata and data to handler file"""
        with open(filename, 'w') as file_handler:
            self.write(file_handler, *args, **kwargs)


class BasePlotExporter(Exporter):
    """docstring for BasePlotExporter"""

    def plot(self, axis, *args, **kwargs):
        """ plotting Data"""
        axis.plot(self.dataset.x, self.dataset.y, *args, **kwargs)


class CSVExporter(BaseTextExporter):
    """Saving to CSV file"""

    def metadata_to_text(self):
        """This writes the metadata to a given csv file"""
        return "# {0}".format(self.dataset.metadata)

    def data_to_text(self):
        """ This writes the data to a given csv file """
        strhandler = StringIO("")
        np.savetxt(strhandler,
                   np.column_stack((self.dataset.x, self.dataset.y)))
        strhandler.seek(0)
        return strhandler.read()
        

class AvivExporter(CSVExporter):
    """ Saving to Aviv file"""

    def metadata_to_text(self):
        """This writes the metadata to a given csv file"""
        text = "data_name something"
        for key in self.dataset.metadata:
            text += "\n_{key}_ {value}".format(
                key=key,
                value=self.dataset.metadata[key]
            )
        text += "\n_data_end_"
        return text

    def data_to_text(self):
        """ This writes the data to a given csv file """
        return "_data_\n" + super(AvivExporter, self).data_to_text()
