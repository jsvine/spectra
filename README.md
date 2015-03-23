# Spectra

Spectra is a Python library that makes color math, color scales, and color-space conversion easy. Support for:

- Color scales (linear, non-linear, and polylinear)
- Color ranges
- Color blending
- Brightening/darkening colors
- Saturating/desaturating colors
- Conversion to/from multiple [color spaces](http://en.wikipedia.org/wiki/Color_space):
    - `rgb` (specifically: [sRGB](http://en.wikipedia.org/wiki/SRGB))
    - `hsl`
    - `hsv`
    - `lab` ([CIELAB](http://en.wikipedia.org/wiki/Lab_color_space#CIELAB))
    - `lch` (a.k.a. `hcl`)
    - `cmy`
    - `cmyk`
    - `xyz`


Spectra is built on [colormath](http://python-colormath.readthedocs.org/) and [grapefruit](https://github.com/xav/Grapefruit). Spectra is *enormously* inspired by [chroma.js](https://github.com/gka/chroma.js) and [d3's scales](https://github.com/mbostock/d3/wiki/Quantitative-Scales).

## Installation

```sh
pip install spectra
```

## Documentation

See [documentation here](http://nbviewer.ipython.org/github/jsvine/spectra/blob/master/docs/walkthrough.ipynb).

## Feedback/Suggestions

Issues and pull requests very much appreciated.
