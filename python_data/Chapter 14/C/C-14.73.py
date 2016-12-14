#-*-coding: utf-8 -*-

"""
Karen has a new way to do path compression in a tree-based union/find
partition data structure starting at a position p. She puts all the positions
that are on the path from p to the root in a set S. Then she scans through
S and sets the parent pointer of each position in S to its parent’s parent
pointer (recall that the parent pointer of the root points to itself). If this
pass changed the value of any position’s parent pointer, then she repeats
this process, and goes on repeating this process until she makes a scan
through S that does not change any position’s parent value. Show that
Karen’s algorithm is correct and analyze its running time for a path of
length h.
"""