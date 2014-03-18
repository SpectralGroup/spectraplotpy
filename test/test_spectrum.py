import spectraplotpy as spp
import numpy as np

def test_construction():
    ds = spp.Dataset()
    assert spp.Spectrum(ds)

def test_copy():
    ds = spp.Dataset()
    s = spp.Spectrum(ds)
#    s.dataset.x = [1,2,3,4]
    s1 = s.copy()
    assert s.dataset.x == s1.dataset.x
    assert s.dataset.y == s1.dataset.y
#    assert s == s1
    
#def test_add():
#    ds = spp.Dataset()
#    s = spp.Spectrum(ds)
#    s.dataset.y = np.array([1,2,3,4])
#    s1 = s.copy()
#    
#    snp = np.array([1,2,3,4])
#    snp1 = snp.copy()
##    snp2 = snp + snp1
#    
#    assert all(s.dataset.y == snp)
#    assert all(s1.dataset.y == snp1)
##    assert all(s2.dataset.x == snp2)
    