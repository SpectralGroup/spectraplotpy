# -*- coding: utf-8 -*-

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
