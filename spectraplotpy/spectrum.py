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
spectrum.py
"""
import copy
import numpy as np
import custom_exceptions
import matplotlib.pyplot as plt


def check_compatible_x(first_spec, other_spec, raise_exception=True):
    """
    Checks if two spectra can be added or subtracted.

    The x values must be of the same length and all must have the same value.
    The length of the y values is checked as well (this is a bit redundant)

    Parameters
    ----------
    other_spec: Spectrum
        The other spectrum that is checked for compatibility against first_spec.

    raise_exception=True: bool
        If false exceptions are not raised

    Returns
    -------
    True if spectra are compatible, false otherwise.

    Raises
    ------
    custom_exceptions.XCompatibilityError
    """
    if len(first_spec.dataset.x) != len(other_spec.dataset.x):
        if raise_exception:
            fmtstr = "Lengths of dataset.x are not equal! ({l1} != {l2})"
            raise custom_exceptions.XCompatibilityError(
                fmtstr.format(l1=len(first_spec.dataset.x), l2=len(other_spec.dataset.x)))
        return False

    if not np.array_equal(first_spec.dataset.x, other_spec.dataset.x):
        if raise_exception:
            fmtstr = "Not all values of dataset.x are the same!"
            raise custom_exceptions.XCompatibilityError(fmtstr)
        return False

    return True


class Spectrum(object):
    """
    An object class defining a spectrum
    """
    def __init__(self, dataset):
        """ """
        self.dataset = dataset


#    def __str__(self):
#        return 'spectum('self.dataset.metadata.filename))
    def add_absolute_errors(self, other):
        """
        Adds the absolute errors (when adding or substracting two spectra)

        The addition is not done in-place, due to broadcasting
        The problem is:

            a = np.array([1, 2, 3])
            b = np.array([[1, 2, 3],[-1 ,-1, -1]])

        then
           * a + b work
           * a += b fail
           * b += a work

        Would this ever be problematic? Don't want to go into premature optimizations...
        """
        self.dataset.x_errors = self.dataset.x_errors + other.dataset.x_errors
        self.dataset.y_errors = self.dataset.y_errors + other.dataset.y_errors

    def add_relative_errors(self, other, new_y):
        """
        Adds the relative errors (when multiplying or dividig two spectra).
        Must be called *before* the y-values have allready been modfied.

        The addition is not done in-place, due to broadcasting.

        Would this ever be problematic? Don't want to go into premature optimizations...
        """
        # since the x values are always he same, the absolute errors can just be added
        self.dataset.x_errors = self.dataset.x_errors + other.dataset.x_errors
        self.dataset.y_errors = (self.dataset.y_errors/self.dataset.y +
                                other.dataset.y_errors/other.dataset.y) * \
                                new_y

    def __add__(self, other):
        """
        adds two spectra, returns third spectrum
        """
        copied = self.copy()
        copied.add(other)
        return copied

    def add(self, other):
        """
        adds two spectra in place
        """
        check_compatible_x(self, other)
        self.dataset.y += other.dataset.y
        self.add_absolute_errors(other)

    def __sub__(self, other):
        """
        substracs two spectra, returns third spectrum
        """
        copied = self.copy()
        copied.sub(other)
        return copied

    def sub(self, other):
        """
        substracs two spectra in place
        """
        check_compatible_x(self, other)
        self.dataset.y -= other.dataset.y
        self.add_absolute_errors(other)

    def __rmul__(self, const):
        """
        reverse multiplication of a number with a spectrum
        """
        copied = self.copy()
        copied.mul(const)
        return copied

    def __mul__(self, const):
        """
        multiplies a spectrum with number returns copy
        """
        copied = self.copy()
        copied.mul(const)
        return copied

    def mul(self, const):
        """
        multiplies a spectrum with a number in place
        """
        self.dataset.y = const * self.dataset.y
        # No abs(const) here, because then we would have to manually switch
        # rows in asymetric errors.
        self.dataset.y_errors = self.dataset.y_errors * const

    def __div__(self, const_or_spec):
        """
        divides a spectrum with a scalar or another spectrum
        """
        copied = self.copy()
        copied.div(const_or_spec)
        return copied

    def div_const(self, const):
        """
        divides a spectrum with a number in place
        """
        # cast to float to avoid surprises with integer division
        fconst = float(const)
        if fconst == 0.:
            raise(ZeroDivisionError, "Spectrum can not be divided by 0")

        self.dataset.y = self.dataset.y / fconst
        self.dataset.y_errors = self.dataset.y_errors / fconst

    def div_spec(self, spec):
        """
        Divides a spectrum with  another spectrum in place.

        The division is done elementwise for the y elements.
        Relative errors are added.
        """
        check_compatible_x(self, spec)
        new_y = self.dataset.y / spec.dataset.y
        self.add_relative_errors(spec, new_y)
        self.dataset.y = new_y


    def div(self, const_or_spec):
        """
        divides a spectrum with a number or another spectrum in place
        """
        if np.isscalar(const_or_spec):
            self.div_const(const_or_spec)
        else:
            self.div_spec(const_or_spec)

    def copy(self):
        """
        creates a copy of a spectrum
        """
        return copy.deepcopy(self)

    def plot(self, *args, **kwargs):
        """
        Plots into `axes` using its plot method, the x and y come from
        the dataset and any other argument you pass will be forwarded to
        the plot method
        """
        axes = kwargs.get('axes', plt.gca())
        return axes.plot(self.dataset.x, self.dataset.y, *args, **kwargs)

    def errorbar(self, *args, **kwargs):
        """
        Plots into `axes` using its errorbar method, the x and y come from
        the dataset and any other argument you pass will be forwarded to
        the errorbar method

        Example
        =======

        >>> import matplotlib.pyplot as plt
        >>> sp.errorbar(plt, '--o')
        """
        axes = kwargs.get('axes', plt.gca())
        return axes.errorbar(
            self.dataset.x, self.dataset.y,
            self.dataset.y_errors, self.dataset.x_errors,
            *args, **kwargs)

    def errorfill(self, *args, **kwargs):
        """
        Plots error bands, using the spectrum y_errors.

        Parameters
        ----------
        axes: matplotlib.Axes()
            Axes into witch to draw.
        color = None
            The color with with to draw. If None is given, one is choshen automatically.
        alpha_fill : float = 0.3
            The alpha level of the error band.

        All the other parameters are passed to `Axes.plot()`

        Notes
        -----
        Inspired by http://tonysyu.github.io/plotting-error-bars.html
        """
        axes = kwargs.get('axes', plt.gca())
        color = kwargs.get('color', axes._get_lines.color_cycle.next())
        alpha_fill = kwargs.pop('alpha_fill', 0.3)

        axes.plot(self.dataset.x, self.dataset.y, color=color, *args, **kwargs)

        if self.dataset.y_errors is None:
            return

        if np.isscalar(self.dataset.y_errors) or len(self.dataset.y_errors) == len(self.dataset.y):
            ymin = self.dataset.y - self.dataset.y_errors
            ymax = self.dataset.y + self.dataset.y_errors
        elif len(self.dataset.y_errors) == 2:
            ymin, ymax = self.dataset.y_errors
        axes.fill_between(self.dataset.x, ymax, ymin, color=color, alpha=alpha_fill)

    def smooth(self, window_len=11, window='hanning'):
        """
        Smoothens spectral data using hanning, hamming, bartlett, and blackman
        schemes and returns smooth data
        """
        if self.dataset.y.ndim != 1:
            raise(ValueError, "smooth only accepts 1 dimension arrays.")

        if self.dataset.y.size < window_len:
            raise(ValueError, "Input vector needs to be bigger than window size")

        if window_len < 3:
            return self.dataset.y

        if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
            raise(ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

        holdspec = np.r_[self.dataset.y[window_len-1:0:-1],
                         self.dataset.y, self.dataset.y[-1:-window_len:-1]]
        #print(len(s))
        if window == 'flat': #moving average
            holdwindow = np.ones(window_len,'d')
        else:
            holdwindow = eval('numpy.'+window+'(window_len)')

        self.dataset.y = np.convolve(holdwindow/holdwindow.sum(), holdspec, mode='valid')

    def y_at_x(self, x):
        """Returns the y value at a specified x value.
        Any values between min and max x are accepted. The returned value is a
        linear interpolation.

        Parameters:
        -----------
            x : array_like
                The x-coordinates of the interpolated values.
        Returns:
        --------
            y : {float, ndarray}
                The interpolated values, same shape as x.
                numpy.NaN is returned for x values outside of xmin and xmax,
        """
        return np.interp(x, self.dataset.x, self.dataset.y,
                         left=np.nan, right=np.nan)
