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

The importer class.

It is used to read data from a file and
store the data and metadata in a dataset.
"""
from  spectraplotpy.dataset import Dataset
import numpy as np
import re
from StringIO import StringIO
import shlex
from collections import OrderedDict

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
    

    if filename is not None:
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


def take_text(filename):
    """
    Read the file and return the text as a string.
    """
    whole_text = None
    with open(filename) as inputfile:
        whole_text = inputfile.read()
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
        text = take_text(filename)
        data_txt, metadata_txt = self.get_txt_data_metadata(text, filename)
        self.dataset.metadata = self.parse_metadata(metadata_txt)
        self.set_info(self.dataset.metadata)
        self.parse_data(data_txt)

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


    def parse_metadata(self, metadata_txt):
        """
        Return the metadata information as a dictionary.
        """
        return  parse_metadata(metadata_txt)


    def set_info(self, metadata):
        """
        Defines the particular informations needed for a dataset.

        It can be overridden by subclass methods.
        """
        pass


    def parse_data(self, data_txt):
        """
        Parse the text containing the data and store the x, y and errors
        in the dataset attributes.
        """
        data = np.loadtxt(StringIO("\n".join(data_txt)))
        if len(data.shape) < 2:
            raise Exception('Invalid data shape. Expecting at least two columns\
            but recived only one.')
        else:
            self.dataset.x = data[:, 0]
            self.dataset.y = data[:, 1]
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
    def get_txt_data_metadata(self, text, filename=None):
        """
        Separate data and metadata information form the text file.

        The data follows the marker `"_DATA"`.
        """
        start = text.index('"_DATA"')

        data_txt = (text[start + 7:]).split('\r\n')
        metadata_txt = 'filename ' + filename + '\n'
        metadata_txt = metadata_txt + text[0:start]
        return data_txt, metadata_txt


    def set_info(self, metadata):
        """
        Defines the particular informations needed for a dataset.

        It stores dimensions and units in the dataset attributes.
        """
        self.dataset.units_x = metadata['"_UNITX"']
        self.dataset.errors_x = metadata['"_DELTAX"']
        #print [key for key in metadata.keys() if key.startswith('"_UNITY"')]
        try:
            self.dataset.units_y = metadata['"_UNITY"']
        except:
            self.dataset.units_y = list()
            for key in metadata:
                if key.startswith('"_UNITY'):
                    self.dataset.units_y.append(metadata[key])
