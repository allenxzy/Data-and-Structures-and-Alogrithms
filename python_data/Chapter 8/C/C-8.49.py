#-*-coding: utf-8 -*-

"""
Let the rank of a position p during a traversal be defined such that the first
element visited has rank 1, the second element visited has rank 2, and so
on. For each position p in a tree T, let pre(p) be the rank of p in a preorder
traversal of T, let post(p) be the rank of p in a postorder traversal of T, let
depth(p) be the depth of p, and let desc(p) be the number of descendants
of p, including p itself. Derive a formula defining post(p) in terms of
desc(p), depth(p), and pre(p), for each node p in T.
"""