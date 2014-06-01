"""
datetimex.api
~~~~~~~~~~~~~

Improved datetimes

"""
import pytz
import datetime as dt

from datetime import datetime


def now(timezone=None):
    if isinstance(timezone, dt.tzinfo) or timezone is None:
        return datetime.now(timezone)
    else:
        return datetime.now(pytz.timezone(timezone))