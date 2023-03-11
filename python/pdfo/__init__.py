# -*- coding: utf-8 -*-
"""Management of the importable functions of pdfo.

Authors
-------
Tom M. RAGONNEAU (tom.ragonneau@connect.polyu.hk)
and Zaikun ZHANG (zaikun.zhang@polyu.edu.hk)
Department of Applied Mathematics,
The Hong Kong Polytechnic University.

Dedicated to the late Professor M. J. D. Powell FRS (1936--2015).
"""
from datetime import datetime

try:
    # Enable subpackage importing when binaries are not yet built.
    __PDFO_SETUP__  # noqa
except NameError:
    __PDFO_SETUP__ = False

# Definition of the metadata of PDFO for Python. It is accessible via:
# >>> import pdfo
# >>> print(pdfo.__author__)
# >>> ...
__author__ = 'Tom M. Ragonneau and Zaikun Zhang'
__copyright__ = f'Copyright 2020--{datetime.now().year}, ' \
                f'Tom M. Ragonneau and Zaikun Zhang'
__credits__ = ['Tom M. Ragonneau', 'Zaikun Zhang', 'Antoine Dechaume']
__license__ = 'LGPLv3+'
__version__ = '1.2'
__date__ = 'October, 2021'
__maintainer__ = 'Tom M. Ragonneau and Zaikun Zhang'
__email__ = 'tom.ragonneau@connect.polyu.hk and zaikun.zhang@polyu.edu.hk'
__status__ = 'Production'

if not __PDFO_SETUP__:

    from ._dependencies import OptimizeResult, Bounds, LinearConstraint, \
        NonlinearConstraint

    from ._bobyqa import bobyqa
    from ._cobyla import cobyla
    from ._lincoa import lincoa
    from ._newuoa import newuoa
    from ._uobyqa import uobyqa
    from ._pdfo import pdfo
    from . import tests
    from .tests import test_pdfo as testpdfo
    __all__ = ['OptimizeResult', 'Bounds', 'LinearConstraint',
               'NonlinearConstraint', 'bobyqa', 'cobyla', 'lincoa', 'newuoa',
               'uobyqa', 'pdfo', 'tests', 'testpdfo']
