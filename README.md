<h1 align="center">
PDFO: Powell's Derivative-Free Optimization solvers
</h1>

 **[Introduction](??) | [Python](??) | [MATLAB](??) | [Citing PDFO](??) | [Acknowledgments](??)** (Make this centerd)

Dedicated to the late Professor [M. J. D. Powell](https://www.zhangzk.net/powell.html) 
FRS (1936&ndash;2015). (Make this centerd?)

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/pdfo/pdfo/build.yml?logo=github&style=for-the-badge)](https://github.com/pdfo/pdfo/actions/workflows/build.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/pdfo/pdfo?logo=github&style=for-the-badge)](https://github.com/pdfo/pdfo/)
[![GitHub](https://img.shields.io/github/license/pdfo/pdfo?logo=github&style=for-the-badge)](https://opensource.org/licenses/BSD-3-Clause/)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/pdfo/pdfo?logo=github&style=for-the-badge)](https://github.com/pdfo/pdfo/releases/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pdfo?logo=pypi&style=for-the-badge)](https://pypi.org/project/pdfo/)
[![View PDFO: Powell's Derivative-Free Optimization solvers on File Exchange](https://img.shields.io/badge/MATLAB-File_Exchange-orange?style=for-the-badge)](https://www.mathworks.com/matlabcentral/fileexchange/75195-pdfo-powell-s-derivative-free-optimization-solvers/)




## Introduction

PDFO (Powell's Derivative-Free Optimization solvers) is a cross-platform package
providing interfaces for using the late Professor [M. J. D. Powell's](https://www.zhangzk.net/powell.html)
derivative-free optimization solvers, including UOBYQA, NEWUOA, BOBYQA, LINCOA,
and COBYLA. See the [PDFO homepage](https://www.pdfo.net) and the [PDFO paper](??) for more information.

This package makes use of a modified version of [Powell's](https://www.zhangzk.net/powell.html)
Fortran code. See the folder [`original`](https://github.com/pdfo/pdfo/tree/main/fsrc/original)
under `fsrc` for [Powell's](https://www.zhangzk.net/powell.html) original code.

## Python version of PDFO

### Installation

#### Recommended installation

To use the Python version of PDFO on Linux, Mac, or Windows, you need
[Python](https://www.python.org/) (version 3.7 or above).

It is highly recommended to install PDFO via [PyPI](https://pypi.org).

Install [pip](https://pip.pypa.io/en/stable/installing/) in your system if
you Python version does not include it. Then execute

```bash
python3 -m pip install pdfo
```

in a command shell (e.g., the terminal for Linux and macOS, or the Command
Shell for Windows). If your Python 3 launcher is not `python3`, adapt the
command accordingly (it may be `python` on Windows for example). If this
command runs successfully, PDFO is installed. You may verify the
installation by

```bash
python3 -m unittest pdfo.testpdfo
```

If you are an Anaconda user, PDFO is also available through the conda installer
( https://anaconda.org/conda-forge/pdfo ). However, it is not managed by us.

#### Alternative installation (using source distribution)

Alternatively, although deeply discouraged, PDFO can be installed from the
source code. It requires you to install additional Python headers, a Fortran
compiler (e.g., [gfortran](https://gcc.gnu.org/fortran/)), and
[F2PY](https://numpy.org/doc/stable/f2py/) (provided by
[NumPy](https://numpy.org/)). Download and decompress the source code package;
you will obtain a folder containing `pyproject.toml`; in a command shell,
change your directory to this folder; then install PDFO by executing

```bash
python3 -m pip install .
```

### Usage

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

### Uninstall

PDFO can be uninstalled by executing the following command in a command shell:

```bash
python3 -m pip uninstall pdfo
```

## MATLAB version of PDFO

### Prerequisites

PDFO supports MATLAB R2014a and later releases. To use PDFO, you need first
set up the [MEX](https://www.mathworks.com/help/matlab/ref/mex.html) of your
MATLAB so that it can compile Fortran.
**The setup of MEX is a pure MATLAB usage problem and it has nothing to do with PDFO.**

To see whether your MEX is ready, run the following code in MATLAB:

```matlab
mex('-setup', '-v', 'fortran'); mex('-v', fullfile(matlabroot, 'extern', 'examples', 'refbook', 'timestwo.F'));
```

If this completes successfully, then your MEX is ready. Otherwise, it is not, and
you may try the [`setup_mex` package](https://github.com/equipez/setup_mex) at
```
https://github.com/equipez/setup_mex
```
It will help you to set MEX up on Windows or macOS (the setup of MEX is trivial on Linux).
In case `setup_mex` does not work, you need to consult a local MATLAB expert or the technical support of
MathWorks about "[how to set up MEX](https://www.mathworks.com/help/matlab/ref/mex.html)", which is
**not** part of PDFO.

### Installation

Download and decompress the [source code package](https://www.pdfo.net/docs.html#download),
or clone it from [GitHub](https://github.com/pdfo/pdfo) or [Gitee](https://gitee.com/pdfo/pdfo).
You will obtain a folder containing `setup.m`. Place this folder at the location
where you  want PDFO to be installed. In MATLAB, change the directory to this
folder, and execute the following command:

```matlab
setup
```

If this command runs successfully, PDFO is installed. You may execute the
following command in MATLAB to verify the installation:

```matlab
testpdfo
```

### Usage

PDFO provides the following MATLAB functions:
`pdfo`, `uobyqa`, `newuoa`, `bobyqa`, `lincoa`, `cobyla`.

The `pdfo` function can automatically identify the type of your problem
and then call one of [Powell's](https://www.zhangzk.net/powell.html) solvers.
The other five functions call the solver indicated by their names. It is highly
recommended using `pdfo` instead of `uobyqa`, `newuoa`, etc.

The `pdfo` function is designed to be compatible with the `fmincon`
function available in the [Optimization Toolbox](https://www.mathworks.com/products/optimization.html)
of MATLAB. You can call `pdfo` in exactly the same way as calling `fmincon`. In
addition, `pdfo` can be  called in some flexible ways that are not supported by
`fmincon`.

For detailed syntax of these functions, use the standard `help` command
of MATLAB. For example,

```matlab
help pdfo
```

will tell you how to use `pdfo`.

### Uninstall

PDFO can be uninstalled using the setup.m script by executing the following
command in MATLAB:

```matlab
setup uninstall
```

## Acknowledgments

PDFO is dedicated to the memory of the late Professor [Powell](https://www.zhangzk.net/powell.html)
with gratitude for his inspiration and for the treasures he left to us.

We are grateful to Professor [Ya-xiang Yuan](http://lsec.cc.ac.cn/~yyx/) for his
everlasting encouragement and support.

The development of PDFO is a long-term project, which would not be sustainable without the continued
funds from the [Hong Kong Research Grants Council](https://www.ugc.edu.hk/eng/rgc)
(ref. PolyU 253012/17P, PolyU 153054/20P, and PolyU 153066/21P),
the [Hong Kong Ph.D. Fellowship Scheme](https://cerg1.ugc.edu.hk/hkpfs) (ref. PF18-24698),
and the [Hong Kong Polytechnic University](https://www.polyu.edu.hk) (PolyU),
in particular the [Department of Applied Mathematics](https://www.polyu.edu.hk/ama) (AMA).

## Citing PDFO

### Citing the PDFO package

T. M. Ragonneau and Z. Zhang, <a href="https://arxiv.org/pdf/2302.13246.pdf">PDFO: a cross-platform package for Powell's derivative-free optimization solvers</a>, arXiv:2302.13246, 2023 [BibTeX]

### Citing Powell’s methods

<details>
    <summary>M. J. D. Powell. A direct search optimization method that models the objective and constraint functions by linear interpolation. In S. Gomez and J. P. Hennart, editors, <i>Advances in Optimization and Numerical Analysis</i>, pages 51–67, Dordrecht, NL, 1994. Springer.</summary>
    <pre>@inproceedings{Powell_1994,
    title        = {A direct search optimization method that models the objective and constraint functions by linear interpolation},
    author       = {Powell, M. J. D.},
    booktitle    = {Advances in Optimization and Numerical Analysis},
    editor       = {Gomez, S. and Hennart, J. P.},
    publisher    = {Springer},
    address      = {Dordrecht, NL},
    pages        = {51--67},
    year         = 1994,
}</pre>
</details>  \[[BibTeX]\]


<br/>

<details>
    <summary>M. J. D. Powell. UOBYQA: unconstrained optimization by quadratic approximation. <i>Math. Program.</i>, 92:555–582, 2002.</summary>
    <pre>@article{Powell_2002,
    title        = {{UOBYQA}: unconstrained optimization by quadratic approximation},
    author       = {Powell, M. J. D.},
    journal      = {Math. Program.},
    volume       = 92,
    pages        = {555--582},
    year         = 2002,
}</pre>
</details>  \[[BibTeX]\]


<br/>

<details>
    <summary>M. J. D. Powell. The NEWUOA software for unconstrained optimization without derivatives. In G. Di Pillo and M. Roma, editors, <i>Large-Scale Nonlinear Optimization</i>, volume 83 of <i>Nonconvex Optimization and Its Applications</i>, pages 255–297, Boston, MA, USA, 2006. Springer.</summary>
    <pre>@inproceedings{Powell_2006,
    title        = {The {NEWUOA} software for unconstrained optimization without derivatives},
    author       = {Powell, M. J. D.},
    booktitle    = {Large-Scale Nonlinear Optimization},
    editor       = {{Di Pillo}, G. and Roma, M.},
    publisher    = {Springer},
    address      = {Boston, MA, USA},
    series       = {Nonconvex Optimization and Its Applications},
    volume       = 83,
    pages        = {255--297},
    year         = 2006,
}</pre>
</details>  \[[BibTeX]\]


<br/>

<details>
    <summary>M. J. D. Powell. The BOBYQA algorithm for bound constrained optimization without derivatives. Technical Report DAMTP 2009/NA06, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge, UK, 2009.</summary>
    <pre>@techreport{Powell_2009,
    title        = {The {BOBYQA} algorithm for bound constrained optimization without derivatives},
    author       = {Powell, M. J. D.},
    institution  = {Department of Applied Mathematics and Theoretical Physics, University of Cambridge},
    address      = {Cambridge, UK},
    number       = {DAMTP 2009/NA06},
    year         = 2009,
}</pre>
</details>  \[[BibTeX]\]

<br/>

**Remark:** LINCOA seeks the least value of a nonlinear function subject to
linear inequality constraints without using derivatives of the objective
function. Powell did not publish a paper to introduce the algorithm.
