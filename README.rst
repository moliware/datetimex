datetimex
=========

Vitamins for datetimes.


Install
-------

It's not in pypi yet, so:

::

  python setup.py install


How to use it
-------------

Just import the module and call patch_all and you will get improved datetimes.

::

  import datetimex
  datetimex.patch_all()


Working with intervals
----------------------

Int objects have now some new properties for creating intervals as follows:

::

  >>> import datetimex
  >>> datetimex.patch_all()

  >>> (2).years
  datetime.timedelta(730)

These are the new methods for ints:

  - micros
  - micros
  - millis
  - millis
  - seconds
  - seconds
  - minutes
  - minutes
  - hours
  - days
  - weeks
  - years


Besides the interval object has new methods:

- ago
- since

For example:

::

  >>> import datetimex
  >>> datetimex.patch_all()
  >>> from datetime import datetime

  >>> (3).days.ago
  datetime.datetime(2014, 6, 5, 10, 46, 20, 588674)

  >>> (3).days.since(datetime.now())
  datetime.datetime(2014, 6, 11, 10, 47, 13, 92963)



Timezones
---------

Timezones can be used as string

::

  >>> datetime.now('Europe/Berlin')
  datetime.datetime(2014, 6, 8, 10, 49, 2, 881309, tzinfo=<DstTzInfo 'Europe/Berlin' CEST+2:00:00 DST>)
