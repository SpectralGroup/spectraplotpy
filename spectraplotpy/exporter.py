""" 
Exporter classes : Exporting data to file

Class BaseTextExporter is used as a template for exporting data to 
differents file

Class CSVExporter export Metada and Data to csv file

Class AvivExporter export Metada and Data to aviv file

Class GraphicExporter export Metada and Data to png file

"""

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


class CSVExporter(BaseTextExporter):
    """Saving to CSV file"""

    def metadata_to_text(self):
        """This writes the metadata to a given csv file"""
        return "# {0}".format(self.dataset.metadata)

    def data_to_text(self):
        """ This writes the data to a given csv file """
        strhandler = StringIO("")
        stack = np.column_stack((self.dataset.x, self.dataset.y))

        if self.dataset.errors_y is not None:

            if self.dataset.errors_x is not None:
                try:
                    np.column_stack((stack, self.dataset.errors_x))
                except ValueError:
                    error = self.dataset.errors_x * np.ones_like(self.dataset.x)
                    np.column_stack((stack, error))

            try:
                np.column_stack((stack, self.dataset.errors_y))
            except ValueError:
                error = self.dataset.error_y * np.ones_like(self.dataset.y)
                np.column_stack((stack, error))

        np.savetxt(strhandler, stack)
        strhandler.seek(0)
        return strhandler.read()
        

class AvivExporter(CSVExporter):
    """ Saving to Aviv file"""

    def metadata_to_text(self):
        """This writes the metadata to a given aviv file"""
        text = "data_name something"
        for key in self.dataset.metadata:
            text += "\n_{key}_ {value}".format(
                key=key,
                value=self.dataset.metadata[key]
            )
        return text

    def data_to_text(self):
        """ This writes the data to a given csv file """
        return "_data_\n" + \
               super(AvivExporter, self).data_to_text() + \
               "\n_data_end"
               
class BaseGraphicExporter(Exporter):
    """ Export Plot To PNG file from matplolib"""   
        
    def plot(self, axis, *args, **kwargs):
        """ Ploting Data """
        return axis.plot(self.dataset.x, self.dataset.y, *args, **kwargs)
 