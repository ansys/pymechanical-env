PyMechanical-Env
================
|pyansys| |python| |pypi| |GH-CI| |MIT| |black| |pre-commit-ci|

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
   :target: https://docs.pyansys.com/
   :alt: PyAnsys

.. |python| image:: https://img.shields.io/pypi/pyversions/ansys-mechanical-env?logo=pypi
   :target: https://pypi.org/project/ansys-mechanical-env
   :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/ansys-mechanical-env.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/ansys-mechanical-env
   :alt: PyPI

.. |GH-CI| image:: https://github.com/ansys/pymechanical-env/actions/workflows/ci_cd.yml/badge.svg
   :target: https://github.com/ansys/pymechanical-env/workflows/ci_cd.yml
   :alt: GH-CI

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
   :target: https://github.com/psf/black
   :alt: Black

.. |pre-commit-ci| image:: https://results.pre-commit.ci/badge/github/ansys/pymechanical-env/main.svg
   :target: https://results.pre-commit.ci/latest/github/ansys/pymechanical-env/main
   :alt: pre-commit.ci status

Overview
--------

PyMechanical-Env contains a package, ``ansys-mechanical-env``, that facilitates the integration
of PyMechanical within a Linux environment. The package has the ability to:

- Automatically determine the version and location of the Ansys Mechanical software.
- Offer users the option to manually specify the version number for Mechanical.
- Configure and set the requisite environment variables.

Installation
------------

Two installation modes are provided: user and developer.

Install in user mode
^^^^^^^^^^^^^^^^^^^^

Before installing the ``ansys-mechanical-env`` package, make sure that you
have the latest version of `pip`_ with this command:

.. code:: bash

 python -m pip install -U pip

Then, install the ``ansys-mechanical-env`` package with this command:

.. code:: bash

 python -m pip install ansys-mechanical-env

Install in developer mode
^^^^^^^^^^^^^^^^^^^^^^^^^

Installing the ``ansys-mechanical-env`` package in developer mode allows you to modify the
source and enhance it.

Before contributing to the project, ensure that you are thoroughly familiar with the
`PyAnsys Developer's Guide`_.

To install the ``ansys-mechanical-env`` package in developer mode, perform these steps:

#. Clone the PyMechanical-Env repository with this command:

   .. code:: bash

      git clone https://github.com/ansys/pymechanical-env

#. Create a clean Python environment and activate it with these commands:

   .. code:: bash

      # Create a virtual environment
      python -m venv .venv

      # Activate it in a POSIX system
      source .venv/bin/activate

      # Activate it in Windows CMD environment
      .venv\Scripts\activate.bat

      # Activate it in Windows Powershell
      .venv\Scripts\Activate.ps1

#. Make sure you have the latest required build system and documentation, testing, and CI tools
   with these commands:

   .. code:: bash

      python -m pip install -U pip setuptools tox
      python -m pip install -r requirements/requirements_build.txt
      python -m pip install -r requirements/requirements_tests.txt


#. Install the project in editable mode with this command:

   .. code:: bash

      python -m pip install --editable ansys-mechanical-env

#. Verify your development installation by running this command:

   .. code:: bash

      tox

Basic usage
-----------

Once the ``ansys-mechanical-env`` and ``ansys-mechanical-core`` packages are installed,
you can run the PyMechanical-Env command-line tool to launch and test embedded instances
of PyMechanical on Linux.

Launching a Python shell containing environment variables set up by PyMechanical-Env
allows you to run embedded instances of PyMechanical on Linux.

Launch the Python shell with this command:

.. code:: bash

   mechanical-env python

In the Python shell, use this code to run an embedded instance of PyMechanical:

.. code:: python

   import ansys.mechanical.core as pymechanical
   app = pymechanical.App()
   print(app)

Run all embedding tests in the PyMechanical repository with this command:

.. code:: bash

   xvfb-run mechanical-env pytest -m embedding

How to test
-----------

This project takes advantage of `tox`_. This tool allows you to automate common
development tasks (similar to Makefile), but it is oriented towards Python
development.

Using ``tox``
^^^^^^^^^^^^^

As Makefile has rules, ``tox`` has environments. In fact, ``tox`` creates its
own virtual environment so anything being tested is isolated from the project to
guarantee the project's integrity. These environment commands are provided:

- **tox -e style**: Checks for coding style quality.
- **tox -e py**: Checks for unit tests.
- **tox -e py-coverage**: Checks for unit testing and code coverage.

Raw testing
^^^^^^^^^^^

If required, you can always call the style commands (`black`_, `isort`_,
`flake8`_...) or unit testing ones (`pytest`_) from the command line. However,
this does not guarantee that your project is being tested in an isolated
environment, which is the reason why tools like ``tox`` exist.

A note on pre-commit
^^^^^^^^^^^^^^^^^^^^

The style checks take advantage of `pre-commit`_. Developers are not forced but
encouraged to install this tool with this command:

.. code:: bash

    python -m pip install pre-commit && pre-commit install

Distributing
------------

If you would like to create either source or wheel files, start by installing
the building requirements and then execute the build module:

.. code:: bash

    python -m pip install -r requirements/requirements_build.txt
    python -m build
    python -m twine check dist/*

Documentation and issues
------------------------

Documentation for the latest stable release of this package can be found in this
README file.

On the `PyMechanical-Env Issues page <https://github.com/ansys-internal/pymechanical-env/issues>`_,
you can create issues to report bugs and request new features. On the
`PyMechanical-Env Discussions <https://github.com/ansys-internal/pymechanical-env/discussions>`_
page or the `Discussions page <https://discuss.ansys.com/>`_ on the Ansys Developer portal, you
can post questions, share ideas, and get community feedback.

To reach the project support team, email `pyansys.core@ansys.com <pyansys.core@ansys.com>`_.

License and acknowledgments
---------------------------

PyMechanical-Env is licensed under the `MIT license <https://github.com/ansys/pymechanical-env/blob/main/LICENSE>`_.

For more information, see the `.reuse/dep5 file <https://github.com/ansys/pymechanical-env/blob/main/.reuse/dep5>`_
file, which follows the `Reuse specification <https://reuse.software/spec/>`_.

PyMechanical-Env makes no commercial claim over Ansys whatsoever. This tool supports
`PyMechanical <https://github.com/ansys/pymechanical>`_, which extends the functionality
of Ansys Mechanical by adding a Python interface to the Mechanical service without changing
the core behavior or license of the original software. The use of PyMechanical with an embedded
or remote instance of the Mechanical application requires a legally licensed local copy of Ansys.

For more information on the Mechanical application, see the `Ansys Mechanical <https://www.ansys.com/products/structures/ansys-mechanical>`_
page on the Ansys website.


.. LINKS AND REFERENCES
.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _pip: https://pypi.org/project/pip/
.. _pre-commit: https://pre-commit.com/
.. _PyAnsys Developer's Guide: https://dev.docs.pyansys.com/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.wiki/
