.. _usage-python:

Usage for Python
================

General information
-------------------

.. currentmodule:: pdfo

PDFO provides a Python function `pdfo`, which can solve general constrained or unconstrained optimization problems without using derivatives.

The `pdfo` function can automatically identify the type of your problem and then call one of Powell's solvers, namely COBYLA, UOBYQA, NEWUOA, BOBYQA, and LINCOA.
The user can also specify the solver by setting the ``method`` argument of `pdfo`.

.. attention::

    The `pdfo` method does not accept any ``'solver'`` option.
    If you want to specify which solver to use, please use the ``method`` argument of the `pdfo` function.

The pdfo function is designed to be compatible with the `scipy.optimize.minimize` function of `SciPy <https://scipy.org>`_.
You can call pdfo in exactly the same way as calling `scipy.optimize.minimize` except that `pdfo` does not accept derivative arguments.

For detailed syntax of `pdfo`, see :ref:`python-api`.

An example
----------

The following code illustrates how to minimize the chained `Rosenbrock function <https://en.wikipedia.org/wiki/Rosenbrock_function>`_

.. math::
    :label: chrosen

    f(x) = \sum_{i = 1}^2 4 (x_{i+1} - x_i^2)^2 + (1 - x_i)^2

subject to various constraints.

.. code-block:: python

    import numpy as np
    from pdfo import pdfo
    from scipy.optimize import Bounds, LinearConstraint, NonlinearConstraint


    def chrosen(x):
        """Objective function"""
        return sum(4 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)


    def con_ineq(x):
        """Nonlinear inequality constraints"""
        return x[:-1] ** 2 - x[1:]


    def con_eq(x):
        """Nonlinear equality constraints"""
        return sum(x ** 2) - 1


    if __name__ == '__main__':
        print('\nMinimize the chained Rosenbrock function with three variables subject to various constraints:\n')
        x0 = [0, 0, 0]  # starting point

        print('\n1. Nonlinear constraints --- ||x||_2^2 = 1, x(i)^2 >= x(i+1) >= 0.5*x(i) >= 0 for i = 1, 2:\n')
        lb = [0, 0, 0]
        ub = [np.inf, np.inf, np.inf]
        bounds = Bounds(lb, ub)  # lb <= x <= ub
        # Alternative formulation:
        # bounds = [(lb[0], ub[0]), (lb[1], ub[1]), (lb[2], ub[2])]
        A = [[0.5, -1, 0], [0, 0.5, -1]]
        lin_lb = [-np.inf, -np.inf]
        lin_ub = [0, 0]
        lin_con = LinearConstraint(A, lin_lb, lin_ub)  # lin_lb <= A*x <= lin_ub
        nonlin_lb = [0, 0]
        nonlin_ub = [np.inf, np.inf]
        nonlin_con_ineq = NonlinearConstraint(con_ineq, nonlin_lb, nonlin_ub)  # nonlin_lb <= con_ineq(x) <= nonlin_ub
        nonlin_con_eq = NonlinearConstraint(con_eq, 0, 0)  # con_eq(x) = 0
        # Alternative formulation:
        # nonlin_con_ineq = {'type': 'ineq', 'fun': con_ineq}  # con_ineq(x) >= 0
        # nonlin_con_eq = {'type': 'eq', 'fun': con_eq}  # con_eq(x) = 0
        res = pdfo(chrosen, x0, bounds=bounds, constraints=[lin_con, nonlin_con_ineq, nonlin_con_eq])
        print(res)

        print('\n2. Linear constraints --- sum(x) = 1, x(i+1) <= x(i) <= 1 for i = 1, 2:\n')
        bounds = Bounds([-np.inf, -np.inf, -np.inf], [1, 1, 1])
        A = [[-1, 1, 0], [0, -1, 1], [1, 1, 1]]
        lin_con = LinearConstraint(A, [-np.inf, -np.inf, 1], [0, 0, 1])
        res = pdfo(chrosen, x0, bounds=bounds, constraints=lin_con)
        print(res)

        print('\n3. Bound constraints --- -0.5 <= x(1) <= 0.5, 0 <= x(2) <= 0.25:\n')
        bounds = Bounds([-0.5, 0, -np.inf], [0.5, 0.25, np.inf])
        res = pdfo(chrosen, x0, bounds=bounds)
        print(res)

        print('\n4. No constraints:\n')
        res = pdfo(chrosen, x0)
        print(res)
