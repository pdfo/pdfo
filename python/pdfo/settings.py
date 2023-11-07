from enum import Enum


class ExitStatus(Enum):
    """
    Exit statuses.
    """
    RADIUS_SUCCESS = 0
    TARGET_SUCCESS = 1
    STEP_REDUCTION_ERROR = 2
    MAX_EVAL_WARNING = 3
    SMALL_DENOMINATOR_WARNING = 4
    NPT_ERROR = 5
    BOUND_ERROR = 6
    DAMAGE_ROUNDING_ERROR = 7
    X_ROUNDING_ERROR = 8
    ZERO_DENOMINATOR_ERROR = 9
    N_ERROR = 10
    MAXFEV_ERROR = 11
    TRIVIAL_CONSTRAINT_ERROR = 12
    FIXED_SUCCESS = 13
    FEASIBILITY_SUCCESS = 14
    INFEASIBILITY_ERROR = 15
    NAN_X_ERROR = -1
    NAN_EVAL_ERROR = -2
    NAN_MODEL_ERROR = -3
    INFEASIBLE_ERROR = -4


class Options(str, Enum):
    """
    Option names.
    """
    CHECK_EVAL = 'check_eval'
    CLASSICAL = 'classical'
    DEBUG = 'debug'
    ELIMINATE_LINEAR_EQ = 'eliminate_lin_eq'
    HONOR_X0 = 'honour_x0'
    MAX_EVAL = 'max_eval'
    NPT = 'npt'
    QUIET = 'quiet'
    RADIUS_INIT = 'radius_init'
    RADIUS_FINAL = 'radius_final'
    SCALE = 'scale'
    TARGET = 'target'


# Default options.
DEFAULT_OPTIONS = {
    Options.CHECK_EVAL.value: False,
    Options.CLASSICAL.value: False,
    Options.DEBUG.value: False,
    Options.ELIMINATE_LINEAR_EQ.value: True,
    Options.HONOR_X0.value: False,
    Options.MAX_EVAL.value: lambda n: 500 * n,
    Options.NPT.value: lambda n: 2 * n + 1,
    Options.QUIET.value: True,
    Options.RADIUS_INIT.value: 1.0,
    Options.RADIUS_FINAL.value: 1e-6,
    Options.SCALE.value: False,
    Options.TARGET.value: float('-inf'),
}
