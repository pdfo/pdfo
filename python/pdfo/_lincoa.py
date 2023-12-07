# -*- coding: utf-8 -*-
import warnings
from inspect import stack

import numpy as np


def lincoa(fun, x0, args=(), bounds=None, constraints=(), options=None):
    r"""LINearly Constrained Optimization Algorithm.

    .. deprecated:: 1.3
        Calling the LINCOA solver via the `lincoa` function is deprecated.
        The LINCOA solver remains available in PDFO. Call the `pdfo` function
        with the argument ``method='lincoa'`` to use it.

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

            ``lincoa(fun, x0, args, ...)``

        is equivalent to

            ``lincoa(lambda x: fun(x, *args), x0, ...)``

    bounds : {`scipy.optimize.Bounds`, array_like, shape (n, 2)}, optional
        Bound constraints of the problem. It can be one of the cases below.

        #. An instance of `scipy.optimize.Bounds`.
        #. An array with shape (n, 2). The bound constraints for ``x[i]`` are
           ``bounds[i, 0] <= x[i] <= bounds[i, 1]``. Set ``bounds[i, 0]`` to
           :math:`-\infty` if there is no lower bound, and set ``bounds[i, 1]``
           to :math:`\infty` if there is no upper bound.

    constraints : {`scipy.optimize.LinearConstraint`, list}, optional
        Constraints of the problem. It can be one of the cases below.

        #. An instance of `scipy.optimize.LinearConstraint`.
        #. A list of instances of `scipy.optimize.LinearConstraint`.

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
                Number of interpolation points.
            quiet: bool, optional
                Whether to suppress the output messages.
            scale : bool, optional
                Whether to scale the problem according to the bound constraints.
            eliminate_lin_eq : bool, optional
                Whether to eliminate linear equality constraints.
            classical : bool, optional
                Whether to use the classical version of Powell's method. It is
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
                Description of the cause of the termination.
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

        For linearly constrained problems, the following field is also returned:

            constraints : {`numpy.ndarray`, list}
                The values of the constraints at the solution point. If a single
                constraint is passed, i.e., if the `constraints` argument is a
                `scipy.optimize.LinearConstraint`, then the returned value is
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

    Notes
    -----
    Professor Powell did not publish any paper introducing LINCOA.

    See also
    --------
    pdfo : Powell's Derivative-Free Optimization solvers.
    uobyqa : Unconstrained Optimization BY Quadratic Approximation.
    newuoa : NEW Unconstrained Optimization Algorithm.
    bobyqa : Bounded Optimization BY Quadratic Approximations.
    cobyla : Constrained Optimization BY Linear Approximations.

    References
    ----------
    .. [1] T. M. Ragonneau and Z. Zhang. PDFO: a cross-platform package for
       Powell's derivative-free optimization solvers.
       arXiv:`2302.13246 [math.OC] <https://arxiv.org/abs/2302.13246>`_, 2023.

    Examples
    --------
    The following example shows how to solve a simple optimization problem using
    `lincoa`. In practice, the  problem considered below should be solved with a
    derivative-based method as it is a smooth problem for which the derivatives
    are known. We solve it here using `lincoa` only as an illustration.

    We consider the 2-dimensional problem

    .. math::

        \min_{x, y \in \R} \quad x^2 + y^2 \quad \text{s.t.} \quad \left\{
        \begin{array}{l}
            0 \le x \le 2,\\
            1 / 2 \le y \le 3,\\
            0 \le x + y \le 1.
        \end{array} \right.

    We solve this problem using `lincoa` starting from the initial guess
    :math:`(x_0, y_0) = (0, 1)` with at most 200 function evaluations.

    .. testsetup::

        import numpy as np
        np.set_printoptions(precision=1, suppress=True)

    >>> from pdfo import lincoa
    >>> from scipy.optimize import Bounds, LinearConstraint
    >>>
    >>> # Build the constraints.
    >>> bounds = Bounds([0, 0.5], [2, 3])
    >>> constraints = LinearConstraint([1, 1], 0, 1)
    >>>
    >>> # Solve the problem.
    >>> options = {'maxfev': 200}
    >>> res = lincoa(lambda x: x[0]**2 + x[1]**2, [0, 1], bounds=bounds, constraints=constraints, options=options)
    >>> res.x
    array([0. , 0.5])
    """
    try:
        from .gethuge import gethuge
    except ImportError:
        from ._common import import_error_so

        # If gethuge cannot be imported, the execution should stop because the package is most likely not built.
        import_error_so('gethuge')

    from ._common import prepdfo, _augmented_linear_constraint, postpdfo
    from ._settings import ExitStatus, Options

    # This function is deprecated. Warn the user.
    warnings.warn('The `lincoa` function is deprecated. Use the `pdfo` function with the argument `method=\'lincoa\'` to use the LINCOA method.', DeprecationWarning, 2)

    fun_name = stack()[0][3]  # name of the current function
    if len(stack()) >= 3:
        invoker = stack()[1][3].lower()
    else:
        invoker = ''

    # A cell that records all the warnings.
    # Why do we record the warning message in output['warnings'] instead of prob_info['warnings']? Because, if lincoa is
    # called by pdfo, then prob_info will not be passed to postpdfo, and hence the warning message will be lost. To the
    # contrary, output will be passed to postpdfo anyway.
    output = dict()
    output['warnings'] = []

    # Preprocess the inputs.
    fun_c, x0_c, bounds_c, constraints_c, options_c, _, prob_info = \
        prepdfo(fun, x0, args, bounds=bounds, constraints=constraints, options=options)

    # Check whether nonlinear constraints are passed to the function.
    if constraints_c['nonlinear'] is not None:
        warn_message = '{}: Nonlinear constraints are given as parameter; they will be ignored.'.format(fun_name)
        warnings.warn(warn_message, Warning, 2)
        output['warnings'].append(warn_message)

    if invoker != 'pdfo' and prob_info['infeasible']:
        # The problem turned out infeasible during prepdfo.
        exitflag = ExitStatus.INFEASIBLE_ERROR.value
        nf = 1
        x = x0_c
        fx = fun_c(x)
        fhist = np.array([fx], dtype=np.float64)
        constrviolation = prob_info['constrv_x0']
        chist = np.array([constrviolation], dtype=np.float64)
        output['constr_modified'] = False
    elif invoker != 'pdfo' and prob_info['nofreex']:
        # x was fixed by the bound constraints during prepdfo.
        exitflag = ExitStatus.FIXED_SUCCESS.value
        nf = 1
        x = prob_info['fixedx_value']
        fx = fun_c(x)
        fhist = np.array([fx], dtype=np.float64)
        constrviolation = prob_info['constrv_fixedx']
        chist = np.array([constrviolation], dtype=np.float64)
        output['constr_modified'] = False
    elif invoker != 'pdfo' and prob_info['feasibility_problem']:
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
        # The problem turns out 'normal' during prepdfo include all the constraints into one single linear constraint
        # (A_aug)'*x <= b_aug; note the TRANSPOSE due to the data structure of the Fortran code.
        n = x0_c.size
        a_aug, b_aug = _augmented_linear_constraint(n, bounds_c, constraints_c)
        a_aug = a_aug.T

        # Extract the options and parameters
        npt = options_c[Options.NPT.value]
        maxfev = options_c[Options.MAXFEV.value]
        rhobeg = options_c[Options.RHOBEG.value]
        rhoend = options_c[Options.RHOEND.value]
        ftarget = options_c[Options.FTARGET.value]

        # The largest integer in the fortran functions; the factor 0.99 provides a buffer.
        max_int = np.floor(0.99 * gethuge('integer'))
        m = b_aug.size  # linear constraints: A_aug.T * x <= b_aug

        # The smallest nw, i.e., the nw with npt = n + 2. If it is larger than a threshold (system dependent), the
        # problem is too large to be executed on the system.
        min_nw = m * (2 + n) + (n + 2) * (2 * n + 6) + n * (9 + 3 * n) + max(m + 3 * n, 2 * m + n, 2 * n + 4)
        if min_nw >= max_int:
            executor = invoker.lower() if invoker == 'pdfo' else fun_name
            # nw would suffer from overflow in the Fortran code, exit immediately.
            raise SystemError('{}: problem too large for {}. Try other solvers.'.format(executor, fun_name))

        # The largest possible value for npt given that nw <= max_int.
        alpha = n + 7
        beta = 2 * m + m * (2 + n) + n * (9 + 3 * n) - max_int
        max_npt = max(n + 2, np.floor(0.5 * (-alpha + np.sqrt(alpha * alpha - 4 * beta))))
        if npt > max_npt:
            npt = max_npt
            w_message = \
                '{}: {} is so large that it is unable to allocate the workspace; it is set to {}'.format(fun_name, Options.NPT.value, npt)
            warnings.warn(w_message, Warning, 2)
            output['warnings'].append(w_message)
        if maxfev > max_int:
            maxfev = max_int
            w_message = \
                '{}: {} exceeds the upper limit of Fortran integer; it is set to {}'.format(fun_name, Options.MAXFEV.value, maxfev)
            warnings.warn(w_message, Warning, 2)
            output['warnings'].append(w_message)

        # If x0 is not feasible, LINCOA will modify the constraints to make it feasible (which is a bit strange).
        # prepdfo has tried to find a feasible x0. Raise a warning is x0 is not 'feasible enough' so that the
        # constraints will be modified.
        if a_aug.size > 0 and any(np.dot(x0_c.T, a_aug) > b_aug + 1e-10 * max(1, np.max(b_aug))):
            output['constr_modified'] = True
            w_message = \
                '{}: preprocessing code did not find a feasible x0; problem is likely infeasible or SciPy is not ' \
                'installed on the machine; {} will modify the right-hand side of the constraints to make x0 ' \
                'feasible.'.format(fun_name, fun_name)
            warnings.warn(w_message, Warning, 2)
            output['warnings'].append(w_message)
        else:
            output['constr_modified'] = False

        # Call the Fortran code.
        try:
            if options_c[Options.CLASSICAL.value]:
                from . import flincoa_classical as flincoa
            else:
                from . import flincoa
        except ImportError:
            from ._common import import_error_so
            import_error_so()

        # m should be precised not to raise any error if there is no linear constraints.
        x, fx, exitflag, fhist, chist, constrviolation = \
            flincoa.mlincoa(npt, m, a_aug, b_aug, x0_c, rhobeg, rhoend, 0, maxfev, ftarget, fun_c)
        nf = int(flincoa.flincoa.nf)

    # Postprocess the result.
    return postpdfo(x, fx, exitflag, output, fun_name, nf, fhist, options_c, prob_info, constrviolation, chist)
