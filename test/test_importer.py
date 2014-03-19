"""Test for the Importer class"""
import spectraplotpy as spp
#import pytest


def test_AvivImporter():
    """Test for the AvivImporter"""
    assert spp.AvivImporter('sampledata/01-CD-Aviv62DS/CSA/CSA.CD')
    assert spp.Importer('sampledata/01-CD-Aviv62DS/CSA/CSA.CD')


def text_functions(filename):
    """Test the special functions"""
    assert spp.take_text(filename)
    assert spp.get_txt_data_metadata(spp.take_text(filename))
    assert spp.get_txt_data_metadata(spp.take_text(filename), filename)

    data_txt, metadata_txt = spp.get_txt_data_metadata(
        spp.take_text(filename),
        filename)

    assert spp.parse_metadata(metadata_txt)
    print spp.parse_metadata(metadata_txt)
