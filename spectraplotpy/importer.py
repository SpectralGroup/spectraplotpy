"""The importer class allows you to read data from file."""
from  spectraplotpy.dataset import Dataset
import numpy as np

class Importer(object):
    """The importer class allows you to read data from file."""

    def __init__(self, filename):
        """Constructor"""
        self.dataset = self.load(filename)

    def load(self, filename):
        """Load method"""
        raise Exception('Cannot load ' + filename + 'in baseclass.')

    def make_dict_metadata(self, text):
        """Method to put metadata in a dictionary"""
        metadata = dict()
        text = text.split('\n')
        #print type(text)
        #print text
        for line in text:
            line = line.split()
            #print 0, line,
            if len(line) > 1:
                keyword = line[0]
                value = ' '.join(line[1:])
                metadata[keyword] = value
        return metadata




class AvivImporter(Importer):
    """ Importer of Aviv files
    """

    def load(self, filename):
        """Load method"""
        with open(filename) as inputfile:
            self.dataset = Dataset()
            whole_text = inputfile.read()
            #print whole_text.index('_data_')
            start = whole_text.index('\n_data_')+7
            end = whole_text.index('\n_data_end_')
            data = (whole_text[start+7:end]).split('\r\n')
            #print len(data)
            #print data

            metadata_text = 'filename = ' + filename + '\n'
            metadata_text = metadata_text + whole_text[0:start] + whole_text[end+10:]
            #print metadata_text

            self.dataset.metadata = self.make_dict_metadata(metadata_text)
            #print self.dataset.metadata
            self.dataset.dim_x = 'wavelength'
            self.dataset.dim_y = self.dataset.metadata['_y_type_']
            self.dataset.units_x = self.dataset.metadata['x_unit']
            self.dataset.units_y = self.dataset.metadata['y_unit']

            lista = [map(float, linea.split()) for linea in  data]
            data_array = np.array(lista)
            #print array
            #print len(data_array), data_array.shape

            self.dataset.ndat = len(data_array)

            if int(self.dataset.metadata['_n_points']) != len(data_array):
                print self.dataset.metadata['_n_points'], len(data_array), self.dataset.metadata['_n_points'] == len(data_array)

                raise Exception('Wrong number of data loaded')

            if self.dataset.ndat < 2:
                raise Exception('Invalid data')
            elif self.dataset.ndat >= 2:
                self.dataset.x = data_array[:, 0]
                self.dataset.y = data_array[:, 1]
                if self.dataset.ndat > 2:
                    if self.dataset.ndat == 3:
                        self.dataset.errors_y = data_array[:, 2]
                    if self.dataset.ndat == 4:
                        self.dataset.errors_x = data_array[:, 2]
                        self.dataset.errors_y = data_array[:, 3]



