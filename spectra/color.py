from colormath import color_objects, color_conversions
from grapefruit import Color as GC
convert_color = color_conversions.convert_color

COLOR_SPACES = {
    "lab": color_objects.LabColor,
    "rgb": color_objects.sRGBColor,
    "lch": color_objects.LCHabColor,
    "xyz": color_objects.XYZColor,
    "hsl": color_objects.HSLColor,
    "hsv": color_objects.HSVColor,
    "cmy": color_objects.CMYColor,
    "cmyk": color_objects.CMYKColor
}

class Color(object):
    def __init__(self, space, *values):
        self.values = values
        self.space = space
        self.color_object = COLOR_SPACES[space](*values)
    
    @classmethod
    def from_html(cls, html_string):
        rgb = GC.NewFromHtml(html_string).rgb
        return cls("rgb", *rgb)

    def to(self, space):
        if space == self.space: return self
        new_color = convert_color(self.color_object, COLOR_SPACES[space])
        return self.__class__(space, *new_color.get_value_tuple())
    
    @property
    def rgb(self):
        if self.space == "rgb":
            return self.values
        rgb = self.to("rgb").color_object
        return (rgb.clamped_rgb_r, rgb.clamped_rgb_g, rgb.clamped_rgb_b)
        
    @property
    def hexcode(self):
        if self.space == "rgb":
            return self.color_object.get_rgb_hex()
        return self.__class__("rgb", *self.rgb).hexcode
        
    def blend(self, other, ratio=0.5):
        keep = 1.0 - ratio
        if not self.space == other.space:
            raise Exception("Colors must belong to the same colorspace.")
        values = tuple(((u * keep) + (v * ratio)
            for u, v in zip(self.values, other.values)))
        return self.__class__(self.space, *values)

    def brighten(self, amount=10):
        lch = self.to("lch")
        l, c, h = lch.values
        new_lch = self.__class__("lch", l + amount, c, h)
        return new_lch.to(self.space)

    def darken(self, amount=10):
        return self.brighten(amount=-amount)

    def saturate(self, amount=10):
        lch = self.to("lch")
        l, c, h = lch.values
        new_lch = self.__class__("lch", l, c + amount, h)
        return new_lch.to(self.space)

    def desaturate(self, amount=10):
        return self.saturate(amount=-amount)
