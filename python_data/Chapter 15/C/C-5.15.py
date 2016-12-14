#-*-coding: utf-8 -*-

"""
Another possible external-memory map implementation is to use a skip
list, but to collect consecutive groups of O(B) nodes, in individual blocks,
on any level in the skip list. In particular, we define an order-d B-skip
list to be such a representation of a skip list structure, where each block
contains at least d/2 list nodes and at most d list nodes. Let us also
choose d in this case to be the maximum number of list nodes from a level
of a skip list that can fit into one block. Describe how we should modify
the skip-list insertion and removal algorithms for a B-skip list so that the
expected height of the structure is O(logn/logB).
"""