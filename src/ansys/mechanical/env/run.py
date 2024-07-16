# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""CLI to find Mechanical version and location."""
import os

import ansys.tools.path as atp
import click


@click.command()
@click.help_option("--help", "-h")
@click.option(
    "-r",
    "--version",
    default=None,
    type=int,
    help='Ansys version number, such as "242" or "241".\
         If a version number is not specified, it uses the default from \
            ansys-tools-path.',
)
def cli_find_mechanical(version: int):
    """
    Use the CLI tool to find the Mechanical version and location.

    Parameters
    ----------
    version: int
        Ansys version number.

    Example
    -------
    Get the version and location of the installation directory.

    >>> find-mechanical -r 242
    """
    # checks for saved mechanical path else try to find installation path
    _exe = atp.get_mechanical_path(allow_input=False, version=version)
    _version = atp.version_from_path("mechanical", _exe)

    _aisol_path = os.path.dirname(_exe)
    print(_version, _aisol_path)

    return _version, _aisol_path
