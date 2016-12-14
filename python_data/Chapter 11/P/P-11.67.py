#-*-coding: utf-8 -*-

"""
In describing multisets and multimaps in Section 10.5.3, we describe a
general approach for adapting a traditional map by storing all duplicates
within a secondary container as a value in the map. Give an alternative
implementation of a multimap using a binary search tree such that each
entry of the map is stored at a distinct node of the tree. With the existence
of duplicates, we redefine the search tree property so that all items in the
left subtree of a position p with key k have keys that are less than or equal
to k, while all items in the right subtree of p have keys that are greater than
or equal to k. Use the public interface given in Code Fragment 10.17
"""
