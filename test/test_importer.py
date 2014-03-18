"""Test for the Importer class"""
import spectraplotpy as spp
#import pytest


def test_AvivImporter():
    """Test for the AvivImporter"""
    assert spp.AvivImporter('Data/01-CD-Aviv62DS/CSA/CSA.CD')
    #assert spp.AvivImporter('Data/01-CD-Aviv62DS/CSA/blank.CD')
    #assert spp.AvivImporter('Data/01-CD-Aviv62DS/PEP-average/4RNSX.001')

    #print spp.Importer('Data/01-CD-Aviv62DS/PEP-average/4RNSX.001')


#def test_baseclass_constructor():
    #with pytest.raises(Exception):
        #spp.Importer('Data/01-CD-Aviv62DS/PEP-average/4RNSX.001')


if __name__ == "__main__":
    """Run the test."""
    test_AvivImporter()




