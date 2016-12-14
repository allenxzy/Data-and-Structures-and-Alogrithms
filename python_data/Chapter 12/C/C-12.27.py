#-*-coding: utf-8 -*-

"""
Augment the PositionalList class (see Section 7.4) to support a method
named merge with the following behavior. If A and B are PositionalList
instances whose elements are sorted, the syntax A.merge(B)should merge
all elements of B into A so that A remains sorted and B becomes empty.
Your implementation must accomplish the merge by relinking existing
nodes; you are not to create any new nodes.
"""