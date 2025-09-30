mite_schema
=========

[![DOI](https://zenodo.org/badge/838326204.svg)](https://zenodo.org/doi/10.5281/zenodo.13294150)
[![PyPI version](https://badge.fury.io/py/mite-schema.svg)](https://badge.fury.io/py/mite-schema)

Contents
-----------------
- [Overview](#overview)
- [Documentation](#documentation)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Quick Start](#quick-start)
- [Attribution](#attribution)
- [For Developers](#for-developers)

## Overview

**MITE** (Minimum Information about a Tailoring Enzyme) is a community-driven database for the characterization of tailoring enzymes.
These enzymes play crucial roles in the biosynthesis of secondary or specialized metabolites, naturally occurring molecules with strong biological activities, such as antibiotic properties.

This repository contains the data schema in *JSON Schema* format followed by the entries of the  **MITE** data repository [mite_data](https://github.com/mite-standard/mite_data).

For more information, visit the [MITE Data Standard Organization page](https://github.com/mite-standard) or read our [publication]( https://doi.org/10.1093/nar/gkaf969).

## Documentation

This repository is the single source of truth for the formatting of entries of the  **MITE** data repository [mite_data](https://github.com/mite-standard/mite_data).

It contains a data model in form of a *JSON Schema* file and provides CLI functionality to validate files against said schema.
Furthermore, this repository can also be used as a library. For examples, see [mite_data](https://github.com/mite-standard/mite_data), [mite_extras](https://github.com/mite-standard/mite_extras) or [mite_web](https://github.com/mite-standard/mite_web).

For feature requests and suggestions, please refer to the [MITE Schema thread](https://github.com/orgs/mite-standard/discussions/3) in the MITE Discussion forum.

## System Requirements

### OS Requirements

Local installation was tested on:

- Ubuntu Linux 20.04 and 22.04 (command line)

#### Python dependencies

Dependencies including exact versions are specified in the [pyproject.toml](./pyproject.toml) file.

## Installation Guide

### With `pip`

- `pip install mite_schema`

## Quick Start

To validate your MITE-formatted .json-file(s), run:

- `mite_schema -i <input1.json input2.json ... inputN.json>`

## Attribution

### License

`mite_schema` is an open source tool licensed under the MIT license (see [LICENSE](LICENSE)).

### Publications

See [CITATION.cff](CITATION.cff) or [MITE online](https://mite.bioinformatics.nl/) for information on citing MITE.

### Acknowledgements

This work was supported by the Netherlands Organization for Scientific Research (NWO) KIC grant KICH1.LWV04.21.013.

## For Developers

*Nota bene: for details on how to contribute to the MITE project, please refer to [CONTRIBUTING](CONTRIBUTING.md).*

### Package Installation

*Please note that the development installation is only tested and supported on (Ubuntu) Linux.*

#### With `uv` from GitHub

*Note: assumes that `uv` is installed locally - see the methods described [here](https://docs.astral.sh/uv/getting-started/installation/)* 

```commandline
git clone https://github.com/mite-standard/mite_schema
uv sync --extra dev
uv run pre-commit install
```

All tests should be passing
```commandline
uv run pytest
```

### CI/CD and Deployment

CI/CD via GitHub Actions runs on every PR and push to the `main` branch.

A new release created on the [mite_schema](https://github.com/mite-standard/mite_schema) GitHub page will automatically relay changes to [PyPI](https://pypi.org/project/mite-schema/) and [Zenodo](https://doi.org/10.5281/zenodo.13294150).
