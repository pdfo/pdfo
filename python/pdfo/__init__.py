# -*- coding: utf-8 -*-
"""Management of the importable functions of pdfo."""
from ._bobyqa import bobyqa
from ._cobyla import cobyla
from ._lincoa import lincoa
from ._newuoa import newuoa
from ._uobyqa import uobyqa
from ._pdfo import pdfo
from . import tests
from .tests import test_pdfo as testpdfo

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Final release markers:
#   X.Y.0   # For first release after an increment in Y
#   X.Y.Z   # For bugfix releases
#
# Admissible pre-release markers:
#   X.YaN   # Alpha release
#   X.YbN   # Beta release
#   X.YrcN  # Release Candidate
#
# Dev branch marker is: 'X.Y.dev' or 'X.Y.devN' where N is an integer.
# 'X.Y.dev0' is the canonical version of 'X.Y.dev'.
__version__ = '2.0.2'

__all__ = ['bobyqa', 'cobyla', 'lincoa', 'newuoa', 'uobyqa', 'pdfo', 'tests', 'testpdfo']
