#-*-coding: utf-8 -*-

"""
We can represent a path from the root to a given node of a binary tree
by means of a binary string, where 0 means “go to the left child” and 1
means “go to the right child.” For example, the path from the root to the
node storing (8,W ) in the heap of Figure 9.12a is represented by “101.”
Design an O(logn)-time algorithm for finding the last node of a complete
binary tree with n nodes, based on the above representation. Show how
this algorithm can be used in the implementation of a complete binary tree
by means of a linked structure that does not keep a reference to the last
node
"""