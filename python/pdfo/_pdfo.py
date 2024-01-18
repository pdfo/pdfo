# -*- coding: utf-8 -*-
import numpy as np


def pdfo(fun, x0, args=(), method=None, bounds=None, constraints=(), options=None):
    r"""Powell's Derivative-Free Optimization solvers.

    PDFO is an interface to call Powell's derivatives-free optimization solvers:
    UOBYQA, NEWUOA, BOBYQA, LINCOA, and COBYLA. They are designed to minimize a
    scalar function of several variables subject to (possibly) bound
    constraints, linear constraints, and nonlinear constraints.

    .. attention::

        This function does not accept any 'solver' options. If you want to
        specify which solver to use, please use the `method` argument.

    Parameters
    ----------
    fun : callable
        Objective function to be minimized.

            ``fun(x, *args) -> float``

        where ``x`` is an array with shape (n,) and `args` is a tuple.
    x0 : array_like, shape (n,)
        Initial guess.
    args : tuple, optional
        Extra arguments of the objective function. For example,

            ``pdfo(fun, x0, args, ...)``

        is equivalent to

            ``pdfo(lambda x: fun(x, *args), x0, ...)``

    method : {'uobyqa', 'newuoa', 'bobyqa', 'lincoa', 'cobyla'}, optional
        Name of the Powell method that will be used. By default, 'uobyqa'
        is selected if the problem is unconstrained with ``2 <= n <= 8``,
        'newuoa' is selected if the problem is unconstrained with ``n = 1``
        or ``n >= 9``, 'bobyqa' is selected if the problem is
        bound-constrained, 'lincoa' is selected if the problem is linearly
        constrained, and 'cobyla' is selected otherwise.
    bounds : {`scipy.optimize.Bounds`, array_like, shape (n, 2)}, optional
        Bound constraints of the problem. It can be one of the cases below.

        #. An instance of `scipy.optimize.Bounds`.
        #. An array with shape (n, 2). The bound constraints for ``x[i]`` are
           ``bounds[i, 0] <= x[i] <= bounds[i, 1]``. Set ``bounds[i, 0]`` to
           :math:`-\infty` if there is no lower bound, and set ``bounds[i, 1]``
           to :math:`\infty` if there is no upper bound.

    constraints : {dict, `scipy.optimize.LinearConstraint`, `scipy.optimize.NonlinearConstraint`, list}, optional
        Constraints of the problem. It can be one of the cases below.

        #. A dictionary with fields:

            type : {'eq', 'ineq'}
                Whether the constraint is ``fun(x) = 0`` or ``fun(x) >= 0``.
            fun : callable
                Constraint function.

        #. An instance of `scipy.optimize.LinearConstraint`.
        #. An instance of `scipy.optimize.NonlinearConstraint`.
        #. A list, each of whose elements are described in 1, 2, and 3.

    options : dict, optional
        The options passed to the solver. Accepted options are:

            radius_init : float, optional
                Initial value of the trust-region radius. Typically, it should
                be in the order of one tenth of the greatest expected change to
                the variables.
            radius_final : float, optional
                Final value of the trust-region radius. It must be smaller than
                or equal to ``options['radius_init']`` and should indicate the
                accuracy required in the final values of the variables.
            maxfev : int, optional
                Maximum number of function evaluations.
            ftarget : float, optional
                Target value of the objective function. The optimization
                procedure is terminated when the objective function value of a
                nearly feasible point is less than or equal to this target.
            npt : int, optional
                Number of interpolation points for NEWUOA, BOBYQA, and LINCOA.
            quiet: bool, optional
                Whether to suppress the output messages.
            scale : bool, optional
                Whether to scale the problem according to the bound constraints.
            eliminate_lin_eq : bool, optional
                Whether to eliminate linear equality constraints.
            honour_x0 : bool, optional
                Whether to honour the initial guess. It is only used by BOBYQA.
            classical : bool, optional
                Whether to use the classical version of Powell's methods. It is
                highly discouraged in production.
            debug : bool, optional
                Whether to perform debugging checks. It is highly discouraged in
                production.
            chkfunval : bool, optional
                Whether to check the value of the objective and constraint
                functions at the solution. This is only done in the debug mode,
                and requires one extra function evaluation. It is highly
                discouraged in production.

    Returns
    -------
    res : `scipy.optimize.OptimizeResult`
        Result of the optimization procedure, with the following fields:

            message : str
                Description of the exit status specified in the ``status``
                field (i.e., the cause of the termination of the solver).
            success : bool
                Whether the optimization procedure terminated successfully.
            status : int
                Termination status of the optimization procedure.
            fun : float
                Objective function value at the solution point.
            x : `numpy.ndarray`, shape (n,)
                Solution point.
            nfev : int
                Number of function evaluations.
            fun_history : `numpy.ndarray`, shape (nfev,)
                History of the objective function values.
            method : str
                Name of the Powell method used.

        For constrained problems, the following fields are also returned:

            maxcv : float
                Maximum constraint violation at the solution point.
            maxcv_history : `numpy.ndarray`, shape (nfev,)
                History of the maximum constraint violation.

        For linearly and nonlinearly constrained problems, the following field
        is also returned:

            constraints : {`numpy.ndarray`, list}
                The values of the constraints at the solution point. If a single
                constraint is passed, i.e., if the `constraints` argument is
                either a dict, a `scipy.optimize.LinearConstraint`, or a
                `scipy.optimize.NonlinearConstraint`, then the returned value is
                a `numpy.ndarray`, which is the value of the constraint at
                ``x``. Otherwise, it is a list of `numpy.ndarray`, each element
                being the value of a constraint at ``x``.

        This function attempts to detect the infeasibility of constraints
        (however, if no such infeasibility is detected, it does not mean that
        the problem is feasible). If the optimization procedure terminated
        because some constraints are infeasible (i.e., when the exit status is
        -4), the following fields may also be returned:

            infeasible_bounds : `numpy.ndarray`
                Indices of the bounds that are infeasible.
            infeasible_linear_constraints : `numpy.ndarray`
                Indices of the linear constraints that are infeasible.
            infeasible_nonlinear_constraints : `numpy.ndarray`
                Indices of the nonlinear constraints that are infeasible.

        Finally, if warnings are raised during the optimization procedure, the
        following field is also returned:

            warnings : list
                A list of the warnings raised during the optimization procedure.

        A description of the termination statuses is given below.

        .. list-table::
            :widths: 25 75
            :header-rows: 1

            * - Exit status
              - Description
            * - 0
              - The lower bound on the trust-region radius is reached.
            * - 1
              - The target value of the objective function is reached.
            * - 2
              - A trust-region step has failed to reduce the quadratic model.
            * - 3
              - The maximum number of function evaluations is reached.
            * - 4
              - Much cancellation occurred in a denominator.
            * - 7
              - Rounding errors are becoming damaging.
            * - 8
              - Rounding errors are damaging the solution point.
            * - 9
              - A denominator has become zero.
            * - 13
              - All variables are fixed by the bounds.
            * - 14
              - A linear feasibility problem has been received and solved.
            * - 15
              - A linear feasibility problem has been received but failed.
            * - -1
              - NaN is encountered in the solution point.
            * - -2
              - NaN is encountered in the objective/constraint function value.
                This is possible only in the classical mode.
            * - -3
              - NaN is encountered in the model parameter.
            * - -4
              - The problem is infeasible.

    References
    ----------
    .. [1] T. M. Ragonneau and Z. Zhang. PDFO: a cross-platform package for
       Powell's derivative-free optimization solvers.
       arXiv:`2302.13246 [math.OC] <https://arxiv.org/abs/2302.13246>`_, 2023.

    Examples
    --------
    The following example shows how to solve a simple optimization problem using
    `pdfo`. In practice, the  problem considered below should be solved with a
    derivative-based method as it is a smooth problem for which the derivatives
    are known. We solve it here using `pdfo` only as an illustration.

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

    >>> import numpy as np
    >>> from pdfo import pdfo
    >>> from scipy.optimize import Bounds, LinearConstraint, NonlinearConstraint
    >>>
    >>> # Build the constraints.
    >>> bounds = Bounds([0, 0.5], [2, 3])
    >>> linear_constraints = LinearConstraint([1, 1], 0, 1)
    >>> nonlinear_constraints = NonlinearConstraint(lambda x: x[0]**2 - x[1], -np.inf, 0)
    >>> constraints = [linear_constraints, nonlinear_constraints]
    >>>
    >>> # Solve the problem.
    >>> options = {'maxfev': 200}
    >>> res = pdfo(lambda x: x[0]**2 + x[1]**2, [0, 1], bounds=bounds, constraints=constraints, options=options)
    >>> res.x
    array([0. , 0.5])
    """
    from ._common import prepdfo, postpdfo
    from ._settings import ExitStatus

    # A cell that records all the warnings.
    output = dict()
    output['warnings'] = []

    # Preprocess the inputs.
    fun_c, x0_c, bounds_c, constraints_c, options_c, method, prob_info = \
        prepdfo(fun, x0, args, method, bounds, constraints, options)

    if prob_info['infeasible']:
        # The problem turned out infeasible during prepdfo.
        exitflag = ExitStatus.INFEASIBLE_ERROR.value
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
        exitflag = ExitStatus.FIXED_SUCCESS.value
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
            exitflag = ExitStatus.FEASIBILITY_SUCCESS.value
        else:
            exitflag = ExitStatus.INFEASIBILITY_ERROR.value
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
            from ._common import import_error_so
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
