from .core import COLOR_SPACES, Color, Scale
from ._version import __version__

def lab(L, a, b):
    """
    Create a spectra.Color object in the CIELAB color space.

    :param float L: L coordinate.
    :param float a: a coordinate.
    :param float b: b coordinate.

    :rtype: Color
    :returns: A spectra.Color object in the CIELAB color space.
    """
    return Color("lab", L, a, b)

def lch(L, c, h):
    """
    Create a spectra.Color object in the CIE LCH color space.

    Based on `colormath`'s LCHabColor class.

    :param float L: L coordinate.
    :param float c: c coordinate.
    :param float h: h coordinate.

    :rtype: Color
    :returns: A spectra.Color object in the CIE LCH color space.
    """
    return Color("lch", L, c, h)

def xyz(x, y, z):
    """
    Create a spectra.Color object in the XYZ color space.

    Based on `colormath`'s LCHabColor class.

    :param float x: x coordinate.
    :param float y: y coordinate.
    :param float z: z coordinate.

    :rtype: Color
    :returns: A spectra.Color object in the XYZ color space.
    """
    return Color("xyz", x, y, z)

def rgb(r, g, b):
    """
    Create a spectra.Color object in the sRGB color space.

    Per `colormath`: "If you pass in upscaled values, we
    automatically scale them down to 0.0-1.0."

    :param float r: r coordinate.
    :param float g: g coordinate.
    :param float b: b coordinate.

    :rtype: Color
    :returns: A spectra.Color object in the sRGB color space.
    """
    return Color("rgb", r, g, b)

def cmyk(c, m, y, k):
    """
    Create a spectra.Color object in the CMYK color space.

    :param float c: c coordinate.
    :param float m: m coordinate.
    :param float y: y coordinate.
    :param float k: k coordinate.

    :rtype: Color
    :returns: A spectra.Color object in the CMYK color space.
    """
    return Color("cmyk", c, m, y, k)

def cmy(c, m, y):
    """
    Create a spectra.Color object in the CMY color space.

    :param float c: c coordinate.
    :param float m: m coordinate.
    :param float y: y coordinate.

    :rtype: Color
    :returns: A spectra.Color object in the CMY color space.
    """
    return Color("cmyk", c, m, y)

def hsl(h, s, l):
    """
    Create a spectra.Color object in the HSL color space.

    :param float h: h coordinate.
    :param float s: s coordinate.
    :param float l: l coordinate.

    :rtype: Color
    :returns: A spectra.Color object in the HSL color space.
    """
    return Color("hsl", h, s, l)

def hsv(h, s, v):
    """
    Create a spectra.Color object in the HSV color space.

    :param float h: h coordinate.
    :param float s: s coordinate.
    :param float v: v coordinate.

    :rtype: Color
    :returns: A spectra.Color object in the HSV color space.
    """
    return Color("hsv", h, s, v)

def html(html_string):
    """
    Create an RGB spectra.Color object from a web-color or hexcode.

    E.g.: "papayawhip", "#FFF", "#ffffff", "FFEFD5"

    :param str html_string: Web-color or hexcode.

    :rtype: Color
    :returns: A spectra.Color object in the sRGB color space.
    """
    return Color.from_html(html_string)

def scale(colors):
    """
    Create a color scale, based on a list of spectra.Color objects.

    The most common use-case involves passing two colors
    (a start and an end), but any number of colors is acceptable.

    Instead of spectra.Color objects, you can also pass a list of 
    web-color or hexcode strings.

    :param list colors: spectra.Color objects or web-color/hexcode strings.

    :rtype: Scale
    :returns: A spectra.Scale object
    """
    return Scale(colors)

def range(colors, count):
    """
    Create a range of `count` colors between two or more base colors.

    Colors should be a list of spectra.Color objects, web-color strings,
    or hexcode strings.

    :param list colors: spectra.Color objects or web-color/hexcode strings.
    :param int count: the number of colors to return.

    :rtype: list
    :returns: A list of `count` spectra.Color objects.
    """
    return Scale(colors).range(count)
