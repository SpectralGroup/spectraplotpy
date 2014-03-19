"""Test for the Importer class"""
import spectraplotpy as spp
#import pytest


def test_AvivImporter():
    """Test for the AvivImporter"""

    filenames= [
                'sampledata/01-CD-Aviv62DS/CSA/CSA.CD',
                'sampledata/01-CD-Aviv62DS/CSA/CSA.CD',
                'sampledata/01-CD-Aviv62DS/CSA/blank.CD',
                'sampledata/01-CD-Aviv62DS/PEP-average/4RNSX.001',
                ]
    assert spp.Importer(filenames[0])

    for filename in filenames:
        assert spp.AvivImporter(filename)


#def test_baseclass_constructor():
    #with pytest.raises(Exception):
        #spp.Importer('sampledata/01-CD-Aviv62DS/PEP-average/4RNSX.001')


def test_MosImporter():
    """
    Test for the MosImporter
    """
    filename = 'sampledata/02-CD-Mos500/blank.bka'
    assert spp.MosImporter(filename)
    filename = 'sampledata/02-CD-Mos500/csa.bka'
    assert spp.MosImporter(filename)
    filename = 'sampledata/02-CD-Mos500/p07-10tfe.bka'
    assert spp.MosImporter(filename)
    filename = 'sampledata/02-CD-Mos500/blank-po7-10tfe.bka'
    assert spp.MosImporter(filename)















def text_functions(filename):
    #assert take_text()
    assert spp.take_text(filename)
    assert spp.get_txt_data_metadata(spp.take_text(filename))
    assert spp.get_txt_data_metadata(spp.take_text(filename), filename)
    data_txt, metadata_txt = spp.get_txt_data_metadata(spp.take_text(filename), filename)
    data_txt, metadata_txt = spp.get_txt_data_metadata(spp.take_text(filename))
    #print metadata_txt
    assert spp.parse_metadata(metadata_txt)
    print spp.parse_metadata(metadata_txt)



if __name__ == "__main__":
    """Run the test."""

    filename = 'sampledata/01-CD-Aviv62DS/CSA/CSA.CD'
    text_functions(filename)
    filename = 'sampledata/01-CD-Aviv62DS/PEP-average/4RNSX.010'
    text_functions(filename)

    test_AvivImporter()

    test_baseclass_constructor()

    test_MosImporter()





