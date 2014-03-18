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
    
    def plot_data(self, plotype=None):
        """ Plotting Data with Matplotlib
            with arguments
            lineair
            semilogy
            semilogx
            loglog
            """

        import matplotlib.pyplot as plt
        
        if plotype == 'linear':
            plt.plot(self.dataset.x, self.dataset.y)
            plt.title('Linear')
            
        if plotype == 'semilogy':
            plt.semilogy(self.dataset.x, self.dataset.y)
            plt.title('Semilogy')            
            plt.grid(True)
            
        if plotype == 'semilogx':
            plt.semilogx(self.dataset.x, self.dataset.y)
            plt.title('Semilogx')
            plt.grid(True)
            
        if plotype == 'loglog':
            plt.loglog(self.dataset.x, self.dataset.y)
            plt.title('loglog')
            plt.grid(True)
            
        plt.show()
        