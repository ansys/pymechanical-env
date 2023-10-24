# Copyright (C) 2023 ANSYS, Inc. and/or its affiliates.
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
    "--revision",
    default=None,
    type=int,
    help='Ansys revision number, such as "241" or "232".\
         If a revision number is not specified, git it uses the default from \
            ansys-tools-path.',
)
def cli_find_mechanical(revision: int):
    """
    Use the CLI tool to find the Mechanical version and location.

    Parameters
    ----------
    revision : int
        Ansys revision number.

    Example
    -------
    Get the version and location of the installation directory.

    >>> find-mechanical -r 232
    """
    # Get the revision number
    if not revision:
        exe, version = atp.find_mechanical()
    else:
        exe, version = atp.find_mechanical(version=revision)
    version = int(version * 10)

    aisol_path = os.path.dirname(exe)
    print(version, aisol_path)

    return version, aisol_path
