#-*-coding: utf-8 -*-

"""
The memory usage for the LinkedBinaryTree class can be streamlined by
removing the parent reference from each node, and instead having each
Position instance keep a member,_path, that is a list of nodes representing
the entire path from the root to that position. (This generally saves memory
because there are typically relatively few stored position instances.)
Reimplement the LinkedBinaryTree class using this strategy
"""