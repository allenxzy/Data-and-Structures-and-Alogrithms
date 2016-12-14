#-*-coding: utf-8 -*-

"""
George claims he has a fast way to do path compression in a partition
structure, starting at a position p. He puts p into a list L, and starts following
parent pointers. Each time he encounters a new position, q, he adds q
to L and updates the parent pointer of each node in L to point to q’s parent.
Show that George’s algorithm runs in Ω(h**2) time on a path of length h.
"""