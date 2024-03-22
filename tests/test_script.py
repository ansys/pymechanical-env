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

import os
import subprocess

import ansys.tools.path as atp
import pytest


def find_installed_versions():
    """Finds all the installed version of Mechanical."""
    supported_versions = [232, 241, 242]
    versions_found = []
    for supported_version in supported_versions:
        try:
            exe, version = atp.find_mechanical(version=supported_version)
        except:
            version = None
        if version:
            versions_found.append(supported_version)
    return versions_found


@pytest.mark.parametrize("version_number", find_installed_versions())
def test_version_argument(version_number):
    """Ensure script takes version and find if it present"""
    cmd = f"mechanical-env -r {version_number} env"
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()

    # Assert no error after running script
    assert stderr is None or stderr == b""


def test_unsupported_version():
    """Ensure script gives error for unsupported version."""
    cmd = "mechanical-env -r 230 env"
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    assert "ValueError" in stderr.decode()


def test_env_variable():
    """Ensure the system environment does not change when running ``mechanical-env``."""
    start_env = os.environ
    cmd = "mechanical-env python"
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    process.wait()
    stdout = process.stdout.read().decode()
    stderr = process.stderr.read().decode()

    # Get environment after running mechanical-env
    end_env = os.environ

    # Assert the environment did not change
    assert start_env == end_env


@pytest.mark.parametrize("version_number", find_installed_versions())
def test_bash_script(version_number):
    """Check if script sets the environment according to version"""
    cmd = "mechanical-env env 2>&1"
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    return_code = process.returncode

    # Assert for AWP_ROOT variable which created by script
    assert f"AWP_ROOT{version_number}=/install/ansys_inc/v{version_number}/aisol/.." in str(stdout)

    # Assert variable specific to version 232
    if version_number == 232:
        print(version_number)
        assert "/tp/IntelCompiler/2019.3.199/linx64/lib/intel64" in str(stdout)

    # Assert variable specific to version 241
    if version_number == 241:
        print(version_number)
        assert "/tp/nss/3.89/lib" and "/tp/IntelCompiler/2023.1.0/linx64/lib/intel64" in str(stdout)

    # Assert variable specific to version 242
    if version_number == 242:
        print(version_number)
        assert (
            "/tp/openssl/3.0/linx64/lib"
            and "/tp/qt/5.15.16/linx64/lib"
            and "/tp/IntelMKL/2023.1.0/linx64/lib/intel64" in str(stdout)
        )

    # Assert if the script returned successfully
    assert return_code == 0
