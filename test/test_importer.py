# -*- coding: utf-8 -*-
#
# This file is part of spectraplotpy.
#
# spectraplotpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# spectraplotpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with spectraplotpy.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Created on March 17 2014

@author: lbressan

Test for the Importer class
"""
import spectraplotpy as spp
import pytest


def test_AvivImporter():
    """Test for the AvivImporter"""

    filenames = [
                'sampledata/01-CD-Aviv62DS/CSA/CSA.CD',
                'sampledata/01-CD-Aviv62DS/CSA/blank.CD',
                'sampledata/01-CD-Aviv62DS/PEP-average/4RNSX.001',
                ]
    assert spp.Importer(filenames[0])

    for filename in filenames:
        assert spp.AvivImporter(filename)


#def test_baseclass_constructor():
    #with pytest.raises(Exception):
        #spp.Importer('sampledata/01-CD-Aviv62DS/CSA/CSA_corrupted.CD4')


def test_MosImporter():
    """
    Test for the MosImporter.
    
    It verifies that the method MosImporter(filename) works with the 
    selected files:
        sampledata/02-CD-Mos500/blank.bka
        sampledata/02-CD-Mos500/csa.bka
        sampledata/02-CD-Mos500/p07-10tfe.bka
        sampledata/02-CD-Mos500/blank-po7-10tfe.bka
    """
    filename = 'sampledata/02-CD-Mos500/blank.bka'
    assert spp.MosImporter(filename)
    filename = 'sampledata/02-CD-Mos500/csa.bka'
    assert spp.MosImporter(filename)
    filename = 'sampledata/02-CD-Mos500/p07-10tfe.bka'
    assert spp.MosImporter(filename)
    filename = 'sampledata/02-CD-Mos500/blank-po7-10tfe.bka'
    assert spp.MosImporter(filename)







def text_functions():
    filenames = [
                 'sampledata/01-CD-Aviv62DS/PEP-average/4RNSX.010',
                 'sampledata/01-CD-Aviv62DS/CSA/CSA.CD'
                 ]

    for filename in filenames:
        assert spp.take_text(filename)
        assert spp.get_txt_data_metadata(spp.take_text(filename))
        assert spp.get_txt_data_metadata(spp.take_text(filename), filename)
        data_txt, metadata_txt = spp.get_txt_data_metadata(spp.take_text(filename), filename)
        assert spp.parse_metadata(metadata_txt)
        data_txt, metadata_txt = spp.get_txt_data_metadata(spp.take_text(filename))
        #print 'metadata_txt = ', metadata_txt
        assert spp.parse_metadata(metadata_txt) == None
        #print spp.parse_metadata(metadata_txt)





if __name__ == "__main__":
    """Run the test."""
    text_functions()

    test_AvivImporter()

    #test_baseclass_constructor()

    test_MosImporter()

