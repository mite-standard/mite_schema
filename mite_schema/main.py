"""Command line interface of mite_schema

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

import argparse
import logging
import sys
from importlib import metadata

import coloredlogs

from mite_schema import SchemaManager


def config_logger(verboseness: str) -> logging.Logger:
    """Set up a named logger with nice formatting

    Args:
        verboseness: sets the logging verboseness

    Returns:
        A Logger object
    """
    logger = logging.getLogger("mite_schema")
    logger.setLevel(getattr(logging, verboseness))
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        coloredlogs.ColoredFormatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    )
    logger.addHandler(console_handler)
    return logger


def setup_cli(args: list) -> argparse.Namespace:
    """Run command line interface using argparse.

    Arguments:
        args: specified arguments

    Returns:
        argparse.Namespace object with command line parameters
    """
    parser = argparse.ArgumentParser(
        description=(
            f"'mite_extras' CLI using MITE schema v{metadata.version('mite_schema')}."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-i",
        type=str,
        required=True,
        nargs="+",
        help="Specifies one or more input files for validation against schema (separated by whitespace).",
    )

    parser.add_argument(
        "-v",
        type=str,
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        required=False,
        help="Specifies the verboseness of logging (default: 'WARNING').",
    )

    return parser.parse_args(args)


def main() -> None:
    """Function to execute main body of code

    Returns:
        A bool indicating the outcome of the validation
    """
    args = setup_cli(sys.argv[1:])
    logger = config_logger(args.v)

    logger.info(
        f"Validate file '{args.i}' with MITE schema v{metadata.version('mite_schema')}."
    )

    for file in args.i:
        try:
            manager = SchemaManager()
            data = manager.read_json(infile=file)
            manager.validate_mite(instance=data)
        except Exception as e:
            logger.fatal(str(e))
            exit(1)

    logger.info(f"Completed validation against MITE schema.")
    exit(0)


if __name__ == "__main__":
    main()
