from spectra.core import COLOR_SPACES, Color, Scale

VERSION_TUPLE = (0, 0, 5)
VERSION = ".".join(map(str, VERSION_TUPLE))

lab = lambda *args: Color("lab", *args)
lch = lambda *args: Color("lch", *args)
xyz = lambda *args: Color("xyz", *args)
rgb = lambda *args: Color("rgb", *args)
cmyk = lambda *args: Color("cmyk", *args)
cmy = lambda *args: Color("cmy", *args)
hsl = lambda *args: Color("hsl", *args)
hsv = lambda *args: Color("hsv", *args)
html = lambda string: Color.from_html(string)

scale = lambda colors: Scale(colors)
range = lambda colors, count: Scale(colors).range(count)
