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
import pytest as pt
from collections import OrderedDict



basic_format = \
"""
data_name dh201.cd
_date_  10-18-2013              
"_UNIT X"	"nm" "wavelength"

_start_
185	-31.6863
-47.5356  123
1.1e-5 123
#end
"""

def test_get_txt_data_metadata():
    "test to see if lines are categorized coorectly"
    
    data,metadata = spp.get_txt_data_metadata(basic_format)
    assert data == ['185\t-31.6863', '-47.5356  123', '1.1e-5 123']
    assert metadata == ['data_name dh201.cd', '_date_  10-18-2013', 
                        '"_UNIT X"\t"nm" "wavelength"', '_start_', '#end']
                        
def test_parse_metadata():
    data_lines,metadata_lines = spp.get_txt_data_metadata(basic_format)
    #print spp.parse_metadata(metadata)                   
    assert spp.parse_metadata(metadata_lines) == OrderedDict([
                        ('data_name', 'dh201.cd'), ('_date_', '10-18-2013'), 
                        ('_UNIT X', 'nm wavelength'), ('_start_', True),
                        ('#end', True)])

def test_parse_metadata_empty_lines():
   metadata_lines = ['data_name dh201.cd', '','_date_  10-18-2013']
   #print spp.parse_metadata(metadata_lines)                   
   assert spp.parse_metadata(metadata_lines) == OrderedDict([
                            ('data_name', 'dh201.cd'), ('_date_', '10-18-2013')])
   


def test_AvivImporter_basic():    
    imp = spp.AvivImporter('sampledata/01-CD-Aviv62DS/CSA/CSA-tiny.CD')
    print imp.dataset.x
    print imp.dataset.y
    assert all(imp.dataset.x == [ 320.,   319.5,  319. ])
    assert all(imp.dataset.y == [ 5.396,  6.374,  7.288])
    assert imp.dataset.dim_x == 'wavelength'    
    assert imp.dataset.dim_y == 'millidegrees'
    assert imp.dataset.units_x == 'nanometers'
    assert imp.dataset.units_y == 'millidegrees'
    
    

    

def test_AvivImporter_sample_data():
    """Test for the AvivImporter"""

    filenames = [
                'sampledata/01-CD-Aviv62DS/CSA/CSA.CD',
                'sampledata/01-CD-Aviv62DS/CSA/blank.CD',
                'sampledata/01-CD-Aviv62DS/PEP-average/4RNSX.001',
                ]
    #assert spp.Importer(filenames[0])

    for filename in filenames:
        assert spp.AvivImporter(filename)


#def test_baseclass_constructor():
#    with pt.raises(Exception):
#        spp.Importer('sampledata/01-CD-Aviv62DS/CSA/CSA_corrupted.CD4')


#def test_MosImporter():
#    """
#    Test for the MosImporter.
#    
#    It verifies that the method MosImporter(filename) works with the 
#    selected files:
#        sampledata/02-CD-Mos500/blank.bka
#        sampledata/02-CD-Mos500/csa.bka
#        sampledata/02-CD-Mos500/p07-10tfe.bka
#        sampledata/02-CD-Mos500/blank-po7-10tfe.bka
#    """
#    filename = 'sampledata/02-CD-Mos500/blank.bka'
#    assert spp.MosImporter(filename)
#    filename = 'sampledata/02-CD-Mos500/csa.bka'
#    assert spp.MosImporter(filename)
#    filename = 'sampledata/02-CD-Mos500/p07-10tfe.bka'
#    assert spp.MosImporter(filename)
#    filename = 'sampledata/02-CD-Mos500/blank-po7-10tfe.bka'
#    assert spp.MosImporter(filename)
#
#
#
#def text_exception():
#    filename = 'sampledata/01-CD-Aviv62DS/CSA/CSA_1c.CD'
#    with pt.raises(Exception):
#        imp = spp.Importer(filename)



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
        print 'metadata_txt = ', metadata_txt
        assert spp.parse_metadata(metadata_txt) == None
        print spp.parse_metadata(metadata_txt)





if __name__ == "__main__":
    """Run the test."""
    #est_get_txt_data_metadata()
    #test_parse_metadata()
    #test_parse_metadata_empty_lines()
    test_AvivImporter_basic()