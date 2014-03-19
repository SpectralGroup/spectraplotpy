"""Test for the Importer class"""
import spectraplotpy as spp
#import pytest


def test_AvivImporter():
    """Test for the AvivImporter"""
    assert spp.AvivImporter('sampledata/01-CD-Aviv62DS/CSA/CSA.CD')
    assert spp.Importer('sampledata/01-CD-Aviv62DS/CSA/CSA.CD')
    #assert spp.AvivImporter('Data/01-CD-Aviv62DS/CSA/blank.CD')
    #assert spp.AvivImporter('Data/01-CD-Aviv62DS/PEP-average/4RNSX.001')

    #print spp.Importer('Data/01-CD-Aviv62DS/PEP-average/4RNSX.001')


#def test_baseclass_constructor():
    #with pytest.raises(Exception):
        #spp.Importer('Data/01-CD-Aviv62DS/PEP-average/4RNSX.001')








def text_functions():
    filename = 'sampledata/01-CD-Aviv62DS/CSA/CSA.CD'
    #assert take_text()
    assert take_text(filename)
    assert get_txt_data_metadata(take_text(filename))
    assert get_txt_data_metadata(take_text(filename), filename)
    data_txt, metadata_txt = get_txt_data_metadata(take_text(filename), filename)
    assert parse_metadata(metadata_txt)



if __name__ == "__main__":
    """Run the test."""
    test_AvivImporter()
    text_functions()



