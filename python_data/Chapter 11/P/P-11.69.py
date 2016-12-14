#-*-coding: utf-8 -*-

"""
The mergeable heap ADT is an extension of the priority queue ADT
consisting of operations add(k, v), min( ), remove_min( ) and merge(h),
where the merge(h) operations performs a union of the mergeable heap h
with the present one, incorporating all items into the current one while
emptying h. Describe a concrete implementation of the mergeable heap
ADT that achieves O(logn) performance for all its operations, where n
denotes the size of the resulting heap for the merge operation
"""