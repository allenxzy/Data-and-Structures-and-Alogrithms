#-*-coding: utf-8 -*-

"""
In Section 2.3.5, we note that our version of the Range class has implicit
support for iteration, due to its explicit support of both__len__
and__getitem__. The class also receives implicit support of the Boolean
test, “k in r” for Range r. This test is evaluated based on a forward iteration
through the range, as evidenced by the relative quickness of the test
2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
more efficient implementation of the__contains__method to determine
whether a particular value lies within a given range. The running time of
your method should be independent of the length of the range
"""
