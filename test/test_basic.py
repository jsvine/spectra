import pytest

import spectra


def test_polylinear():
    """
    via: https://github.com/jsvine/spectra/issues/4
    """
    colors = ['yellow', 'red', 'black']
    domain = [0, 50, 100]
    color_scale = spectra.scale(colors).domain(domain)
    r = color_scale.range(5)
    results = [ c.hexcode for c in r ]
    goal = ['#ffff00', '#ff8000', '#ff0000', '#800000', '#000000']
    assert(results == goal)


def test_polylinear_fail():
    colors = ['yellow', 'red', 'black']
    domain = [ 0, 50 ] # Domain has one too few items
    with pytest.raises(ValueError):
        spectra.scale(colors).domain(domain)
