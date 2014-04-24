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
Created on Wed March 19 22:36:41 2014

@author: lbressan
"""
"""
It plots multiple spectra.
"""
import matplotlib.pyplot as plt

def plot_spectra(*sp_list,  **kwargs):
    """
    Function that takes a list of spectra in input and plots them
    by calling their spectra plot method.
    """
    axes=kwargs.get('axes', plt.gca())   
    for sp in sp_list:
        sp.plot(axes)
        
    return axes    


def average_spectra(sp_list, *args, **kwarg):
    """
    Function that creates an average spectra from a list of spectra.
    It takes as input the list of spectra and returns a new spectrum
    """

    spectrum = sp_list[0]

    for sp in sp_list[1:]:
        spectrum += sp

    spectrum = spectrum / len(sp_list)

    return spectrum
    
