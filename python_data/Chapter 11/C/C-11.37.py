#-*-coding: utf-8 -*-

"""
Suppose we wish to support a new method count_range(start, stop) that
determines how many keys of a sorted map fall in the specified range. We
could clearly implement this in O(s+h) time by adapting our approach to
find_range. Describe how to modify the search tree structure to support
O(h) worst-case time for count_range.
"""