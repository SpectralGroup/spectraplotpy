#from dataset import dataset


class Importer(object):
    """The importer class allows you to read data from file."""

    def __init__(self, filename):
        self.dataset = self.load(filename)
        
    def load(self, filename):
        raise Exception('loadd')   
        
   
      
            
            
class AvivImporter(Importer) :
    
     def load(self, filename):
         with open(filename) as f:
             whole_text=f.read()
             #print whole_text.index('_data_')
             data=whole_text[whole_text.index('\n_data_')+7: whole_text.index('\n_data_end_')]
             metadata = 'filename = ' + filename + '\n'
             metadata = metadata + whole_text[0:whole_text.index('\n_data_')] + whole_text[whole_text.index('_data_end_')+10:]
             #print metadata
             
             
             
         
   


   






