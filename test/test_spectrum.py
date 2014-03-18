import spectraplotpy as spp
import numpy as np

def test_construction():
    ds = [1,2,3,4]   
    s = spp.Spectrum(ds)
    assert s

def test_copy():
    ds = [1,2,3,4]
    s = spp.Spectrum(ds)
    s1 = s.copy()
    
    snp = np.array(ds)
    snp1 = snp.copy()
    
    assert s1 == snp1 
#    assert s1 == s
    
#def test_add():
#    ds = [1,2,3,4]
#    s = spp.Spectrum(ds) 
#    s1 = s.copy()
#    s2 = s.add(s1)
#    
#    snp = np.array(ds)
#    snp1 = snp.copy()
#    snp2 = snp + snp1
#    
#    assert s == snp
#    assert s1 == snp1
#    assert s2 == snp2
    