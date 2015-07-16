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
    """
    Represents a color in a given color space.
    """
    def __init__(self, space, *values):
        """
        :param str space: Name of the color space.
        """
        self.values = values
        self.space = space
        self.color_object = COLOR_SPACES[space](*values)
        _rgb = self.color_object if space == "rgb" else self.to("rgb").color_object
        self.rgb = _rgb.get_value_tuple()
        self.clamped_rgb = (_rgb.clamped_rgb_r, _rgb.clamped_rgb_g, _rgb.clamped_rgb_b)
        self.rbg_clamped = self.clamped_rgb
    
    @classmethod
    def from_html(cls, html_string):
        """
        Create sRGB color from a web-color name or hexcode.

        :param str html_string: Web-color name or hexcode.

        :rtype: Color
        :returns: A spectra.Color in the sRGB color space.
        """
        rgb = GC.NewFromHtml(html_string).rgb
        return cls("rgb", *rgb)

    def to(self, space):
        """
        Convert color to a different color space.

        :param str space: Name of the color space.

        :rtype: Color
        :returns: A new spectra.Color in the given color space.
        """
        if space == self.space: return self
        new_color = convert_color(self.color_object, COLOR_SPACES[space])
        return self.__class__(space, *new_color.get_value_tuple())
    
    @property
    def hexcode(self):
        """
        Get this color's corresponding RGB hex.

        :rtype: str
        :returns: A six-character string.
        """
        return COLOR_SPACES["rgb"](*self.clamped_rgb).get_rgb_hex()
        
    def blend(self, other, ratio=0.5):
        """
        Blend this color with another color in the same color space.

        By default, blends the colors half-and-half (ratio: 0.5).

        :param Color other: The color to blend.
        :param float ratio: How much to blend (0 -> 1).

        :rtype: Color
        :returns: A new spectra.Color
        """
        keep = 1.0 - ratio
        if not self.space == other.space:
            raise Exception("Colors must belong to the same color space.")
        values = tuple(((u * keep) + (v * ratio)
            for u, v in zip(self.values, other.values)))
        return self.__class__(self.space, *values)

    def brighten(self, amount=10):
        """
        Brighten this color by `amount` luminance.

        Converts this color to the LCH color space, and then
        increases the `L` parameter by `amount`.

        :param float amount: Amount to increase the luminance.

        :rtype: Color
        :returns: A new spectra.Color
        """
        lch = self.to("lch")
        l, c, h = lch.values
        new_lch = self.__class__("lch", l + amount, c, h)
        return new_lch.to(self.space)

    def darken(self, amount=10):
        """
        Darken this color by `amount` luminance.

        Converts this color to the LCH color space, and then
        decreases the `L` parameter by `amount`.

        :param float amount: Amount to decrease the luminance.

        :rtype: Color
        :returns: A new spectra.Color
        """
        return self.brighten(amount=-amount)

    def saturate(self, amount=10):
        """
        Saturate this color by `amount` chroma.

        Converts this color to the LCH color space, and then
        increases the `C` parameter by `amount`.

        :param float amount: Amount to increase the chroma.

        :rtype: Color
        :returns: A new spectra.Color
        """
        lch = self.to("lch")
        l, c, h = lch.values
        new_lch = self.__class__("lch", l, c + amount, h)
        return new_lch.to(self.space)

    def desaturate(self, amount=10):
        """
        Desaturate this color by `amount` chroma.

        Converts this color to the LCH color space, and then
        decreases the `C` parameter by `amount`.

        :param float amount: Amount to decrease the chroma.

        :rtype: Color
        :returns: A new spectra.Color
        """
        return self.saturate(amount=-amount)

class Scale(object):
    """
    Represents a color scale.
    """
    def __init__(self, colors, domain=None):
        """
        :param list colors: List of two or more spectra.Colors, or web-color/hexcode strings.
        :param domain: List of two or more numbers.
        :type domain: list or None
        """
        _colors = [ c if isinstance(c, Color) else Color.from_html(c)
            for c in colors ]
        self.colors = _colors

        # Set domain
        n = len(_colors)
        self._domain = domain or [ float(x) / (n - 1) for x in range(n) ]

        # Check whether domain is correct length.
        if len(self._domain) != n:
            raise ValueError("len(domain) must equal len(colors)")

    def __call__(self, number):
        """
        Return the color corresponding to the given `number`.

        :param float number: The number to color-ify.

        :rtype: Color
        :returns: A spectra.Color
        """
        if number < self._domain[0] or number > self._domain[-1]:
            msg = "Number ({0}) not in domain ({1} -> {2})."
            raise ValueError(msg.format(number, self._domain[0], self._domain[-1]))
        segments = zip(self._domain[:-1], self._domain[1:])
        for i, seg in enumerate(segments):
            x0, x1 = seg
            if number >= x0 and number <= x1:
                num_range = x1 - x0
                prop = float(number - x0) / num_range
                return self.colors[i].blend(self.colors[i+1], prop)
    
    def domain(self, domain):
        """
        Create a new scale with the given domain. 

        :param list domain: A list of floats.

        :rtype: Scale
        :returns: A new color.Scale object.
        """
        return self.__class__(self.colors, domain)

    def get_domain(self):
        """
        List this scale's domain.

        :rtype: list
        :returns: A list of numbers.
        """
        return self._domain

    def colorspace(self, space):
        """
        Create a new scale in the given color space.

        :param str space: The new color space.

        :rtype: Scale
        :returns: A new color.Scale object.
        """
        new_colors = [ c.to(space) for c in self.colors ]
        return self.__class__(new_colors, self._domain)

    def range(self, count):
        """
        Create a list of colors evenly spaced along this scale's domain.

        :param int count: The number of colors to return.

        :rtype: list
        :returns: A list of spectra.Color objects.
        """
        if count <= 1:
            raise ValueError("Range size must be greater than 1.")
        dom = self._domain
        distance = dom[-1] - dom[0]
        props = [ self(dom[0] + distance * float(x)/(count-1))
            for x in range(count) ]
        return props
