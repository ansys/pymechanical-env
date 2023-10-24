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

import os

import pytest


@pytest.fixture(scope="session")
def make_executable_and_restore(request):
    # Define the path to your script
    script_directory = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src/ansys/mechanical/env")
    )
    script_path = os.path.join(script_directory, "mechanical-env")

    # Set the execute permission to 0o755
    # (read, write, and execute for owner, read and execute for group and others)
    os.chmod(script_path, 0o755)

    # Yield to the test functions
    yield

    # Restore the original file permissions after the test session
    # (read, write, and execute for owner, read for group and others)
    os.chmod(script_path, 0o644)
