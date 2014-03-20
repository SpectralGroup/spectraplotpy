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
This uses the *spectraplotpy* library as a format converter
in both expanded and sort syntax
"""

from spectraplotpy import AvivImporter, CSVExporter

def main():
    """Performs the example code"""
    
    filename = '../sampledata/01-CD-Aviv62DS/CSA/CSA.CD'
    avii = AvivImporter(filename)
    csve = CSVExporter(avii.dataset)
    csve.save('csa.csv')

    # Or just

    CSVExporter(AvivImporter(filename).dataset).save('csa1.csv')

if __name__ == '__main__':
    main()
