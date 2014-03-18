import spectraplotpy as spp


def test_importer() :
#    assert spp.Importer.load(nomefile)
    assert spp.Importer('Data/01-CD-Aviv62DS/CSA/CSA.CD')
    
if __name__ == "__main__":
    test_importer()
    
    
    
    
    