# PDFO: Powell's Derivative-Free Optimization solvers

[![wheels](https://github.com/pdfo/pdfo/actions/workflows/build.yml/badge.svg)](https://github.com/pdfo/pdfo/actions/workflows/build.yml)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![pypi](https://img.shields.io/pypi/v/pdfo)](https://pypi.org/project/pdfo/)
[![download](https://img.shields.io/pypi/dm/pdfo?label=pypi%20downloads)](https://pypi.org/project/pdfo/)
[![View PDFO: Powell's Derivative-Free Optimization solvers on File Exchange](https://www.mathworks.com/matlabcentral/images/matlab-file-exchange.svg)](https://www.mathworks.com/matlabcentral/fileexchange/75195-pdfo-powell-s-derivative-free-optimization-solvers)

Dedicated to the late Professor [M. J. D. Powell](https://www.zhangzk.net/powell.html)
FRS (1936&ndash;2015).

## Getting started

PDFO (Powell's Derivative-Free Optimization solvers) is a cross-platform package
providing interfaces for using the late Professor [M. J. D. Powell's](https://www.zhangzk.net/powell.html)
derivative-free optimization solvers, including UOBYQA, NEWUOA, BOBYQA, LINCOA,
and COBYLA. See https://www.pdfo.net for more information.

- To use the MATLAB version of PDFO, see [README_mat.md](https://github.com/pdfo/pdfo/blob/main/README_mat.md).
- To use the Python version of PDFO, see [README_py.md](https://github.com/pdfo/pdfo/blob/main/README_py.md).

This package makes use of a modified version of [Powell's](https://www.zhangzk.net/powell.html)
Fortran code. See the folder [`original`](https://github.com/pdfo/pdfo/tree/main/fsrc/original)
under `fsrc` for [Powell's](https://www.zhangzk.net/powell.html) original code.

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
