""" Exporter Program"""

class Exporter(object):
    """ Class Exporter """

    def __init__(self, dataset):
        self.dataset = dataset
        self.filename = ""

    def __str__(self):
        pass
    
    def write(self , filename):
        """This function writest the content of the dataset to a file"""
        self.filename = filename
        self.write_metadata()
        self.write_data()

    def write_metadata(self):
        """This writes the metadata to a given file"""
        foutput = open(self.filename , 'w')
        foutput.write('Test Writing\n')
        
    def write_data(self):
        """ This writes the data to a given file """
        pass
    
    def plot_data(self):
        """ Plotting Data with Matplotlib"""
        import matplotlib.pyplot as plt
        plt.plot(self.dataset.x, self.dataset.y)
        plt.show()
        