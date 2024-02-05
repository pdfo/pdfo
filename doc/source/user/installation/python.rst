.. _installation-python:

Installation for Python
=======================

Recommended installation
------------------------

To use the Python version of PDFO on Linux, Mac, or Windows, you need `Python <https://www.python.org>`_ 3.8 or above.

We highly recommend installing PDFO via `PyPI <https://pypi.org/project/pdfo>`_.
This does not need you to download the source code.
Install `pip <https://pip.pypa.io/en/stable/installing>`_ in your system, then execute

.. code-block:: bash

    pip install pdfo

in a command shell (e.g., the terminal in Linux or Mac, or the Command Shell for Windows).
If your pip launcher is not ``pip``, adapt the command accordingly (it may be ``pip3`` for example).
If this command runs successfully, PDFO is installed.
You may verify the installation by

.. code-block:: bash

    python -m unittest pdfo.testpdfo

Once again, if your Python launcher is not ``python``, adapt the command accordingly (it may be ``python3`` for example).
If you are an Anaconda user, PDFO is also available through the `conda installer <https://anaconda.org/conda-forge/pdfo>`_.

.. important::

    Python wheels (i.e., pre-compiled packages) are available for Linux, Mac, and Windows.
    However, we only distribute wheels for 64-bit systems.
    We provide wheels for PDFO version 2.0.2 and below only for x86_64 systems.
    Starting from PDFO version 2.1.0, we provide wheels for ARM-based macOS systems, including recent Apple machines with M1, M2, and M3 chips.

Alternative installation (using source distribution)
----------------------------------------------------

Alternatively, although deeply discouraged, PDFO can be installed from the source code.
It requires you to install additional Python headers and a Fortran compiler (e.g., `gfortran <https://gcc.gnu.org/fortran>`_).
Download and decompress the source code package.
You will obtain a folder containing ``pyproject.toml``.
In a command shell, change your directory to this folder, and then run

.. code-block:: bash

    pip install .
