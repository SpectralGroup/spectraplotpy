#from dataset import dataset
"""The importer class allows you to read data from file."""


class Importer(object):
    """The importer class allows you to read data from file."""

    def __init__(self, filename):
        """Constructor"""
        self.dataset = self.load(filename)

    def load(self, filename):
        """Load method"""
        raise Exception('Cannot load ' + filename + 'in baseclass.')


class AvivImporter(Importer):
    """ Importer of Aviv files
    """

    def load(self, filename):
        """Load method"""
        with open(filename) as inputfile:
            whole_text = inputfile.read()
            #print whole_text.index('_data_')
            start = whole_text.index('\n_data_')+7
            end = whole_text.index('\n_data_end_')
            data = whole_text[start+7:end]
            print len(data)
            metadata = 'filename = ' + filename + '\n'
            metadata = metadata + whole_text[0:start] + whole_text[end+10:]
            #print metadata














