#-*-coding: utf-8 -*-

"""
Python’s collections module provides an OrderedDict class that is unrelated
to our sorted map abstraction. An OrderedDict is a subclass of the
standard hash-based dict class that retains the expected O(1) performance
for the primary map operations, but that also guarantees that the__iter__
method reports items of the map according to first-in, first-out (FIFO)
order. That is, the key that has been in the dictionary the longest is reported
first. (The order is unaffected when the value for an existing key
is overwritten.) Describe an algorithmic approach for achieving such performance.
"""