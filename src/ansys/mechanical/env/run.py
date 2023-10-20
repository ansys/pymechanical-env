"""CLI to find mechanical version and location."""
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
    help='Ansys Revision number, e.g. "241" or "232".\
         If a revision number is not specified, git it uses the default from \
            ansys-tools-path.',
)
def cli_find_mechanical(revision: int):
    """
    CLI tool to find the mechanical version and location.

    Parameters
    ----------
    revision : int
        The Ansys Revision number.
    Example:
    --------
    Gets the version and location of install directory
    >>> find-mechanical -r 232
    """
    # Gets the revision number
    if not revision:
        exe, version = atp.find_mechanical()
    else:
        exe, version = atp.find_mechanical(version=revision)
    version = int(version * 10)

    aisol_path = os.path.dirname(exe)
    print(version, aisol_path)

    return version, aisol_path
