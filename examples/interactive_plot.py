# -*- coding: utf-8 -*-

"""
This uses the *spectraplotpy* library for easy ploting
"""

from spectraplotpy import AvivImporter
from spectraplotpy import BasePlotExporter
from spectraplotpy import Spectrum

import matplotlib.pyplot as plt

def main():
    """Performs the example code"""
    
    filename = '../sampledata/01-CD-Aviv62DS/CSA/CSA.CD'
    avii = AvivImporter(filename)
    spec = Spectrum(avii.dataset)
    spec.plot(plt, '--ob')
    plt.show()

    # Or just

    Spectrum(AvivImporter(filename).dataset).plot(plt, '--ob')
    # And for example
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
