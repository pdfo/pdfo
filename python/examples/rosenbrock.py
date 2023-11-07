#!/usr/bin/env python3
"""Illustration of how to use pdfo."""
import numpy as np
from pdfo import pdfo
from scipy.optimize import Bounds, LinearConstraint, NonlinearConstraint


# Print NumPy array nicely.
np.set_printoptions(precision=4, threshold=7, edgeitems=3)


def chrosen(x):
    """Chained Rosenbrock function."""
    return sum((1 - x[:-1]) ** 2 + 4 * (x[1:] - x[:-1] ** 2) ** 2)


def nlc_ineq(x):
    """Example of nonlinear inequality constraint function."""
    return x[:-1] ** 2 - x[1:]


def nlc_eq(x):
    """Example of nonlinear equality constraint function."""
    return sum(x ** 2) - 1


if __name__ == '__main__':
    print('Minimize the chained Rosenbrock function with three variables subject to various constraints:', end='\n\n')
    x0 = [0, 0, 0]  # starting point

    print('1. Nonlinear constraints --- ||x||_2^2 = 1, x(i)^2 >= x(i+1) >= 0.5*x(i) >= 0 for i = 1, 2:', end='\n\n')
    lb = [0, 0, 0]
    ub = [np.inf, np.inf, np.inf]
    bounds = Bounds(lb, ub)  # bound constraints: lb <= x <= ub
    A = [[0.5, -1, 0], [0, 0.5, -1]]
    lin_lb = [-np.inf, -np.inf]
    lin_ub = [0, 0]
    lin_con = LinearConstraint(A, lin_lb, lin_ub)  # inequality constraints: lin_lb <= A*x <= lin_ub
    nonlin_lb = [0, 0]
    nonlin_ub = [np.inf, np.inf]
    nonlin_con_ineq = NonlinearConstraint(nlc_ineq, nonlin_lb, nonlin_ub)  # inequality constraints: nonlin_lb <= nlc_ineq(x) <= nonlin_ub
    nonlin_con_eq = NonlinearConstraint(nlc_eq, 0, 0)  # equality constraint: nlc_eq(x) = 0
    res = pdfo(chrosen, x0, bounds=bounds, constraints=[lin_con, nonlin_con_ineq, nonlin_con_eq])
    print(res, end='\n\n')

    print('2. Linear constraints --- sum(x) = 1, x(i+1) <= x(i) <= 1 for i = 1, 2:', end='\n\n')
    bounds = Bounds([-np.inf, -np.inf, -np.inf], [1, 1, 1])
    A = [[-1, 1, 0], [0, -1, 1], [1, 1, 1]]
    lin_con = LinearConstraint(A, [-np.inf, -np.inf, 1], [0, 0, 1])
    res = pdfo(chrosen, x0, bounds=bounds, constraints=lin_con)
    print(res, end='\n\n')

    print('3. Bound constraints --- -0.5 <= x(1) <= 0.5, 0 <= x(2) <= 0.25:', end='\n\n')
    bounds = Bounds([-0.5, 0, -np.inf], [0.5, 0.25, np.inf])
    res = pdfo(chrosen, x0, bounds=bounds)
    print(res, end='\n\n')

    print('4. No constraints:', end='\n\n')
    res = pdfo(chrosen, x0)
    print(res)
