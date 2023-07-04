Issues and bugs
===============

During the development of PDFO, some issues have occurred.
We keep below a list of the most important one.

In case of problems or bugs when using PDFO, you may open a `new issue <https://github.com/pdfo/pdfo/issues>`_ on GitHub.

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Date
     - Description
     - Status/Solution
   * - August 23, 2021
     - Python users of version 1.0 and below needed to install manually some dependencies, e.g., Python headers and a Fortran compiler.
     - Starting from version 1.1, wheel distributions are available on `PyPI <https://pypi.org/project/pdfo/#files>`_ for Windows, Linux, and macOS. The wheel distributions are generated automatically using `GitHub Actions <https://github.com/pdfo/pdfo/actions>`_. Users do not need to handle the dependencies anymore as long as they install PDFO via `PyPI <https://pypi.org/project/pdfo/#files>`_ with Python 3.7 or above.
   * - June 15, 2020
     - Version 1.0 of PDFO could not be installed on Windows for Python 3.8 and above, because the most recent version of `Intel Distribution for Python <https://software.intel.com/content/www/us/en/develop/tools/distribution-for-python.html>`_ supports only Python 3.7.
     - The latest versions of Python are supported on Windows by version 1.1 and above.
   * - April 19, 2020
     - Version 0.9 does not support 64-bit Python on Windows because F2PY does not work well with MinGW-w64.
     - 64-bit Python is supported by version 1.0 and above on Windows.
