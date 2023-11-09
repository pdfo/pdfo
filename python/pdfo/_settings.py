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
    RHOBEG = 'rhobeg'
    RHOEND = 'rhoend'
    MAXFEV = 'maxfev'
    FTARGET = 'ftarget'
    NPT = 'npt'
    QUIET = 'quiet'
    SCALE = 'scale'
    ELIMINATE_LIN_EQ = 'eliminate_lin_eq'
    HONOUR_X0 = 'honour_x0'
    CLASSICAL = 'classical'
    DEBUG = 'debug'
    CHKFUNVAL = 'chkfunval'


# Default options.
DEFAULT_OPTIONS = {
    Options.RHOBEG.value: 1.0,
    Options.RHOEND.value: 1e-6,
    Options.MAXFEV.value: lambda n: 500 * n,
    Options.FTARGET.value: float('-inf'),
    Options.NPT.value: lambda n: 2 * n + 1,
    Options.QUIET.value: True,
    Options.SCALE.value: False,
    Options.ELIMINATE_LIN_EQ.value: True,
    Options.HONOUR_X0.value: False,
    Options.CLASSICAL.value: False,
    Options.DEBUG.value: False,
    Options.CHKFUNVAL.value: False,
}
