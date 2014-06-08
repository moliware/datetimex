import datetimex.int
import datetimex.intervals

from .api import *

def patch_all():
    patch()                     # api changes
    datetimex.int.patch()
    datetimex.intervals.patch()