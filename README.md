# Spectra

Spectra is a Python library that simplifies the process of creating color scales and converting colors between color spaces.

Spectra is built on [colormath](http://python-colormath.readthedocs.org/) and [grapefruit](https://github.com/xav/Grapefruit). Spectra is *enormously* inspired by [chroma.js](https://github.com/gka/chroma.js) and [d3's scales](https://github.com/mbostock/d3/wiki/Quantitative-Scales).

## Installation

```sh
pip install spectra
```

## Documentation

See [documentation here](http://nbviewer.ipython.org/github/jsvine/spectra/blob/master/docs/walkthrough.ipynb).

## Supported Color Spaces

- `rgb`
- `hsl`
- `hsv`
- `lab`
- `lch` (a.k.a. `hcl`)
- `cmy`
- `cmyk`
- `xyz`

Spectra also supports specifying `rgb` colors via W3C names or hexcodes.
