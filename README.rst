pydurations
===========

Time intervals
--------------
::

  >>> import pydurations
  >>> x = 10
  >>> x.seconds
  datetime.timedelta(0, 10)
  >>> (3).weeks
  datetime.timedelta(21)

Date times
----------
::

  >>> import pydurations
  >>> from datetime import datetime
  >>> datetime.now()
  datetime.datetime(2014, 5, 18, 16, 28, 22, 112898)
  >>> datetime.now() - (10).days
  datetime.datetime(2014, 5, 8, 16, 28, 29, 199993)
  >>> (10).days.ago
  datetime.datetime(2014, 5, 8, 16, 28, 34, 475991)