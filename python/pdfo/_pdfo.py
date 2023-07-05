# -*- coding: utf-8 -*-
import numpy as np


def pdfo(fun, x0, args=(), method=None, bounds=None, constraints=(), options=None):
    r"""Powell's Derivative-Free Optimization solvers.

    PDFO is an interface to call Powell's derivatives-free optimization solvers:
    UOBYQA, NEWUOA, BOBYQA, LINCOA, and COBYLA. They are designed to minimize a
    scalar function of several variables subject to (possibly) simple bound
    constraints, linear constraints, and nonlinear constraints.

    Parameters
    ----------
    fun: callable
        Objective function to be minimized.

            ``fun(x, *args) -> float``

        where ``x`` is an array with shape (n,) and `args` is a tuple.
    x0: ndarray, shape (n,)
        Initial guess.
    args: tuple, optional
        Parameters of the objective function. For example,

            ``pdfo(fun, x0, args, ...)``

        is equivalent to

            ``pdfo(lambda x: fun(x, *args), x0, ...)``

    method: str, optional
        Name of the Powell method that will be used. By default, the most
        appropriate method will be chosen automatically. The available methods
        are: ``'uobyqa'``, ``'newuoa'``, ``'bobyqa'``, ``'lincoa'``, and
        ``'cobyla'``.
    bounds: {Bounds, ndarray, shape (n, 2)}, optional
        Bound constraints of the problem. It can be one of the cases below.

        #. An instance of `Bounds`.
        #. An ndarray with shape (n, 2). The bound constraint for x[i] is
           ``bounds[i, 0] <= x[i] <= bounds[i, 1]``. Set ``bounds[i, 0]`` to
           :math:`-\infty` or ``None`` if there is no lower bound, and set
           ``bounds[i, 1]`` to :math:`\infty` or ``None`` if there is no upper
           bound.

    constraints: {dict, LinearConstraint, NonlinearConstraint, list}, optional
        Constraints of the problem. It can be one of the cases below.

        #. A dictionary with fields:

            type: str
                Constraint type: ``'eq'`` for equality constraints and
                ``'ineq'`` for inequality constraints.
            fun: callable
                The constraint function.

            When ``type='eq'``, such a dictionary specifies an equality
            constraint ``fun(x) = 0``; when ``type='ineq'``, it specifies an
            inequality constraint ``fun(x) >= 0``.
        #. An instance of `LinearConstraint` or `NonlinearConstraint`.
        #. A list, each of whose elements is a dictionary described in 1, or an
           instance of `LinearConstraint` or `NonlinearConstraint`.

    options: dict, optional
        The options passed to the solver. It contains optionally:

            rhobeg: float, optional
                Initial value of the trust region radius, which should be a
                positive scalar. Typically, ``options['rhobeg']`` should be in
                the order of one tenth of the greatest expected change to a
                variable. By default, it is ``1`` if the problem is not scaled
                (but ``min(1, min(ub - lb) / 4)`` if the solver is BOBYQA),
                ``0.5`` if the problem is scaled.
            rhoend: float, optional
                Final value of the trust region radius, which should be a
                positive scalar. ``options['rhoend']`` should indicate the
                accuracy required in the final values of the variables.
                Moreover, ``options['rhoend']`` should be no more than
                ``options['rhobeg']`` and is by default ``1e-6``.
            maxfev: int, optional
                Upper bound of the number of calls of the objective function
                `fun`. Its value must be not less than ``options['npt'] + 1``.
                By default, it is ``500 * n``.
            npt: int, optional
                Number of interpolation points of each model used in Powell's
                Fortran code. It is used only if the solver is NEWUOA, BOBYQA,
                or LINCOA.
            ftarget: float, optional
                Target value of the objective function. If a feasible iterate
                achieves an objective function value lower or equal to
                ```options['ftarget']``, the algorithm stops immediately. By
                default, it is :math:`-\infty`.
            scale: bool, optional
                Whether to scale the problem according to the bound constraints.
                By default, it is ``False``. If the problem is to be scaled,
                then ``rhobeg`` and ``rhoend`` will be used as the initial and
                final trust region radii for the scaled problem.
            honour_x0: bool, optional
                Whether to respect the user-defined ``x0``. By default, it is
                ``False``. It is used only if the solver is BOBYQA.
            quiet: bool, optional
                Whether the interface is quiet. If it is set to ``True``, the
                output message will not be printed. This flag does not interfere
                with the warning and error printing.
            classical: bool, optional
                Whether to call the classical Powell code or not. It is not
                encouraged in production. By default, it is ``False``.
            eliminate_lin_eq: bool, optional
                Whether the linear equality constraints should be eliminated.
                By default, it is ``True``.
            debug: bool, optional
                Debugging flag. It is not encouraged in production. By default,
                it is ``False``.
            chkfunval: bool, optional
                Flag used when debugging. If both ``options['debug']`` and
                ``options['chkfunval']`` are ``True``, an extra
                function/constraint evaluation would be performed to check
                whether the returned values of objective function and constraint
                match the returned ``x``. By default, it is ``False``.

    Returns
    -------
    res: OptimizeResult
        The results of the solver. Check `OptimizeResult` for a description of
        the attributes.

    See also
    --------
    uobyqa : Unconstrained Optimization BY Quadratic Approximation.
    newuoa : NEW Unconstrained Optimization Algorithm.
    bobyqa : Bounded Optimization BY Quadratic Approximations.
    lincoa : LINearly Constrained Optimization Algorithm.
    cobyla : Constrained Optimization BY Linear Approximations.

    References
    ----------
    .. [1] T. M. Ragonneau and Z. Zhang. PDFO: a cross-platform package for
       Powell's derivative-free optimization solvers.
       arXiv:`2302.13246 [math.OC] <https://arxiv.org/abs/2302.13246>`_, 2023.


    Examples
    --------
    The following example shows how to solve a simple constrained optimization
    problem. The problem considered below should be solved with a
    derivative-based method. It is used here only as an illustration.

    We consider the 2-dimensional problem

    .. math::

        \min_{x, y \in \R} \quad x^2 + y^2 \quad \text{s.t.} \quad \left\{
        \begin{array}{l}
            0 \le x \le 2,\\
            1 / 2 \le y \le 3,\\
            0 \le x + y \le 1,\\
            x^2 - y \le 0.
        \end{array} \right.

    We solve this problem using `pdfo` starting from the initial guess
    :math:`(x_0, y_0) = (0, 1)` with at most 200 function evaluations.

    .. testsetup::

        import numpy as np
        np.set_printoptions(precision=1, suppress=True)

    >>> from pdfo import Bounds, LinearConstraint, NonlinearConstraint, pdfo
    >>> bounds = Bounds([0, 0.5], [2, 3])
    >>> linear_constraints = LinearConstraint([1, 1], 0, 1)
    >>> nonlinear_constraints = NonlinearConstraint(lambda x: x[0]**2 - x[1], None, 0)
    >>> options = {'maxfev': 200}
    >>> res = pdfo(lambda x: x[0]**2 + x[1]**2, [0, 1], bounds=bounds, constraints=[linear_constraints, nonlinear_constraints], options=options)
    >>> res.x
    array([0. , 0.5])
    """
    from ._dependencies import prepdfo, postpdfo

    # A cell that records all the warnings.
    output = dict()
    output['warnings'] = []

    # Preprocess the inputs.
    fun_c, x0_c, bounds_c, constraints_c, options_c, method, prob_info = \
        prepdfo(fun, x0, args, method, bounds, constraints, options)

    if prob_info['infeasible']:
        # The problem turned out infeasible during prepdfo.
        exitflag = -4
        nf = 1
        x = x0_c
        fx = fun_c(x)
        fhist = np.array([fx], dtype=np.float64)
        constrviolation = prob_info['constrv_x0']
        chist = np.array([constrviolation], dtype=np.float64)
        output['constr_value'] = prob_info['nlc_x0']
        output['constr_modified'] = False
    elif prob_info['nofreex']:
        # x was fixed by the bound constraints during prepdfo.
        exitflag = 13
        nf = 1
        x = prob_info['fixedx_value']
        fx = fun_c(x)
        fhist = np.array([fx], dtype=np.float64)
        constrviolation = prob_info['constrv_fixedx']
        chist = np.array([constrviolation], dtype=np.float64)
        output['constr_value'] = prob_info['nlc_fixedx']
        output['constr_modified'] = False
    elif prob_info['feasibility_problem'] and prob_info['refined_type'] != 'nonlinearly-constrained':
        # We could set fx=[], funcCount=0, and fhist=[] since no function evaluation occurred. But then we will have to
        # modify the validation of fx, funcCount, and fhist in postpdfo. To avoid such a modification, we set fx,
        # funcCount, and fhist as below and then revise them in postpdfo.
        nf = 1
        x = x0_c  # prepdfo has tried to set x0 to a feasible point (but may have failed)
        fx = fun_c(x)
        fhist = np.array([fx], dtype=np.float64)
        constrviolation = prob_info['constrv_x0']
        chist = np.array([constrviolation], dtype=np.float64)
        output['constr_value'] = np.asarray([], dtype=np.float64)
        if constrviolation < np.finfo(np.float64).eps:
            # Did prepdfo find a feasible point?
            exitflag = 14
        else:
            exitflag = 15
        output['constr_modified'] = False
    else:
        # The problem turns out 'normal' during prepdfo.
        lower_method = method.lower()
        try:
            if lower_method == 'uobyqa':
                from . import uobyqa
                opti_res = uobyqa(fun_c, x0_c, options=options_c)
            elif lower_method == 'newuoa':
                from . import newuoa
                opti_res = newuoa(fun_c, x0_c, options=options_c)
            elif lower_method == 'bobyqa':
                from . import bobyqa
                opti_res = bobyqa(fun_c, x0_c, bounds=bounds_c, options=options_c)
            elif lower_method == 'lincoa':
                from . import lincoa
                opti_res = lincoa(fun_c, x0_c, bounds=bounds_c, constraints=constraints_c, options=options_c)
            elif lower_method == 'cobyla':
                from . import cobyla
                opti_res = cobyla(fun_c, x0_c, bounds=bounds_c, constraints=constraints_c, options=options_c)
        except ImportError:
            from ._dependencies import import_error_so
            import_error_so(lower_method)

        # Extract the output from the solvers. The output is extended with the possible outputs returned by some
        # specific solvers (like the nonlinear constraint nlc for COBYLA).
        x = opti_res.x
        fx = opti_res.fun
        exitflag = opti_res.status
        nf = opti_res.nfev
        fhist = opti_res.fhist
        try:
            constrviolation = opti_res.constrviolation
        except AttributeError:
            constrviolation = 0
        try:
            chist = opti_res.chist
        except AttributeError:
            chist = None
        try:
            output['constr_value'] = opti_res.constr_value
        except AttributeError:
            pass
        try:
            output['constr_modified'] = opti_res.constr_modified
        except AttributeError:
            pass

        # The warnings that have been raised in the solvers and treated during their own calls to postpdfo should be
        # transfer to the call to postpdfo of pdfo to appear to the output of pdfo.
        output['warnings'].extend(opti_res.warnings)

    # Postprocess the result.
    return postpdfo(x, fx, exitflag, output, method, nf, fhist, options_c, prob_info, constrviolation, chist)
