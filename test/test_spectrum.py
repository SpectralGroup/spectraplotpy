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
Created on Mon Mar 17 2014

@author: ariamania
"""

import spectraplotpy as spp
import numpy as np
import pytest as pt
from mock import MagicMock


def create_fake_dataset():
    ds = spp.Dataset()
    ds.x = np.array([1, 2, 3, 4])
    ds.y = np.array([2, 4, 6, 8])
    ds.y_errors = np.array([.1, .2, .2, .3])
    ds.x_errors = np.array([.1, .1, .1, .1])
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


def test_Length_Error_exception():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    ds1 = spp.Dataset()
    ds1.x = np.array([1, 2, 3])
    ds1.y = np.array([2, 4, 6])
    s1 = spp.Spectrum(ds1)

    with pt.raises(spp.XCompatibilityError):
        s + s1

    with pt.raises(spp.XCompatibilityError):
        s - s1


def test_different_x_values_exception():
    """Test for exception raised if x-values are diffrent"""
    ds1 = spp.Dataset(x=[1, 2, 3], y=[4, 5, 6])
    ds2 = spp.Dataset(x=[1, 2, 4], y=[4, 5, 6])
    s1 = spp.Spectrum(ds1)
    s2 = spp.Spectrum(ds2)

    with pt.raises(spp.XCompatibilityError):
        s1 + s2

    with pt.raises(spp.XCompatibilityError):
        s1 - s2


def test_add():
    ds1 = spp.Dataset(x=[1, 2, 3], y=[4, 5, 6],
                      x_errors=[0.1, 0.2, 0.3], y_errors=[0.1, 0.1, 0.1])
    ds2 = spp.Dataset(x=[1, 2, 3], y=[2, 3, 4],
                      x_errors=[0.1, 0.1, 0.1], y_errors=[0.2, 0.2, 0.2])
    s1 = spp.Spectrum(ds1)
    s2 = spp.Spectrum(ds2)

    s = s1 + s2

    assert np.array_equal(s.dataset.x, ds1.x)
    assert np.array_equal(s.dataset.y, ds1.y + ds2.y)
    assert np.array_equal(s.dataset.x_errors, ds1.x_errors + ds2.x_errors)
    assert np.array_equal(s.dataset.y_errors, ds1.y_errors + ds2.y_errors)


def test_add_errors_scalar():
    ds1 = spp.Dataset(x=[1, 2, 3], y=[4, 5, 6],
                      x_errors=[0.1, 0.2, 0.3], y_errors=0.2)
    ds2 = spp.Dataset(x=[1, 2, 3], y=[2, 3, 4],
                      x_errors=0.1, y_errors=[0.1, 0.1, 0.1])
    s1 = spp.Spectrum(ds1)
    s2 = spp.Spectrum(ds2)

    s = s1 + s2

    assert np.array_equal(s.dataset.x, ds1.x)
    assert np.array_equal(s.dataset.y, ds1.y + ds2.y)
    assert np.array_equal(s.dataset.x_errors, ds1.x_errors + ds2.x_errors)
    assert np.array_equal(s.dataset.y_errors, ds1.y_errors + ds2.y_errors)


def test_add_errors_2N():
    ds1 = spp.Dataset(x=[1, 2, 3], y=[4, 5, 6],
                      x_errors=[0.1, 0.2, 0.3], y_errors=[0.1, 0.1, 0.1])
    ds2 = spp.Dataset(x=[1, 2, 3], y=[2, 3, 4],
                      x_errors=[[0.1, 0.2, 0.3], [0.1, 0.1, 0.1]], y_errors=0.2)
    s1 = spp.Spectrum(ds1)
    s2 = spp.Spectrum(ds2)

    s = s1 + s2

    assert np.array_equal(s.dataset.x, ds1.x)
    assert np.array_equal(s.dataset.y, ds1.y + ds2.y)
    assert np.array_equal(s.dataset.x_errors, ds1.x_errors + ds2.x_errors)
    assert np.array_equal(s.dataset.y_errors, ds1.y_errors + ds2.y_errors)


def test_add_value():
    s_y_np = np.array([2, 4, 6, 8])
    s_y_np1 = s_y_np.copy()
    s_y_np2 = s_y_np + s_y_np1

    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()

    assert all(s.dataset.y == s_y_np)

    s.add(s1)

    assert all(s.dataset.y == s_y_np2)

def test_sub():
    ds1 = spp.Dataset(x=[1, 2, 3], y=[4, 5, 6],
                      x_errors=[0.1, 0.2, 0.3], y_errors=[0.1, 0.1, 0.1])
    ds2 = spp.Dataset(x=[1, 2, 3], y=[2, 3, 4],
                      x_errors=[0.1, 0.1, 0.1], y_errors=[0.2, 0.2, 0.2])
    s1 = spp.Spectrum(ds1)
    s2 = spp.Spectrum(ds2)

    s = s1 - s2

    assert np.array_equal(s.dataset.x, ds1.x)
    assert np.array_equal(s.dataset.y, ds1.y - ds2.y)
    assert np.array_equal(s.dataset.x_errors, ds1.x_errors + ds2.x_errors)
    assert np.array_equal(s.dataset.y_errors, ds1.y_errors + ds2.y_errors)


def test_sub_value():
    s_y_np = np.array([2, 4, 6, 8])
    s_y_np1 = s_y_np.copy()
    s_y_np2 = s_y_np - s_y_np1

    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()

    assert all(s.dataset.y == s_y_np)

    s.sub(s1)

    assert all(s.dataset.y == s_y_np2)


def test_mul_all():
    """All methods of multiplication should yield the same results"""
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s * 3.0
    s2 = 3.0 * s
    s3 = s.copy()
    s3.mul(3.0)

    # all ways of multiplication should yield the same results
    assert np.array_equal(s3.dataset.x, s1.dataset.x)
    assert np.array_equal(s3.dataset.y, s1.dataset.y)
    assert np.array_equal(s3.dataset.x, s2.dataset.x)
    assert np.array_equal(s3.dataset.y, s2.dataset.y)


def test_mul():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s * 3.0

    assert np.array_equal(s1.dataset.x, ds.x)
    assert np.array_equal(s1.dataset.y, 3.0*ds.y)
    # x_errors are not affected
    assert np.array_equal(s1.dataset.x_errors, ds.x_errors)
    # y_errors are scaled
    assert np.array_equal(s1.dataset.y_errors, ds.y_errors*3.0)


def test_rmul():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = -2.0 * s

    assert np.array_equal(s1.dataset.x, ds.x)
    assert np.array_equal(s1.dataset.y, -2*ds.y)
    # x_errors are not affected
    assert np.array_equal(s1.dataset.x_errors, ds.x_errors)
    # y_errors are scaled
    assert np.array_equal(s1.dataset.y_errors, ds.y_errors*-2.0)


def test_mul_inplace():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    s1.mul(1./3)

    assert np.array_equal(s1.dataset.x, ds.x)
    assert np.array_equal(s1.dataset.y, ds.y*(1./3))
    # x_errors are not affected
    assert np.array_equal(s1.dataset.x_errors, ds.x_errors)
    # y_errors are scaled
    assert np.array_equal(s1.dataset.y_errors, ds.y_errors*(1./3))


def test_mul_value():
    s_y_np = np.array([2, 4, 6, 8])
    s_y_np1 = 3.0 * s_y_np

    ds = create_fake_dataset()
    s = spp.Spectrum(ds)

    assert all(s.dataset.y == s_y_np)

    s1 = 3.0 * s

    assert all(s1.dataset.y == s_y_np1)


def test_div_all():
    """Both methods of division (inplace, copy)
    should yield the same results"""
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s / 3.0
    s2 = s.copy()
    s2.div(3.0)

    assert np.array_equal(s1.dataset.x, s2.dataset.x)
    assert np.array_equal(s1.dataset.y, s2.dataset.y)


def test_div():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s / 3.0

    assert np.array_equal(s1.dataset.x, ds.x)
    assert np.array_equal(s1.dataset.y, ds.y/3.0)
    # x_errors are not affected
    assert np.array_equal(s1.dataset.x_errors, ds.x_errors)
    # y_errors are scaled
    assert np.array_equal(s1.dataset.y_errors, ds.y_errors/3.0)


def test_div_inplace():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    s1 = s.copy()
    s1.div(-2.0)

    assert np.array_equal(s1.dataset.x, ds.x)
    assert np.array_equal(s1.dataset.y, ds.y/-2.0)
    # x_errors are not affected
    assert np.array_equal(s1.dataset.x_errors, ds.x_errors)
    # y_errors are scaled
    assert np.array_equal(s1.dataset.y_errors, ds.y_errors/-2.0)

def test_div_exceptions():
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    # not yet supported
    with pt.raises(TypeError):
        3.0/s
    with pt.raises(ZeroDivisionError):
        s/0
    with pt.raises(ZeroDivisionError):
        s/0.


def test_mock_plot():
    """
    create a mock test for the plot method
    """
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)

    mock_axes = MagicMock()
    mock_axes.plot = MagicMock()
    s.plot(axes=mock_axes)
    mock_axes.plot.assert_called_once_with(s.dataset.x, s.dataset.y,
                                           axes=mock_axes)


def test_errorbar():
    """
    create a mock test for the plot_errorbar method
    """
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)
    x_data = s.dataset.x
    y_data = s.dataset.y
    x_errors = s.dataset.x_errors
    y_errors = s.dataset.y_errors

    mock_axes = MagicMock()
    mock_axes.errorbar = MagicMock()
    s.errorbar(axes=mock_axes)
    mock_axes.errorbar.assert_called_once_with(x_data, y_data,
                                               y_errors, x_errors,
                                               axes=mock_axes)


def test_errorfill():
    #ds = spp.Dataset(x=[1, 2, 3], y = [1, 2, 5], y_errors = [0.1, 0.2, 0.5])
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)

    mock_axes = MagicMock()
    mock_axes.plot = MagicMock()
    mock_axes.fill_between = MagicMock()
    s.errorfill(axes=mock_axes)
    mock_axes.plot.assert_called_once()
    mock_axes.fill_between.assert_called_once()


def test_errorfill_alpha_fill():
    ds = spp.Dataset(x=[1, 2, 3], y=[1, 2, 5], y_errors=[0.1, 0.2, 0.5])
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)

    mock_axes = MagicMock()
    mock_axes.plot = MagicMock()
    mock_axes.fill_between = MagicMock()
    s.errorfill(axes=mock_axes, alpha_fill=0.1)
    mock_axes.plot.assert_called_once()
    mock_axes.fill_between.assert_called_once()


def test_errorfill_no_erros():
    """ What happens if no errors are present ... just plot """
    ds = create_fake_dataset()
    s = spp.Spectrum(ds)

    mock_axes = MagicMock()
    mock_axes.plot = MagicMock()
    mock_axes.fill_between = MagicMock()
    s.errorfill(axes=mock_axes)
    mock_axes.plot.assert_called_once()
