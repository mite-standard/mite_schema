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
from referencing import Registry, Resource

logger = logging.getLogger("mite_schema")


class SchemaManager(BaseModel):
    """Pydantic-based class to manage validation against json schema

    Attributes:
        entry: path to base specs of the MITE json schema
        enzyme: path to specs of the enzyme (meta)data
        reactions: path to specs of reaction data
        changelog: path to specs of changelog data (shared with MIBiG)
        citation: path to specs of citation data (shared with MIBiG)
    """

    entry: Path = Path(__file__).parent.parent.joinpath("schema/entry.json")
    enzyme: Path = Path(__file__).parent.parent.joinpath(
        "schema/definitions/enzyme.json"
    )
    reactions: Path = Path(__file__).parent.parent.joinpath(
        "schema/definitions/reactions.json"
    )
    changelog: Path = Path(__file__).parent.parent.joinpath(
        "schema/definitions/changelog.json"
    )
    citation: Path = Path(__file__).parent.parent.joinpath(
        "schema/definitions/citation.json"
    )

    @model_validator(mode="after")
    def validate_files(self):
        if not all(
            (
                self.entry.exists(),
                self.enzyme.exists(),
                self.reactions.exists(),
                self.changelog.exists(),
                self.citation.exists(),
            )
        ):
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
        with open(self.enzyme) as infile:
            enzyme = json.load(infile)
        with open(self.reactions) as infile:
            reactions = json.load(infile)
        with open(self.changelog) as infile:
            changelog = json.load(infile)
        with open(self.citation) as infile:
            citation = json.load(infile)

        registry = Registry()
        registry = registry.with_resource(
            resource=Resource.from_contents(changelog), uri="definitions/changelog.json"
        )
        registry = registry.with_resource(
            resource=Resource.from_contents(citation), uri="definitions/citation.json"
        )
        registry = registry.with_resource(
            resource=Resource.from_contents(enzyme), uri="definitions/enzyme.json"
        )
        registry = registry.with_resource(
            resource=Resource.from_contents(reactions), uri="definitions/reactions.json"
        )

        try:
            jsonschema.validate(instance=instance, schema=entry, registry=registry)
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(
                f"SchemaManager: Validation of instance against "
                f"MITE schema led to an error: '{e!s}"
            ) from e
