Utility classes
===============

.. currentmodule:: pdfo

These classes are used by the optimizers in PDFO.
The bound, linear, and nonlinear constraints are represented by the `Bounds`, `LinearConstraint`, and `NonlinearConstraint` classes, respectively.
Similar classes are also available in `scipy.optimize`, except that the ones below do not have derivative arguments, as PDFO does not use derivatives.
You can use either these classes or those provided by `SciPy <https://scipy.org>`_ when calling `pdfo`, `bobyqa`, `lincoa`, and `cobyla`.

.. autosummary::
    :toctree: generated/

    Bounds
    LinearConstraint
    NonlinearConstraint
    OptimizeResult
