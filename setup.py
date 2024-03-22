"""Project installation script."""

from setuptools import find_namespace_packages, setup

setup(
    name="ansys-mechanical-env",
    version="0.1.5",
    url="https://github.com/ansys/pymechanical-env",
    author="ANSYS, Inc.",
    author_email="pyansys.core@ansys.com",
    maintainer="ANSYS, Inc.",
    maintainer_email="pyansys.core@ansys.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    license="MIT",
    license_file="LICENSE",
    description="A python wrapper for loading environment variables "
    "when using PyMechanical embedded instances in Linux.",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    python_requires=">3.8,<4",
    packages=find_namespace_packages(where="src", include="ansys*"),
    package_dir={"": "src"},
    include_package_data=True,
    scripts=["src/ansys/mechanical/env/mechanical-env"],
    entry_points={
        "console_scripts": ["find-mechanical=ansys.mechanical.env.run:cli_find_mechanical"]
    },
    install_requires=[
        "importlib-metadata >=4.0",
        "ansys-tools-path>=0.3.1",
        "click>=8.1.3",
    ],
)
