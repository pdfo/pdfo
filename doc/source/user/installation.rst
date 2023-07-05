.. _installation:

Installation
============

PDFO can be installed separately for :ref:`Python <python-installation>` and :ref:`MATLAB <matlab-installation>`, as detailed below.

.. _python-installation:

Python
------

Recommended installation
^^^^^^^^^^^^^^^^^^^^^^^^

To use the Python version of PDFO on Linux, Mac, or Windows, you need `Python <https://www.python.org>`_ 3.7 or above.

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

Alternative installation (using source distribution)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, although *deeply discouraged*, PDFO can be installed from the source code.
It requires you to install additional Python headers and a Fortran compiler (e.g., `gfortran <https://gcc.gnu.org/fortran>`_).
Download and decompress the source code package.
You will obtain a folder containing ``pyproject.toml``.
In a command shell, change your directory to this folder, and then run

.. code-block:: bash

    pip install .

.. _matlab-installation:

MATLAB
------

Prerequisites
^^^^^^^^^^^^^

PDFO supports MATLAB R2014a and later releases. To use the MATLAB version of PDFO, you need first to configure the MEX of your MATLAB so that it can compile Fortran. To check whether your `MEX <https://www.mathworks.com/help/matlab/ref/mex.html>`_ is ready, run the following code in MATLAB

.. code-block:: matlab

    mex('-v', '-setup', 'Fortran'); mex('-v', fullfile(matlabroot, 'extern', 'examples', 'refbook', 'timestwo.F')); timestwo(1); delete('timestwo.mex*');

It will attempt to set up your MEX and then compile an `example provided by MathWorks <https://www.mathworks.com/help/matlab/matlab_external/create-fortran-source-mex-file.html>`_ for testing MEX on Fortran.
If this completes successfully, then your MEX is ready. Otherwise, it is not, and you may try https://github.com/equipez/setup_mex.

It will help you to set MEX up on Windows or macOS (the setup of MEX is trivial on Linux).
In case ``setup_mex`` does not work, you need to consult a local MATLAB expert or the technical support of MathWorks about "`how to set up MEX <https://www.mathworks.com/help/matlab/ref/mex.html>`_," which is not part of PDFO.

Installation
^^^^^^^^^^^^

Download and decompress the source code package.
You will obtain a folder containing ``setup.m``.
Place this folder at the location where you want PDFO to be installed.
In MATLAB, change the directory to this folder, and execute

.. code-block:: matlab

    setup

If this command runs successfully, PDFO is installed.
You may execute the following command in MATLAB to verify the installation

.. code-block:: matlab

    testpdfo
