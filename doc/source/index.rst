PDFO documentation
==================

.. toctree::
    :maxdepth: 1
    :hidden:

    User guide <user/index>
    Python API reference <python/index>

:Version: |version|
:Downloads: |total_downloads|
:Author of solvers: `M. J. D. Powell <https://www.zhangzk.net/powell.html>`_
:Authors of PDFO: `Tom M. Ragonneau <https://www.tomragonneau.com>`_ | `Zaikun Zhang <https://www.zhangzk.net>`_

PDFO is a cross-platform package providing the late `Professor M. J. D. Powell <https://www.zhangzk.net/powell.html>`_'s derivative-free (i.e., zeroth-order) optimization solvers.
Using only function values, but not derivatives, it solves problems of the form

.. math::

    \min_{x \in \R^n} \quad \obj ( x ) \quad \text{s.t.} \quad \left\{
    \begin{array}{l}
        \xl \le x \le \xu,\\
        \aub x \le \bub, ~ \aeq x = \beq,\\
        \cub ( x ) \le 0, ~ \ceq ( x ) = 0.
    \end{array} \right.

To install PDFO for Python, run

.. code-block:: bash

    pip install pdfo

You can also check the :ref:`installation guide for MATLAB<matlab-installation>`.
For more details, see the :ref:`user guide<user-guide>`.

Citing PDFO
-----------

If you would like to acknowledge the significance of PDFO in your research, we suggest citing the project as follows:

- T.\  M.\  Ragonneau and Z.\  Zhang. PDFO: a cross-platform package for Powell's derivative-free optimization solvers. arXiv:`2302.13246 [math.OC] <https://arxiv.org/abs/2302.13246>`_, 2023.

The corresponding BibTeX entry is given hereunder.

.. code-block:: bib

    @misc{pdfo,
        author       = {Ragonneau, T. M. and Zhang, Z.},
        title        = {{PDFO}: a cross-platform package for {Powell}'s derivative-free optimization solvers},
        howpublished = {arXiv:2302.13246 [math.OC]},
        year         = 2023,
    }

Statistics
----------

As of |today|, PDFO has been downloaded |total_downloads| times, including

- |github_downloads| times on `GitHub <https://github.com/pdfo/pdfo>`_,
- |pypi_downloads| times on `PyPI <https://pypi.org/project/pdfo/>`_ (`mirror downloads <https://pypistats.org/faqs>`_ excluded), and
- |conda_downloads| times on `Anaconda <https://anaconda.org/conda-forge/pdfo>`_.

Acknowledgments
---------------

PDFO is dedicated to the memory of the late `Professor M. J. D. Powell <https://www.zhangzk.net/powell.html>`_ with gratitude for his inspiration and for the treasures he left to us.
We are grateful to `Professor Ya-xiang Yuan <http://lsec.cc.ac.cn/~yyx/>`_ for his everlasting encouragement and support.

The development of PDFO is a long-term project, which would not be sustainable without the continued funds from the `Hong Kong Research Grants Council <https://www.ugc.edu.hk/eng/rgc/>`_ (ref. PolyU 253012/17P, PolyU 153054/20P, and PolyU 153066/21P), the `Hong Kong PhD Fellowship Scheme <https://cerg1.ugc.edu.hk/hkpfs/index.html>`_ (ref. PF18-24698), and `The Hong Kong Polytechnic University <https://www.polyu.edu.hk/>`_ (PolyU), in particular the `Department of Applied Mathematics <https://www.polyu.edu.hk/ama>`_ (AMA).
