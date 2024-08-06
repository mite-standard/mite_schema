mite_schema
=========

This repository contains the schema of the **Minimum Information about a Tailoring Enzyme** data standard. 

Furthermore, this repository provides functionality to validate files against said schema.
It can be used as command line interface or as library. For command line use, see the installation instructions below.

More information about the schema can be found in [the MITE publication](https://doi.org/10.26434/chemrxiv-2024-78mtl).

## Installation

- `pip install mite_schema`

## Quick Start

To validate your MITE-formatted .json-file, run:

- `mite_schema -i <input.json>`

### For developers

- Install `hatch` using one of the methods described [here](https://hatch.pypa.io/1.12/install/)
- Download or clone this repository
- Run `hatch -v env create dev`. This will download and install the appropriate Python version and any required packages
- Run `hatch run dev:pre-commit install`. This will set up `pre-commit`
- If necessary, remove the environment with `hatch env remove dev`