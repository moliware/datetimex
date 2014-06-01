"""
datetimex.intervals
~~~~~~~~~~~~~~~~~~~

Adds some methods to intervals in order to get dates. So far:

* ago
* since

"""
from datetime import datetime, timedelta
from forbiddenfruit import curse


@property
def ago(self):
    return datetime.now() - self

def since(self, date):
    return date + self

curse(timedelta, 'ago', ago)
curse(timedelta, 'since', since)