#-*-coding: utf-8 -*-

"""
We can simplify parts of our LinkedBinaryTree implementation if we
make use of of a single sentinel node, referenced as the_sentinel member
of the tree instance, such that the sentinel is the parent of the real root of
the tree, and the root is referenced as the left child of the sentinel. Furthermore,
the sentinel will take the place of None as the value of the_left
or_right member for a node without such a child. Give a new implementation
of the update methods_delete and_attach, assuming such a
representation.
"""