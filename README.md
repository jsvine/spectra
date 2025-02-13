# Spectra

Spectra is a Python library that makes color math, color scales, and color-space conversion easy. Support for:

- Color scales
- Color ranges
- Color blending
- Brightening/darkening colors
- Saturating/desaturating colors
- Conversion to/from multiple [color spaces](http://en.wikipedia.org/wiki/Color_space)

Spectra is built on [colormath2](https://github.com/bkmgit/python-colormath2) and [grapefruit](https://github.com/xav/Grapefruit). Spectra is *enormously* inspired by [chroma.js](https://github.com/gka/chroma.js) and [d3's scales](https://github.com/mbostock/d3/wiki/Quantitative-Scales).

## Installation

```sh
pip install spectra
```

## Walkthrough

See [this walkthrough](docs/walkthrough.ipynb) to see what Spectra can do.

## API

### Creating color objects from web-colors or hexcode strings

##### `spectra.html(html_string)`

E.g., `spectra.html("papayawhip")`, `spectra.html("#BAABAA")` `spectra.html("#FFF")`

### Creating color objects from color space values

##### `spectra.rgb(r, g, b)`

Specifically: [sRGB](http://en.wikipedia.org/wiki/SRGB)

---

##### `spectra.lab(L, a, b)`

Specifically: [CIELAB](http://en.wikipedia.org/wiki/Lab_color_space#CIELAB)

---

##### `spectra.lch(L, c, h)`

Also known elsewhere as "hcl"

---

##### `spectra.hsl(h, s, l)`

---

##### `spectra.hsv(h, s, v)`

---

##### `spectra.xyz(x, y, z)`

---

##### `spectra.cmy(c, m, y)`

---

##### `spectra.cmky(c, m, y, k)`

---

### Getting color values

Instances of `spectra.Color` have four main properties:

- __`.values`__: An array representation of the color's values in its own color space, e.g. `(L, a, b)` for an `lab` color.
- __`.hexcode`__: The hex encoding of this color, e.g. `#ffffff` for `rgb(255, 255, 255)`/`html(\"white\")`.
- __`.rgb`__: The `(r, g, b)` values for this color in the `rgb` color space; these are allowed to go out of gamut.
- __`.clamped_rgb`__: The \"clamped\" `(r, g, b)` values for this color in the `rgb` color space.

Note on `.rgb` and `.rgb_clamped`: Spectra follows [colormath](http://python-colormath.readthedocs.org/en/latest/conversions.html?highlight=clamp#rgb-conversions-and-out-of-gamut-coordinates)'s convention:

> RGB spaces tend to have a smaller gamut than some of the CIE color spaces. When converting to RGB, this can cause some of the coordinates to end up being out of the acceptable range (0.0-1.0 or 1-255, depending on whether your RGB color is upscaled). [...] Rather than clamp these for you, we leave them as-is.

### Modifying colors

##### `color.to(space)`

Convert this color to another color space.

```python
teal_lab = spectra.html("teal").to("lab")
print(teal_lab.values)
>>> (48.25453959565715, -28.843707890081394, -8.48135382506432)
```

---

##### `color.blend(other_color, ratio=0.5)`

Blend this color with another color, using `ratio` of that other color.

```python
yellow, red = spectra.html("red"), spectra.html("yellow")
orange = yellow.blend(red)
print(orange.hexcode)
>>> '#ff8000'
```

---

##### `color.brighten(amount=10)`

Brighten this color by `amount` luminance. (Converts this color to the LCH color space, and then increases the `L` parameter by `amount`.)

```python
teal = spectra.html("teal")
light_teal = light_teal.brighten(30)
print(light_teal.hexcode)
>>> '#75d1d0'
```

---

##### `color.darken(amount=10)`

The opposite of `color.brighten`; *reduces* color by `amount` luminance.

---

##### `color.saturate(amount=10)`

Saturate this color by `amount` chroma. (Converts this color to the LCH color space, and then increases the `C` parameter by `amount`.)

---

##### `color.desaturate(amount=10)`

The opposite of `color.saturate`; *reduces* color by `amount` chroma.

---

### Creating color scales

##### `spectra.scale(colors)`

`colors` should be a list of two or more colors (created by any of the methods above), web-color names, or hexcodes.

Returns a `spectra.Scale` object, which translates numbers to their corresponding colors:

```python
my_scale = spectra.scale([ "gray", "red" ])
halfway = my_scale(0.5)
print(halfway.hexcode)
>>> '#c04040'
```

---

### Modifying color scales

##### `scale.domain(numbers)`

By default, a scale's domain is [ 0, 1 ]. But you can change it to be anything else, e.g.:

```python
my_scale = spectra.scale([ "gray", "red" ]).domain([ 10, 20 ])
halfway = my_scale(15)
print(halfway.hexcode)
>>> '#c04040'
```

---

### Creating color ranges

##### `scale.range(count)`

This function returns a list of `spectra.Color` objects evenly spaced between a scale's `colors`. For example:

```python
my_scale = spectra.scale([ "gray", "red" ])
my_range = my_scale.range(5)

print(my_range)
>>> [<spectra.core.Color object at 0x10f4759d0>, <spectra.core.Color object at 0x10f475a90>, 
    <spectra.core.Color object at 0x10f475b50>, <spectra.core.Color object at 0x10f475cd0>, 
    <spectra.core.Color object at 0x10f475d50>]

print([ c.hexcode for c in my_range ])
>>> ['#808080', '#a06060', '#c04040', '#df2020', '#ff0000']
```

Alternatively, as a shortcut, you can use `spectra.range(colors, count)`.

---

## Feedback/Suggestions

Issues and pull requests very much appreciated.
