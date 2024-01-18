Citation
========

If you would like to acknowledge the significance of PDFO in your research, we suggest citing the project as follows:

- T.\  M.\  Ragonneau and Z.\  Zhang. "PDFO: a cross-platform package for Powell's derivative-free optimization solvers." 2023. DOI: `10.48550/arXiv.2302.13246 <https://doi.org/10.48550/arXiv.2302.13246>`_. arXiv: `2302.13246 [math.OC] <https://arxiv.org/abs/2302.13246>`_.

The corresponding BibTeX entry is given hereunder.

.. code-block:: bib

    @unpublished{pdfo,
        author       = {Ragonneau, T. M. and Zhang, Z.},
        title        = {{PDFO}: a cross-platform package for {P}owell's derivative-free optimization solvers},
        eprint       = {2302.13246},
        eprinttype   = {arxiv},
        eprintclass  = {math.OC},
        year         = 2023,
        doi          = {10.48550/arXiv.2302.13246},
    }

In addition, we provide below a list of references closely related to PDFO.

#. M.\  J.\  D.\  Powell. A direct search optimization method that models the objective and constraint functions by linear interpolation. In S. Gomez and J. P. Hennart, editors, *Advances in Optimization and Numerical Analysis*, 51--67. Springer, 1994.
#. M.\  J.\  D.\  Powell. UOBYQA: unconstrained optimization by quadratic approximation. *Math. Program.*, 92:555--582, 2002.
#. M.\  J.\  D.\  Powell. Least Frobenius norm updating of quadratic models that satisfy interpolation conditions. *Math. Program.*, 100:183--215, 2004.
#. M.\  J.\  D.\  Powell. On the use of quadratic models in unconstrained minimization without derivatives. *Optim. Methods Softw.*, 19:399--411, 2004.
#. M.\  J.\  D.\  Powell. On updating the inverse of a KKT matrix. In Y. Yuan, editor, *Numerical Linear Algebra and Optimization*, 56--78. Science Press, 2004.
#. M.\  J.\  D.\  Powell. The NEWUOA software for unconstrained optimization without derivatives. In G. Di Pillo and M. Roma, editors, *Large-Scale Nonlinear Optimization*, volume 83 of Nonconvex Optimization and Its Applications, 255--297. Springer, 2006.
#. M.\  J.\  D.\  Powell. A view of algorithms for optimization without derivatives. Technical Report DAMTP 2007/NA63, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, 2007.
#. M.\  J.\  D.\  Powell. Developments of NEWUOA for minimization without derivatives. *IMA J. Numer. Anal.*, 28:649--664, 2008.
#. M.\  J.\  D.\  Powell. The BOBYQA algorithm for bound constrained optimization without derivatives. Technical Report DAMTP 2009/NA06, Department of Applied Mathematics and Theoretical Physics, University of Cambridge, 2009.
#. M.\  J.\  D.\  Powell. On fast trust region methods for quadratic models with linear constraints. *Math. Program. Comput.*, 7:237--267, 2015.
#. T.\  M.\  Ragonneau. *Model-Based Derivative-Free Optimization Methods and Software*, Chapter 3. PhD thesis, The Hong Kong Polytechnic University, Hong Kong, China, 2022.
#. Z.\  Zhang, PRIMA: Reference Implementation for Powell's Methods with Modernization and Amelioration, available at http://www.libprima.net, 2023.

**Remarks**

#. A key technique underlying the success of NEWUOA, BOBYQA, and LINCOA is the least Frobenius norm updating of quadratic models elaborated in [3] and [4].
   The idea comes from the `least change update <https://www.jstor.org/stable/2030103?seq=1>`_ for `quasi-Newton methods <https://epubs.siam.org/doi/abs/10.1137/1019005>`_, a vast research area initiated by the `DFP algorithm <https://academic.oup.com/comjnl/article/6/2/163/364776>`_, where P stands for Powell.
#. The least Frobenius norm updating is a quadratic programming problem, whose constraints correspond to the interpolation conditions.
   At each iteration of Powell's algorithms, only one of the constraints is different from the previous iteration.
   To solve this problem efficiently and stably, Powell designed a procedure to update the inverse of its KKT matrix along the iterations.
   Such a procedure is detailed in [5], and it is indispensable for the remarkable numerical stability of NEWUOA, BOBYQA, and LINCOA.
#. LINCOA seeks the least value of a nonlinear function subject to linear inequality constraints without using derivatives of the objective function.
   Professor Powell did not publish a paper to introduce the algorithm.
   The paper [10] discusses how LINCOA solves its trust-region subproblems.
#. Different from PDFO, which provides interfaces for Powell's code, [12] provides the modernized reference implementation for Powell's methods.
