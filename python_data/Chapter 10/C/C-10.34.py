#-*-coding: utf-8 -*-

"""
Computing a hash code can be expensive, especially for lengthy keys. In
our hash table implementations, we compute the hash code when first inserting
an item, and recompute each item’s hash code each time we resize
our table. Python’s dict class makes an interesting trade-off. The hash
code is computed once, when an item is inserted, and the hash code is
stored as an extra field of the item composite, so that it need not be recomputed.
Reimplement our HashTableBase class to use such an approach.
"""