from colormath import color_objects, color_conversions
from spectra.grapefruit import Color as GC
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
        _rgb = self.color_object if space == "rgb" else self.to("rgb").color_object
        self.rgb = _rgb.get_value_tuple()
        self.clamped_rgb = (_rgb.clamped_rgb_r, _rgb.clamped_rgb_g, _rgb.clamped_rgb_b)
    
    @classmethod
    def from_html(cls, html_string):
        rgb = GC.NewFromHtml(html_string).rgb
        return cls("rgb", *rgb)

    def to(self, space):
        if space == self.space: return self
        new_color = convert_color(self.color_object, COLOR_SPACES[space])
        return self.__class__(space, *new_color.get_value_tuple())
    
    @property
    def hexcode(self):
        return COLOR_SPACES["rgb"](*self.clamped_rgb).get_rgb_hex()
        
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

class Scale(object):
    def __init__(self, colors, domain=None, mapping=None):
        self.colors = colors
        n = len(colors)
        self._domain = domain or [ float(x) / (n - 1) for x in range(n) ]
        self._mapping = mapping or (lambda x: x)
        
    def __call__(self, num):
        if num < self._domain[0] or num > self._domain[-1]:
            msg = "Number ({0}) not in domain ({1} -> {2})."
            raise ValueError(msg.format(num, self._domain[0], self._domain[-1]))
        f = self._mapping
        segments = zip(self._domain[:-1], self._domain[1:])
        for i, seg in enumerate(segments):
            x0, x1 = seg
            if num >= x0 and num <= x1:
                num_range = f(x1) - f(x0)
                prop = float(f(num) - f(x0)) / num_range
                return self.colors[i].blend(self.colors[i+1], prop)
    
    def domain(self, domain):
        return self.__class__(self.colors, domain, self._mapping)
    
    def mapping(self, mapping):
        return self.__class__(self.colors, self._domain, mapping)
    
    def colorspace(self, space):
        new_colors = [ c.to(space) for c in self.colors ]
        return self.__class__(new_colors, self._domain, self._mapping)

    def range(self, count):
        if count <= 1:
            raise ValueError("Range size must be greater than 1.")
        dom = self._domain
        distance = dom[-1] - dom[0]
        props = [ self(dom[0] + distance * float(x)/(count-1))
            for x in range(count) ]
        return props
