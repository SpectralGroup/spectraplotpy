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
        """Load method"""
        text = self.take_text(filename)
        #print text
        data_txt, metadata_txt = self.get_txt_data_metadata(text, filename)
        #print data_txt
        #print metadata_txt
        self.dataset.metadata = self.parse_metadata(metadata_txt)
        self.set_info(self.dataset.metadata)
        #print self.dataset.metadata
        #print self.dataset.units_x
        #print self.dataset.units_y
        #print self.dataset.dim_x
        #print self.dataset.dim_y
        self.parse_data(data_txt)
        #print self.dataset.x  #[0:3]
        #print self.dataset.y #[0:3]
        #print self.dataset.errors_x
        #print self.dataset.errors_y

    def take_text(self, filename):
        whole_text = None
        with open(filename) as inputfile:
            self.dataset = Dataset()
            whole_text = inputfile.read()
            return whole_text
        ##raise Exception('Cannot load ' + filename + 'in baseclass.')

    def get_txt_data_metadata(self, text, filename=None):
        """Separate data and metadata information form the text file"""
        text = text.split('\n')
        data_txt = [line for line in text if not (line.startswith('_') or re.match('[a-z]',line)) ]
        metadata_txt = 'filename = ' + filename + '\n'
        return data_txt, metadata_txt

    def parse_metadata(self, metadata_txt):
        """Transform metadata from metadata_txt to a dictionary"""
        metadata = dict()
        metadata_txt = metadata_txt.split('\n')
        #print type(metadata_txt)
        #print metadata_txt
        for line in metadata_txt:
            line = line.split()
            #print 0, line,
            if len(line) > 1:
                keyword = line[0]
                value = ' '.join(line[1:])
                metadata[keyword] = value
        return metadata

    ##def get_metadata(self, metadata_txt):
        ##metadata =  self.parse_metadata(metadata_txt)
        ##return metadata

    def set_info(self, metadata_txt):
        return None

    def parse_data(self, data_txt):
        data = np.loadtxt(data_txt)
        self.dataset.x = data[:,0]
        self.dataset.y = data[:,1]
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
        #return self.dataset




class AvivImporter(Importer):
    """ Importer of Aviv files
    """
    def get_txt_data_metadata(self, text, filename):
        """Separate data and metadata information form the text file"""
        metadata_txt = 'filename = ' + filename + '\n'
        start = text.index('\n_data_')+7
        end = text.index('\n_data_end_')
        data_txt = (text[start+7:end]).split('\r\n')

        metadata_txt = 'filename = ' + filename + '\n'
        metadata_txt = metadata_txt + text[0:start] + text[end+10:]
        #print metadata_text
        return data_txt, metadata_txt

    def set_info(self, metadata):
        self.dataset.dim_x = 'wavelength'
        self.dataset.dim_y = metadata['_y_type_']
        self.dataset.units_x = metadata['x_unit']
        self.dataset.units_y = metadata['y_unit']
        #print self.dataset.dim_x, self.dataset.dim_y, self.dataset.units_x, self.dataset.units_y







