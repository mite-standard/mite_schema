mite_schema
=========

[![DOI](https://zenodo.org/badge/838326204.svg)](https://zenodo.org/doi/10.5281/zenodo.13294150)
[![PyPI version](https://badge.fury.io/py/mite-schema.svg)](https://badge.fury.io/py/mite-schema)

This repository contains the schema of the **MITE** data standard. 

Furthermore, this repository provides functionality to validate files against said schema.
It can be used as command line interface or as library. For command line use, see the installation instructions below.

For more information, see the [MITE Data Standard Organization page](https://github.com/mite-standard).

## Installation

- `pip install mite_schema`

## Quick Start

To validate your MITE-formatted .json-file(s), run:

- `mite_schema -i <input1.json input2.json ... inputN.json>`

### For developers

- Install `hatch` using one of the methods described [here](https://hatch.pypa.io/1.12/install/)
- Download or clone this repository
- Run `hatch -v env create dev`. This will download and install the appropriate Python version and any required packages
- Run `hatch run dev:pre-commit install`. This will set up `pre-commit`
- If necessary, remove the environment with `hatch env remove dev`
