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

The importer class.

It is used to read data from a file and
store the data and metadata in a dataset.
"""
from spectraplotpy.dataset import Dataset
import numpy as np
import re
from StringIO import StringIO
import shlex
from collections import OrderedDict
import string

def get_txt_data_metadata(text, filename=None):
    """
    Function that takes a text (as a single string)
    and returns the text containing the metadata (as a list of strings)
    and the data (as a list of strings).

    It identifies every lines starting with a number as data and the rest
    as metadata. Examples of valid numbers
        123
        123.321
        12.23e5
        -123
        .23
        +123
    """

    data_lines = []
    meta_lines = []
    #matches any line that starts with a number.
    number_re = re.compile('\A[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?')
    for line in text.splitlines():
        sline = line.strip()
        if sline == "": continue

        if re.match(number_re, sline):
            data_lines.append(sline)
        else:
            meta_lines.append(sline)


    if (filename is not None) and isinstance(filename , str):
        meta_lines.append('filename ' + filename)

    return data_lines, meta_lines


def parse_metadata(meta_lines):
    """
    Function that returns a dictionary of the metadata
    from the meta_lines as a list of strings.

    Quotes are handled correctly.
    Valid examples:
      - key = value
      - key value
      - "long key" = "long value"
      - "long key" "long value"
    """
    metadata = OrderedDict()
    for line in meta_lines:
        sline = line.strip()
        if sline == "": continue

        # split on whitespace, but preserve quoted strings
        p = shlex.split(sline)
        #filter for lone =
        p = filter(lambda l: l != '=', p)

        key = p[0]

        if len(p) > 1:
            metadata[key] = ' '.join(p[1:])
        else:
            # just mark the presence of a flag
            metadata[key] = True

    return metadata


def take_text(filename_or_fdesc):
    """
    Read the file or a file descriptor and return the text as a string.
    """

    whole_text = None
    #TODO the isnstance comaprison mises unicode strings in python 2.7
    #should use six.str_types?
    if isinstance(filename_or_fdesc, str):
        with open(filename_or_fdesc) as inputfile:
            whole_text = inputfile.read()
    else:
        whole_text = filename_or_fdesc.read()

    return whole_text


class Importer(object):
    """
    The importer class allows you to read data from file
    and store the data into a dataset instance.
    """
    def __init__(self, filename):
        """
        Constructor: it calls the load function.
        """
        self.dataset = self.load(filename)
        self.parsed_data = []


    def load(self, filename):
        """
        The load method takes a filename and stores all the information
        into the dataset.

        It performs the following steps:
         - read the text file as a string (see take_text);
         - separate the metadata and the data lines
            (see get_txt_data_metadata);
         - store the metadata information in the dataset.metadata dictionary
            (see parse_metadata);
         - store the needed information (as for example units, dimensions, ...)
            of the data in the dataset.metadata instance (see set_info);
         - store the data into the x, y, errors_x, errors_y of the dataset
            (see parse_data).
        """
        self.dataset = Dataset()
        self.datasets = [self.dataset]
        text = take_text(filename)
        data_lines, metadata_lines = self.get_txt_data_metadata(text, filename)

        self.dataset.metadata = self.parse_metadata(metadata_lines)
        self.set_info(self.dataset.metadata)
        self.parse_data(data_lines)

#        print self.dataset.metadata
#        print self.dataset.dim_x, self.dataset.dim_y, \
#              self.dataset.units_x, self.dataset.units_y
#        print len(self.dataset.x)
        return self.dataset


    def get_txt_data_metadata(self, text, filename=None):
        """
        Separate the data and metadata part from the text file (string).

        It depends on the file format, it should be overriden for each specific
        importer subclass.
        """
        return get_txt_data_metadata(text, filename)


    def parse_metadata(self, metadata_lines):
        """
        Return the metadata information as a dictionary.
        """
        return  parse_metadata(metadata_lines)


    def set_info(self, metadata):
        """
        Defines the particular informations needed for a dataset.

        It can be overridden by subclass methods.
        """
        pass


    def parse_data(self, data_lines):
        """
        Parse the text containing the data and store the x, y and errors
        in the dataset attributes.
        """
        self.parsed_data = np.loadtxt(StringIO("\n".join(data_lines)))
        #TODO: test this further
        if self.parsed_data.shape[1] < 2:
            raise Exception('Invalid data shape. Expecting at least two columns\
            but recived only one.')
        else:
            self.dataset.x = self.parsed_data[:, 0]
            self.dataset.y = self.parsed_data[:, 1]
#            if data.shape[1] > 2:
#                if data.shape[1] == 3:
#                    self.dataset.errors_y = data[:, 2]
#                if data.shape[1] == 4:
#                    self.dataset.errors_x = data[:, 2]
#                    self.dataset.errors_y = data[:, 3]



class AvivImporter(Importer):
    """
    Importer of Aviv files.
    """

    def set_info(self, metadata):
        """
        Defines the particular informations needed for a dataset.

        It stores dimensions and units in the dataset attributes.
        """
        self.dataset.dim_x = 'wavelength'
        self.dataset.dim_y = metadata['_y_type_']
        self.dataset.units_x = metadata['x_unit']
        self.dataset.units_y = metadata['y_unit']


class MosImporter(Importer):
    """
    Importer of Mos500 files.
    """
    def ascii_type(self):
        """
        Returns the type of biokine ascii file. Can be either multi or
        simple. If None should an exception be raised?

        The type is determined by the first line
        """
        result = None
        if self.dataset.metadata.get('BIO-KINE ASCII FILE', False):
            result = 'simple'
        if self.dataset.metadata.get('BIO-KINE MULTI-Y ASCII FILE', False):
            result = 'multi'
        return result

    def set_info_simple(self, metadata):
        self.dataset.units_x = metadata['_UNITX']
        self.dataset.units_y = metadata['_UNITY']
        self.dataset.dim_x = 'wavelength'

    def set_info_multi(self, metadata):
        """
        Sets the information and creates the datasets in case there are multiple
        datasets.
        """
        num_sets = int(metadata['_NBY'])
        # create additional datasets. The first one is allready created
        if num_sets > 1:
            for n in range(1,num_sets):
                self.datasets.append(Dataset())

        # iterate over datasets and set metadata
        for n in range(num_sets):
            self.datasets[n].dim_x = 'wavelength'
            self.datasets[n].units_x = metadata['_UNITX']
            self.datasets[n].units_y = metadata['_UNITY'+str(n+1)]

    def set_info(self, metadata):
        """
        Defines the particular informations needed for a dataset.

        It stores dimensions and units in the dataset attributes.
        """
        if self.ascii_type() == 'simple':
            self.set_info_simple(metadata)

        if self.ascii_type() == 'multi':
            self.set_info_multi(metadata)

    def parse_data(self, data_lines):
        super(MosImporter, self).parse_data(data_lines)

        #assign other datasets as well
        if self.ascii_type() == 'multi':
            for n in range(1, len(self.datasets)):
                self.datasets[n].x = self.parsed_data[:, 0]
                self.datasets[n].y = self.parsed_data[:, n+1]


class CSVImporter(Importer):
    """ Importer of various CSV files and similar formats. """

    def __init__(self, filename, csv_type = "XYYY"):
        """
        Constructor: it calls the load function.
        """
        self.csv_type = csv_type
        self.dataset = self.load(filename)
        self.parsed_data = []

    def create_datasets_XYYY(self):
        num_sets =  self.parsed_data.shape[1] - 1
        for n in range(1, num_sets):
            ds = Dataset()
            ds.x = self.parsed_data[:, 0]
            ds.y = self.parsed_data[:, n+1]
            self.datasets.append(ds)

    def create_datasets_XYXY(self):
        #Todo: check for correct dimensions        
        num_sets =  self.parsed_data.shape[1]/2 
        for n in range(1, num_sets):
            ds = Dataset()
            ds.x = self.parsed_data[:, 2*n]
            ds.y = self.parsed_data[:, 2*n+1]
            self.datasets.append(ds)                    

    def parse_data(self, data_lines):
        # translate separators to whitespace so that it will be loaded correctly.
        # this is very hacky... Better would be to pass a delimiter to parse_data.
        # Should really implement kwargs passing.
        trans_table = string.maketrans(";,", "  ")
        data_lines = map(lambda l: l.translate(trans_table), data_lines)

        super(CSVImporter, self).parse_data(data_lines)

        # if there are more than two columns
        if self.parsed_data.shape[1] > 2:
            if self.csv_type == "XYYY":
                self.create_datasets_XYYY()
            if self.csv_type == "XYXY":
                self.create_datasets_XYXY()                




