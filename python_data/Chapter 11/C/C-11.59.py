#-*-coding: utf-8 -*-

"""
As a positional structure, our TreeMap implementation has a subtle flaw.
A position instance p associated with an key-value pair (k,v) should remain
valid as long as that item remains in the map. In particular, that
position should be unaffected by calls to insert or delete other items in the
collection. Our algorithm for deleting an item from a binary search tree
may fail to provide such a guarantee, in particular because of our rule for
using the inorder predecessor of a key as a replacement when deleting a
key that is located in a node with two children. Given an explicit series of
Python commands that demonstrates such a flaw
"""
