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

            rhobeg: float, optional
                Initial value of the trust region radius, which should be a
                positive scalar. Typically, ``options['rhobeg']`` should be in
                the order of one tenth of the greatest expected change to a
                variable. By default, it is ``1``.
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
                Fortran code.
            ftarget: float, optional
                Target value of the objective function. If a feasible iterate
                achieves an objective function value lower or equal to
                ```options['ftarget']``, the algorithm stops immediately. By
                default, it is :math:`-\infty`.
            quiet: bool, optional
                Whether the interface is quiet. If it is set to ``True``, the
                output message will not be printed. This flag does not interfere
                with the warning and error printing.
            classical: bool, optional
                Whether to call the classical Powell code or not. It is not
                encouraged in production. By default, it is ``False``.
            debug: bool, optional
                Debugging flag. It is not encouraged in production. By default,
                it is ``False``.
            chkfunval: bool, optional
                Flag used when debugging. If both ``options['debug']`` and
                ``options['chkfunval']`` are ``True``, an extra function
                evaluation would be performed to check whether the returned
                values of objective function and constraint match the returned
                ``x``. By default, it is ``False``.

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

    from ._common import prepdfo, postpdfo
    from ._settings import ExitStatus

    # This method is deprecated. Warn the user.
    warnings.warn('The `newuoa` function is deprecated. Use the `pdfo` function with the argument `method=\'newuoa\'` to use the NEWUOA method.', DeprecationWarning)

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
        npt = options_c['npt']
        maxfev = options_c['maxfev']
        rhobeg = options_c['rhobeg']
        rhoend = options_c['rhoend']
        ftarget = options_c['ftarget']

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
                '{}: npt is so large that it is unable to allocate the workspace; it is set to {}'.format(fun_name, npt)
            warnings.warn(w_message, Warning)
            output['warnings'].append(w_message)
        if maxfev > max_int:
            maxfev = max_int
            w_message = '{}: maxfev exceeds the upper limit of Fortran integer; it is set to {}'.format(fun_name, maxfev)
            warnings.warn(w_message, Warning)
            output['warnings'].append(w_message)

        # Call the Fortran code.
        try:
            if options_c['classical']:
                from . import fnewuoa_classical as fnewuoa
            else:
                from . import fnewuoa
        except ImportError:
            from ._common import import_error_so
            import_error_so()

        x, fx, exitflag, fhist = fnewuoa.mnewuoa(npt, x0_c, rhobeg, rhoend, 0, maxfev, ftarget, fun_c)
        nf = int(fnewuoa.fnewuoa.nf)

    # Postprocess the result.
    return postpdfo(x, fx, exitflag, output, fun_name, nf, fhist, options_c, prob_info)
