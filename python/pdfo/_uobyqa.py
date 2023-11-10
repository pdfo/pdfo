# -*- coding: utf-8 -*-
import warnings
from inspect import stack

import numpy as np


def uobyqa(fun, x0, args=(), options=None):
    r"""Unconstrained Optimization BY Quadratic Approximation.

    .. deprecated:: 1.3
        Calling the UOBYQA solver via the `uobyqa` function is deprecated.
        The UOBYQA solver remains available in PDFO. Call the `pdfo` function
        with the argument ``method='uobyqa'`` to use it.

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

            ``uobyqa(fun, x0, args, ...)``

        is equivalent to

            ``uobyqa(lambda x: fun(x, *args), x0, ...)``

    options : dict, optional
        The options passed to the solver. Accepted options are:

            rhobeg : float, optional
                Initial value of the trust-region radius, which should be
                positive. Typically, it should be in the order of one tenth of
                the greatest expected change to the variables.
            rhoend : float, optional
                Final value of the trust-region radius, which should be positive
                and at most ``options['rhobeg']``. It should indicate the
                accuracy required in the final values of the variables.
            maxfev : int, optional
                Maximum number of function evaluations.
            ftarget : float, optional
                Target value of the objective function. The optimization
                procedure is terminated when the objective function value of a
                point is less than or equal to this target.
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

        If warnings are raised during the optimization procedure, the following
        field is also returned:

            warnings : list
                A list of the warnings raised during the optimization procedure.

    References
    ----------
    .. [1] M. J. D. Powell. UOBYQA: unconstrained optimization by quadratic
       approximation. *Math. Program.*, 92:555--582, 2002.
    .. [2] T. M. Ragonneau and Z. Zhang. PDFO: a cross-platform package for
       Powell's derivative-free optimization solvers.
       arXiv:`2302.13246 [math.OC] <https://arxiv.org/abs/2302.13246>`_, 2023.

    See also
    --------
    pdfo : Powell's Derivative-Free Optimization solvers.
    newuoa : NEW Unconstrained Optimization Algorithm.
    bobyqa : Bounded Optimization BY Quadratic Approximations.
    lincoa : LINearly Constrained Optimization Algorithm.
    cobyla : Constrained Optimization BY Linear Approximations.

    Examples
    --------
    The following example shows how to solve a simple optimization problem using
    `uobyqa`. In practice, the  problem considered below should be solved with a
    derivative-based method as it is a smooth problem for which the derivatives
    are known. We solve it here using `uobyqa` only as an illustration.

    We consider the 2-dimensional problem

    .. math::

        \min_{x, y \in \R} \quad x^2 + y^2.

    We solve this problem using `uobyqa` starting from the initial guess
    :math:`(x_0, y_0) = (0, 1)` with at most 200 function evaluations.

    .. testsetup::

        import numpy as np
        np.set_printoptions(precision=1, suppress=True)

    >>> from pdfo import uobyqa
    >>>
    >>> # Solve the problem.
    >>> options = {'maxfev': 200}
    >>> res = uobyqa(lambda x: x[0]**2 + x[1]**2, [0, 1], options=options)
    >>> res.x
    array([0., 0.])
    """
    try:
        from .gethuge import gethuge
    except ImportError:
        from ._common import import_error_so

        # If gethuge cannot be imported, the execution should stop because the package is most likely not built.
        import_error_so('gethuge')

    from ._common import prepdfo, postpdfo
    from ._settings import ExitStatus, Options

    # This method is deprecated. Warn the user.
    warnings.warn('The `uobyqa` function is deprecated. Use the `pdfo` function with the argument `method=\'uobyqa\'` to use the UOBYQA method.', DeprecationWarning, 2)

    fun_name = stack()[0][3]  # name of the current function
    if len(stack()) >= 3:
        invoker = stack()[1][3].lower()
    else:
        invoker = ''

    # A cell that records all the warnings.
    # Why do we record the warning message in output['warnings'] instead of prob_info['warnings']? Because, if uobyqa is
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
        maxfev = options_c[Options.MAXFEV.value]
        rhobeg = options_c[Options.RHOBEG.value]
        rhoend = options_c[Options.RHOEND.value]
        ftarget = options_c[Options.FTARGET.value]

        # UOBYQA is not intended to solve univariate problem; most likely, the solver will fail.
        n = x0_c.size
        if n <= 1:
            w_message = '{}: a univariate problem received; {} may fail. Try other solvers.'.format(fun_name, fun_name)
            warnings.warn(w_message, Warning, 2)
            output['warnings'].append(w_message)

        # The largest integer in the fortran functions; the factor 0.99 provides a buffer.
        max_int = np.floor(0.99 * gethuge('integer'))

        # The smallest nw, i.e., the nw with npt = (n+1)*(n+2)/2. If it is larger than a threshold (system dependent),
        # the problem is too large to be executed on the system.
        min_nw = (n * (42 + n * (23 + n * (8 + n))) + max(2 * n**2, 18 * n)) / 4
        if min_nw + 1 >= max_int:
            executor = invoker.lower() if invoker == 'pdfo' else fun_name
            # nw would suffer from overflow in the Fortran code, exit immediately.
            raise SystemError('{}: problem too large for {}. Try other solvers.'.format(executor, fun_name))

        if maxfev > max_int:
            maxfev = max_int
            w_message = '{}: {} exceeds the upper limit of Fortran integer; it is set to {}'.format(fun_name, Options.MAXFEV.value, maxfev)
            warnings.warn(w_message, Warning, 2)
            output['warnings'].append(w_message)

        # Call the Fortran code.
        try:
            if options_c[Options.CLASSICAL.value]:
                from . import fuobyqa_classical as fuobyqa
            else:
                from . import fuobyqa
        except ImportError:
            from ._common import import_error_so
            import_error_so()

        x, fx, exitflag, fhist = fuobyqa.muobyqa(x0_c, rhobeg, rhoend, 0, maxfev, ftarget, fun_c)
        nf = int(fuobyqa.fuobyqa.nf)

    # Postprocess the result.
    return postpdfo(x, fx, exitflag, output, fun_name, nf, fhist, options_c, prob_info)
