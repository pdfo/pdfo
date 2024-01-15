# -*- coding: utf-8 -*-
import warnings
from inspect import stack

import numpy as np


def newuoa(fun, x0, args=(), options=None):
    r"""NEW Unconstrained Optimization Algorithm.

    .. deprecated:: 1.3
        Calling the NEWUOA solver via the `newuoa` function is deprecated.
        The NEWUOA solver remains available in PDFO. Call the `newuoa` function
        with the argument ``method='newuoa'`` to use it.

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

            ``newuoa(fun, x0, args, ...)``

        is equivalent to

            ``newuoa(lambda x: fun(x, *args), x0, ...)``

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
                point is less than or equal to this target.
            npt : int, optional
                Number of interpolation points.
            quiet: bool, optional
                Whether to suppress the output messages.
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
    .. [1] M. J. D. Powell. The NEWUOA software for unconstrained optimization
       without derivatives. In G. Di Pillo and M. Roma, editors, *Large-Scale
       Nonlinear Optimization*, volume 83 of *Nonconvex Optimization and Its
       Applications*, pages 255--297, Boston, MA, USA, 2006. Springer.
    .. [2] M. J. D. Powell. Developments of NEWUOA for minimization without
       derivatives. *IMA J. Numer. Anal.*, 28:649--664, 2008.
    .. [3] T. M. Ragonneau and Z. Zhang. PDFO: a cross-platform package for
       Powell's derivative-free optimization solvers.
       arXiv:`2302.13246 [math.OC] <https://arxiv.org/abs/2302.13246>`_, 2023.

    See also
    --------
    pdfo : Powell's Derivative-Free Optimization solvers.
    uobyqa : Unconstrained Optimization BY Quadratic Approximation.
    bobyqa : Bounded Optimization BY Quadratic Approximations.
    lincoa : LINearly Constrained Optimization Algorithm.
    cobyla : Constrained Optimization BY Linear Approximations.

    Examples
    --------
    The following example shows how to solve a simple optimization problem using
    `newuoa`. In practice, the  problem considered below should be solved with a
    derivative-based method as it is a smooth problem for which the derivatives
    are known. We solve it here using `newuoa` only as an illustration.

    We consider the 2-dimensional problem

    .. math::

        \min_{x, y \in \R} \quad x^2 + y^2.

    We solve this problem using `newuoa` starting from the initial guess
    :math:`(x_0, y_0) = (0, 1)` with at most 200 function evaluations.

    .. testsetup::

        import numpy as np
        np.set_printoptions(precision=1, suppress=True)

    >>> from pdfo import newuoa
    >>>
    >>> # Solve the problem.
    >>> options = {'maxfev': 200}
    >>> res = newuoa(lambda x: x[0]**2 + x[1]**2, [0, 1], options=options)
    >>> res.x
    array([0., 0.])
    """
    try:
        from .gethuge import gethuge
    except ImportError:
        from ._common import import_error_so

        # If gethuge cannot be imported, the execution should stop because the package is most likely not built.
        import_error_so('gethuge')

    from ._common import prepdfo, postpdfo, suppress_stderr
    from ._settings import ExitStatus, Options

    # This method is deprecated. Warn the user.
    warnings.warn('The `newuoa` function is deprecated. Use the `pdfo` function with the argument `method=\'newuoa\'` to use the NEWUOA method.', DeprecationWarning, 2)

    fun_name = stack()[0][3]  # name of the current function
    if len(stack()) >= 3:
        invoker = stack()[1][3].lower()
    else:
        invoker = ''

    # A cell that records all the warnings.
    # Why do we record the warning message in output['warnings'] instead of prob_info['warnings']? Because, if newuoa is
    # called by pdfo, then prob_info will not be passed to postpdfo, and hence the warning message will be lost. To the
    # contrary, output will be passed to postpdfo anyway.
    output = dict()
    output['warnings'] = []

    # Preprocess the inputs.
    fun_c, x0_c, _, _, options_c, _, prob_info = prepdfo(fun, x0, args, options=options)

    if invoker != 'pdfo' and prob_info['feasibility_problem']:
        # An "unconstrained feasibility problem" is ridiculous yet nothing wrong mathematically.
        # We could set fx=[], funcCount=0, and fhist=[] since no function evaluation occurred. But then we will have to
        # modify the validation of fx, funcCount, and fhist in postpdfo. To avoid such a modification, we set fx,
        # funcCount, and fhist as below and then revise them in postpdfo.
        nf = 1
        x = x0_c  # prepdfo has tried to set x0 to a feasible point (but may have failed)
        fx = fun_c(x)
        fhist = np.array([fx], dtype=np.float64)
        exitflag = ExitStatus.FEASIBILITY_SUCCESS.value
    else:
        # Extract the options and parameters.
        npt = options_c[Options.NPT.value]
        maxfev = options_c[Options.MAXFEV.value]
        rhobeg = options_c[Options.RHOBEG.value]
        rhoend = options_c[Options.RHOEND.value]
        ftarget = options_c[Options.FTARGET.value]

        # The largest integer in the fortran functions; the factor 0.99 provides a buffer.
        max_int = np.floor(0.99 * gethuge('integer'))
        n = x0_c.size

        # The smallest nw, i.e., the nw with npt = n + 2. If it is larger than a threshold (system dependent), the
        # problem is too large to be executed on the system.
        min_nw = (n + 15) * (2 * n + 2) + 3 * n * (n + 3) / 2
        if min_nw + 1 >= max_int:
            executor = invoker.lower() if invoker == 'pdfo' else fun_name
            # nw would suffer from overflow in the Fortran code, exit immediately.
            raise SystemError('{}: problem too large for {}. Try other solvers.'.format(executor, fun_name))

        # The largest possible value for npt given that nw <= max_int.
        max_npt = max(n + 2, np.floor(0.5 * (-n - 13 + np.sqrt((n - 13) ** 2 + 4 * (max_int - 3 * n * (n + 3) / 2 - 1)))))
        if npt > max_npt:
            npt = max_npt
            w_message = \
                '{}: {} is so large that it is unable to allocate the workspace; it is set to {}'.format(fun_name, Options.NPT.value, npt)
            warnings.warn(w_message, Warning, 2)
            output['warnings'].append(w_message)
        if maxfev > max_int:
            maxfev = max_int
            w_message = '{}: {} exceeds the upper limit of Fortran integer; it is set to {}'.format(fun_name, Options.MAXFEV.value, maxfev)
            warnings.warn(w_message, Warning, 2)
            output['warnings'].append(w_message)

        # Call the Fortran code.
        try:
            if options_c[Options.CLASSICAL.value]:
                from . import fnewuoa_classical as fnewuoa
            else:
                from . import fnewuoa
        except ImportError:
            from ._common import import_error_so
            import_error_so()

        with suppress_stderr():
            x, fx, exitflag, fhist = fnewuoa.mnewuoa(npt, x0_c, rhobeg, rhoend, 0, maxfev, ftarget, fun_c)
        nf = int(fnewuoa.fnewuoa.nf)

    # Postprocess the result.
    return postpdfo(x, fx, exitflag, output, fun_name, nf, fhist, options_c, prob_info)
