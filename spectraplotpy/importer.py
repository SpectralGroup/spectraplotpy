"""The importer class allows you to read data from file."""
from  spectraplotpy.dataset import Dataset
import numpy as np
import re

class Importer(object):
    """The importer class allows you to read data from file."""

    def __init__(self, filename):
        """Constructor"""
        self.dataset = self.load(filename)


    def load(self, filename):
        """
        Load method
        """
        text = self.take_text(filename)

        data_txt, metadata_txt = self.get_txt_data_metadata(text, filename)
        self.dataset.metadata = self.parse_metadata(metadata_txt)
        self.set_info(self.dataset.metadata)
        self.parse_data(data_txt)


    def take_text(self, filename):
        """
        Read the file and return the text.
        """

        whole_text = None
        with open(filename) as inputfile:
            self.dataset = Dataset()
            whole_text = inputfile.read()
            return whole_text


    def get_txt_data_metadata(self, text, filename=None):
        """Separate data and metadata information form the text file"""
        text = text.split('\n')
        data_txt = [line for line in text
                         if not (line.startswith('_')
                            or re.match('[a-z]', line))]
        metadata_txt = 'filename = ' + filename + '\n'
        return data_txt, metadata_txt


    def parse_metadata(self, metadata_txt):
        """
        Transform metadata from metadata_txt to a dictionary
        """
        metadata = dict()
        metadata_txt = metadata_txt.split('\n')
        for line in metadata_txt:
            line = line.split()
            #print 0, line,
            if len(line) > 1:
                keyword = line[0]
                value = ' '.join(line[1:])
                metadata[keyword] = value
        return metadata


    def set_info(self, metadata):
        """
        Defines units and dimensions of the dataset.
        """
        pass


    def parse_data(self, data_txt):
        """
        Parse the text containing the data
        """
        data = np.loadtxt(data_txt)
        self.dataset.x = data[:, 0]
        self.dataset.y = data[:, 1]
        if data.shape[1] < 2:
            raise Exception('Invalid data')
        elif data.shape[1] >= 2:
            self.dataset.x = data[:, 0]
            self.dataset.y = data[:, 1]
            if data.shape[1] > 2:
                if data.shape[1] == 3:
                    self.dataset.errors_y = data[:, 2]
                if data.shape[1] == 4:
                    self.dataset.errors_x = data[:, 2]
                    self.dataset.errors_y = data[:, 3]



class AvivImporter(Importer):
    """
    Importer of Aviv files
    """
    def get_txt_data_metadata(self, text, filename=None):
        """Separate data and metadata information form the text file"""
        metadata_txt = 'filename = ' + filename + '\n'
        start = text.index('\n_data_') + 7
        end = text.index('\n_data_end_')
        data_txt = (text[start + 7:end]).split('\r\n')

        metadata_txt = 'filename = ' + filename + '\n'
        metadata_txt = metadata_txt + text[0:start] + text[end + 10:]
        return data_txt, metadata_txt

    def set_info(self, metadata):
        self.dataset.dim_x = 'wavelength'
        self.dataset.dim_y = metadata['_y_type_']
        self.dataset.units_x = metadata['x_unit']
        self.dataset.units_y = metadata['y_unit']







