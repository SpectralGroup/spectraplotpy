""" Exporter Program"""

class Exporter(object):
    """ Class Exporter """

    def __init__(self , dataset):
        """ Initialise the dataset"""
        pass

    def __str__(self):
        """ """
        pass
    
    def write(self , filename):
        """"""
        self.filename = filename
        self.write_metadata()
        self.write_data()

    def write_metadata(self):
        """"""
        self.fichier = open(self.filename , 'w')
        self.fichier.write('Test Writing\n')
        
    def write_data(self):
        """ """
        pass
    
    def plot_data(self,dataset):
        """ Plotting Data with Matplotlib"""
        import matplotlib as plt
        plt.plot(dataset)
        plt.show()
        