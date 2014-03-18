#from dataset import dataset


class Importer(object):
    """The importer class allows you to read data from file."""
    #self.dataset = Dataset()
    
    def __init__(self, filename):
        self.dataset = None
        with open(filename) as f:
            whole_text=f.read()
            print whole_text
#        pass
#        return dataset
    






