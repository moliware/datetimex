"""
datetimex.int
~~~~~~~~~~~~~

Adds to int objects a few new methods to create intervals.

"""
from datetime import timedelta
from forbiddenfruit import curse


@property
def micros(self):
    return timedelta(microseconds=self)

@property
def millis(self):
    return timedelta(milliseconds=self)

@property
def seconds(self):
    return timedelta(seconds=self)

@property
def minutes(self):
    return timedelta(minutes=self)

@property
def hours(self):
    return timedelta(hours=self)

@property
def days(self):
    return timedelta(days=self)

@property
def weeks(self):
    return timedelta(weeks=self)

@property
def years(self):
    return timedelta(days=self * 365)

def patch():
    curse(int, 'micros', micros)
    curse(int, 'microseconds', micros)
    curse(int, 'millis', millis)
    curse(int, 'milliseconds', millis)
    curse(int, 'secs', seconds)
    curse(int, 'seconds', seconds)
    curse(int, 'mins', minutes)
    curse(int, 'minutes', minutes)
    curse(int, 'hours', hours)
    curse(int, 'days', days)
    curse(int, 'weeks', weeks)
    curse(int, 'years', years)
