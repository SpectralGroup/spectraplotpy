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

@author: lbressan, ajasja

Test for the Importer class
"""
import spectraplotpy as spp
#import pytest as pt
from collections import OrderedDict
from StringIO import StringIO



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

def test_take_text_file_descriptor():
    whole_text = spp.take_text(StringIO(basic_format))
    assert whole_text == basic_format

basic_aviv = """\
data_name csa.cd
_n_points  3
x_unit nanometers
y_unit millidegrees
_y_type_   millidegrees
_data_
320.00 5.396
319.50 6.374
319.00 7.288
_data_end_
"""

def test_take_text_filer():
    whole_text = spp.take_text('sampledata/01-CD-Aviv62DS/CSA/CSA-tiny.CD')
    assert whole_text == basic_aviv

def test_AvivImporter_basic():
    imp = spp.AvivImporter('sampledata/01-CD-Aviv62DS/CSA/CSA-tiny.CD')
    #print imp.dataset.x
    #print imp.dataset.y
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

    for filename in filenames:
        #TODO test that the data is in fact correctly loaded
        assert spp.AvivImporter(filename)

mos_basic="""\
"BIO-KINE ASCII FILE"
"_UNITX"	"nm"
"_UNITY"	""
"_DELTAX"	0
"_DATA"
185	-6.36455
186	-5.60259
187	-4.94525
"""

#def test_baseclass_constructor():
#    with pt.raises(Exception):
#        spp.Importer('sampledata/01-CD-Aviv62DS/CSA/CSA_corrupted.CD4')

def test_MosImporter_basic():
    imp = spp.MosImporter(StringIO(mos_basic))
    #print imp

    assert imp.ascii_type() == 'simple'
    assert all(imp.dataset.x == [ 185.,  186.,  187.])
    assert all(imp.dataset.y == [-6.36455, -5.60259, -4.94525])
    assert imp.dataset.dim_x == 'wavelength'
    #assert imp.dataset.dim_y == 'millidegrees'
    assert imp.dataset.units_x == 'nm'
    assert imp.dataset.units_y == ''


mos_multiline="""\
"BIO-KINE MULTI-Y ASCII FILE"
"_UNITX"	"nm"
"_NBY"	3
"_COMMENT1"  "First comment"
"_COMMENT1"  "some more first comment"
"_UNITY1"	"MilliDegree"
"_UNITY2"	"AU"
"_UNITY3"	"Volt"
"_DATA"
185	-31.6863	1.34487 	687
186	-47.5356	1.32574 	608
187	-61.078 	1.29144 	549
"""

def check_first_multiline_dataset(dataset):
    assert all(dataset.x == [ 185.,  186.,  187.])
    assert all(dataset.y == [-31.6863, -47.5356, -61.078])
    assert dataset.dim_x == 'wavelength'
    assert dataset.units_x == 'nm'
    assert dataset.units_y == 'MilliDegree'

def check_second_multiline_dataset(dataset):
    assert all(dataset.x == [ 185.,  186.,  187.])
    assert all(dataset.y == [1.34487, 1.32574, 1.29144])
    assert dataset.dim_x == 'wavelength'
    assert dataset.units_x == 'nm'
    assert dataset.units_y == 'AU'

def check_third_multiline_dataset(dataset):
    assert all(dataset.x == [ 185.,  186.,  187.])
    assert all(dataset.y == [ 687.,  608.,  549.])
    assert dataset.dim_x == 'wavelength'
    assert dataset.units_x == 'nm'
    assert dataset.units_y == 'Volt'


def test_MosImporter_mutiline():
    imp = spp.MosImporter(StringIO(mos_multiline))
    assert imp.ascii_type() == 'multi'

    #has three datasets
    assert len(imp.datasets) == 3

    check_first_multiline_dataset(imp.dataset)
    check_first_multiline_dataset(imp.datasets[0])
    check_second_multiline_dataset(imp.datasets[1])
    check_third_multiline_dataset(imp.datasets[2])
    print imp

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
##
#
#
#def text_exception():
#    filename = 'sampledata/01-CD-Aviv62DS/CSA/CSA_1c.CD'
#    with pt.raises(Exception):
#        imp = spp.Importer(filename)

csv_basic = """\
nm, A
320.000000, 0.402335
319.000000, 0.402692
318.000000, 0.402974
"""


def test_CSVImporter_basic():
    imp = spp.CSVImporter(StringIO(csv_basic))
    assert all(imp.dataset.x == [320.,  319.,  318.])
    assert all(imp.dataset.y == [0.402335, 0.402692, 0.402974])
    #assert imp.dataset.dim_x == 'wavelength'
    #assert imp.dataset.dim_y == 'millidegrees'
    #assert imp.dataset.units_x == 'nm'
    #assert imp.dataset.units_y == ''


csv_multicol_XYYY = """\
;FL Blank.Sample.Raw.sp;FL p07 v oc po cent.Sample.Raw.sp
Wavelength [nm];Absorbance; Absorbance
230;0.68722;4.6999
231;0.64781;4.7001
"""
def test_CSVImporter_multicol_XYYY():
    imp = spp.CSVImporter(StringIO(csv_multicol_XYYY), csv_type="XYYY")

    def check_first(ds):
        assert all(ds.x == [230.,  231.])
        assert all(ds.y == [0.68722, 0.64781])

    def check_second(ds):
        assert all(ds.x == [230.,  231.])
        assert all(ds.y == [4.6999, 4.7001])

    assert len(imp.datasets) == 2
    check_first(imp.dataset)
    check_first(imp.datasets[0])

    check_second(imp.datasets[1])

csv_multicol_XYXY = """\
;;FL Blank.Sample.Raw.sp;;FL p07 v oc po cent.Sample.Raw.sp
Wavelength [nm];Absorbance; Absorbance
230;0.68722;236;4.6999
231;0.64781;237;4.7001
"""
def test_CSVImporter_multicol_XYXY():
    imp = spp.CSVImporter(StringIO(csv_multicol_XYXY), csv_type="XYXY")

    def check_first(ds):
        assert all(ds.x == [230.,  231.])
        assert all(ds.y == [0.68722, 0.64781])

    def check_second(ds):
        assert all(ds.x == [236.,  237.])
        assert all(ds.y == [4.6999, 4.7001])

    assert len(imp.datasets) == 2
    check_first(imp.dataset)
    check_first(imp.datasets[0])

    check_second(imp.datasets[1])

if __name__ == "__main__":
    """Run selected tests."""
    test_CSVImporter_multicol_XYYY()