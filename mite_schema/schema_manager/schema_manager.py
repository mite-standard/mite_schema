"""Validates input json files against the mite schema

Copyright (c) 2024 to present Mitja M. Zdouc and individual contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import logging
from pathlib import Path
from typing import Self

import jsonschema
from pydantic import BaseModel, ValidationError, model_validator

logger = logging.getLogger("mite_schema")


class SchemaManager(BaseModel):
    """Pydantic-based class to manage validation against json schema

    Attributes:
        entry: path to base specs of the MITE json schema
    """

    entry: Path = Path(__file__).parent.parent.joinpath("schema/entry.json")

    @model_validator(mode="after")
    def validate_files(self):
        if not self.entry.exists():
            raise ValidationError
        return self

    @staticmethod
    def read_json(infile: str | Path) -> dict:
        """Read an input json file and perform basic validation

        Arguments:
            infile: the input json file name

        Returns:
            A dict resulting from the input json file

        Raises:
            FileNotFoundError: file does not exist
            RuntimeError: file is empty or has incorrect suffix
        """
        infile = Path(infile)

        logger.debug(f"SchemaManager: started reading input file '{infile.name}'.")

        if not infile.exists():
            raise FileNotFoundError(f"Input file {infile.name} does not exist.")

        if infile.suffix != ".json":
            raise RuntimeError(f'Input file {infile.name} has no ".json" suffix.')

        with open(infile) as file_in:
            json_dict = json.load(file_in)

        if not json_dict:
            raise RuntimeError(f"Input file {infile.name} appears to be empty.")

        logger.debug(f"SchemaManager: completed reading input file '{infile.name}'.")

        return json_dict

    def validate_mite(self: Self, instance: dict):
        """Validate a dictionary against the MITE JSON schema

        Arguments:
            instance: a dictionary representing a json file

        Raises:
            ValueError: validation of instance against schema led to an error
        """
        logger.debug(f"SchemaManager: started validation against MITE schema.")

        with open(self.entry) as infile:
            entry = json.load(infile)

        try:
            jsonschema.validate(instance=instance, schema=entry)
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(f"Validation error: {e.message}") from e
