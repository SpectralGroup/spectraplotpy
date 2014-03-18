import spectraplotpy as spp

def test_construction():
    ds = [1,2,3,4]   
    s = spp.Spectrum(ds)
    assert s
      