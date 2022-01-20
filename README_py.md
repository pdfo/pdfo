# PDFO for Python: Powell's Derivative-Free Optimization solvers

Dedicated to late Professor [M. J. D. Powell](https://www.zhangzk.net/powell.html)
FRS (1936&ndash;2015).

We look forward to your feedback! Thank you very much!

This is the README for the Python version of PDFO.
See https://www.pdfo.net for more information.

## Installation

### Recommended installation

To use the Python version of PDFO on Linux, Mac, or Windows, you need
[Python](https://www.python.org/) (version 3.7 or above).

It is highly recommended to install PDFO via [PyPI](https://pypi.org).

Install [pip](https://pip.pypa.io/en/stable/installing/) in your system if
you Python version does not incude it. Then execute

```bash
python -m pip install pdfo
```

in a command shell (e.g., the terminal for Linux and macOS, or the Command
Shell for Windows). If your Python launcher is not python, adapt the command
accordingly. If this command runs successfully, PDFO is installed. You may
verify the installation by

```bash
python -m unittest pdfo.testpdfo
```

If you are an Anaconda user, PDFO is also available through the conda installer
( https://anaconda.org/conda-forge/pdfo ). However, it is not managed by us.

### Alternative installation (using source distribution)

Alternatively, although deeply discouraged, PDFO can be installed from the
source code. It requires you to install additional Python headers, a Fortran
compiler (e.g., [gfortran](https://gcc.gnu.org/fortran/)), and
[F2PY](https://numpy.org/doc/stable/f2py/) (provided by
[NumPy](https://numpy.org/)). Download and decompress the source code package;
you will obtain a folder containing `setup.py`; in a command shell, change your
directory to this folder; then install PDFO by executing

```bash
python -m pip install ./
```

## Usage

PDFO provides the following Python functions:
`pdfo`, `uobyqa`, `newuoa`, `bobyqa`, `lincoa`, `cobyla`.

The `pdfo` function can automatically identify the type of your problem
and call one of [Powell's](https://www.zhangzk.net/powell.html) solvers. The
other five functions call the solver indicated by their names. It is highly
recommended using `pdfo` instead of `uobyqa`, `newuoa`, etc.

The `pdfo` function is designed to be compatible with the `minimize`
function available in [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html).
You can call `pdfo` in exactly the same way as calling `minimize`, without the
derivative arguments (PDFO does not use derivatives).

For the detailed syntax of these functions, use the standard `help` command
of Python. For example,

```python
from pdfo import pdfo
help(pdfo)
```

will tell you how to use `pdfo`.

## Uninstall

PDFO can be uninstalled by executing the following command in a command shell:

```bash
python -m pip uninstall pdfo
```

## References

[1] M. J. D. Powell, A direct search optimization method that models the
objective and constraint functions by linear interpolation, In Advances
in Optimization and Numerical Analysis, eds. S. Gomez and J. P. Hennart,
pages 51&ndash;67, Springer Verlag, Dordrecht, Netherlands, 1994

[2] M. J. D. Powell, UOBYQA: unconstrained optimization by quadratic
approximation, Math. Program., 92(B):555&ndash;582, 2002

[3] M. J. D. Powell, The NEWUOA software for unconstrained optimization
without derivatives, In Large-Scale Nonlinear Optimization, eds. G. Di Pillo
and M. Roma, pages 255&ndash;297, Springer, New York, US, 2006

[4] M. J. D. Powell, The BOBYQA algorithm for bound constrained
optimization without derivatives, Technical Report DAMTP 2009/NA06,
Department of Applied Mathematics and Theoretical Physics, Cambridge
University, Cambridge, UK, 2009

*Remark:* LINCOA seeks the least value of a nonlinear function subject to
linear inequality constraints without using derivatives of the objective
function. Powell did not publish a paper to introduce the algorithm.
