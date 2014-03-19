import spectraplotpy as spp
import numpy as np

def create_fake_dataset():
    ds = spp.Dataset()
    ds.x = np.array([1,2,3,4])
    ds.y = np.array([2,4,6,8])
    return ds 

def test_construction():
    ds = spp.Dataset()
    assert spp.Spectrum(ds)

def test_copy():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds) 
    s1 = s.copy()
    
    assert all(s.dataset.x == s1.dataset.x)
    assert all(s.dataset.y == s1.dataset.y)
    
    s1.dataset.x[2] = 100
    assert not all(s.dataset.x == s1.dataset.x)
    
    
def test_add():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    s2 = s + s1
    s.add(s1)
    
    assert all(s.dataset.x == s2.dataset.x)
    assert all(s.dataset.y == s2.dataset.y)

def test_add_value():
    s_y_np = np.array([2,4,6,8])
    s_y_np1 = s_y_np.copy()
    s_y_np2 = s_y_np + s_y_np1
    
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    
    assert all(s.dataset.y == s_y_np)
    
    s.add(s1)
    
    assert all(s.dataset.y == s_y_np2)
    
def test_sub():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    s2 = s - s1
    s.sub(s1)
    
    assert all(s.dataset.x == s2.dataset.x)
    assert all(s.dataset.y == s2.dataset.y)
    
def test_sub_value():
    s_y_np = np.array([2,4,6,8])
    s_y_np1 = s_y_np.copy()
    s_y_np2 = s_y_np - s_y_np1
    
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    
    assert all(s.dataset.y == s_y_np)
    
    s.sub(s1)
    
    assert all(s.dataset.y == s_y_np2)
    
def test_mul():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s * 3.0
    s2 = 3.0 * s
    s.mul(3.0)
    
    assert all(s.dataset.x == s1.dataset.x)
    assert all(s.dataset.y == s1.dataset.y)
    assert all(s.dataset.x == s2.dataset.x)
    assert all(s.dataset.y == s2.dataset.y)
    
def test_mul_value():
    s_y_np = np.array([2,4,6,8])
    s_y_np1 = 3.0 * s_y_np
    
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    
    assert all(s.dataset.y == s_y_np)
    
    s1 =  3.0 * s 
    
    assert all(s1.dataset.y == s_y_np1)