PDFO documentation
==================

.. toctree::
    :maxdepth: 1
    :hidden:

    User guide <user/index>
    Python API reference <python/index>

:Version: |version|
:Useful links: `Issue tracker <https://github.com/pdfo/pdfo/issues>`_ | `Email <mailto:pdfocode@gmail.com>`_

PDFO is a cross-platform package providing Python and MATLAB interfaces for using the late Professor M. J. D. Powell's derivative-free optimization solvers.
It aims at solving problems of the form

.. math::

    \min_{x \in \R^n} \quad \obj ( x ) \quad \text{s.t.} \quad \left\{
    \begin{array}{l}
        \xl \le x \le \xu,\\
        \aub x \le \bub, ~ \aeq x = \beq,\\
        \cub ( x ) \le 0, ~ \ceq ( x ) = 0,
    \end{array} \right.

where :math:`\obj` is a real-valued objective function, :math:`\xl` and :math:`\xu` are lower and upper bounds, :math:`\aub`, :math:`\aeq`, :math:`\bub`, and :math:`\beq` formulates linear constraints, and :math:`\cub` and :math:`\ceq` are vector-valued constraint functions.
PDFO uses function values of :math:`\obj`, :math:`\cub`, and :math:`\ceq`, but no derivatives.

.. grid:: 1 2 2 3

    .. grid-item-card::
        :img-top: ../source/_static/fontawesome-free-6.4.0-desktop/svgs/solid/download.svg

        Installation
        ^^^^^^^^^^^^

        Installation manual.

        .. button-ref:: user/installation
            :expand:
            :color: secondary
            :click-parent:

            To the installation

    .. grid-item-card::
        :img-top: ../source/_static/fontawesome-free-6.4.0-desktop/svgs/solid/users.svg

        Usage
        ^^^^^

        Usage and examples.

        .. button-ref:: user/usage
            :expand:
            :color: secondary
            :click-parent:

            To the usage

    .. grid-item-card::
        :img-top: ../source/_static/fontawesome-free-6.4.0-desktop/svgs/solid/code-branch.svg

        Releases
        ^^^^^^^^

        Release notes.

        .. button-ref:: user/releases
            :expand:
            :color: secondary
            :click-parent:

            To the releases

    .. grid-item-card::
        :img-top: ../source/_static/fontawesome-free-6.4.0-desktop/svgs/solid/screwdriver-wrench.svg

        Issues
        ^^^^^^

        Issues and bugs.

        .. button-ref:: user/issues
            :expand:
            :color: secondary
            :click-parent:

            To the issues

    .. grid-item-card::
        :img-top: ../source/_static/fontawesome-free-6.4.0-desktop/svgs/solid/book.svg

        References
        ^^^^^^^^^^

        Related publications.

        .. button-ref:: user/references
            :expand:
            :color: secondary
            :click-parent:

            To the references

    .. grid-item-card::
        :img-top: ../source/_static/fontawesome-free-6.4.0-desktop/svgs/solid/scale-balanced.svg

        License
        ^^^^^^^

        License information.

        .. button-ref:: license
            :expand:
            :color: secondary
            :click-parent:

            To the license

.. note::

    As of |today|, PDFO has been downloaded

    - X times on `GitHub <https://github.com/pdfo/pdfo>`_,
    - Y times on `PyPI <https://pypi.org/project/pdfo/>`_ (`mirror downloads <https://pypistats.org/faqs>`_ excluded), and
    - Z times on `Anaconda <https://anaconda.org/conda-forge/pdfo>`_.

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

Acknowledgments
---------------

PDFO is dedicated to the memory of the late `Professor Powell <https://www.zhangzk.net/powell.html>`_ with gratitude for his inspiration and for the treasures he left to us.
We are grateful to `Professor Ya-xiang Yuan <http://lsec.cc.ac.cn/~yyx/>`_ for his everlasting encouragement and support.

The development of PDFO is a long-term project, which would not be sustainable without the continued funds from the `Hong Kong Research Grants Council <https://www.ugc.edu.hk/eng/rgc/>`_ (ref. PolyU 253012/17P, PolyU 153054/20P, and PolyU 153066/21P), the `Hong Kong PhD Fellowship Scheme <https://cerg1.ugc.edu.hk/hkpfs/index.html>`_ (ref. PF18-24698), and `The Hong Kong Polytechnic University <https://www.polyu.edu.hk/>`_ (PolyU), in particular the `Department of Applied Mathematics <https://www.polyu.edu.hk/ama>`_ (AMA).
