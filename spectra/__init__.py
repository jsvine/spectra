from spectra.color import Color, COLOR_SPACES
from spectra.scale import Scale

VERSION_TUPLE = (0, 0, 0)
VERSION = ".".join(map(str, VERSION_TUPLE))

lab = lambda *args: Color("lab", *args)
xyz = lambda *args: Color("xyz", *args)
rgb = lambda *args: Color("rgb", *args)
cmyk = lambda *args: Color("cmyk", *args)
cmy = lambda *args: Color("cmy", *args)
hsl = lambda *args: Color("hsl", *args)
hsv = lambda *args: Color("hsv", *args)
html = lambda string: Color.from_html(string)
