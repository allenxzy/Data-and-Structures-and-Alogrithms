#-*-coding: utf-8 -*-

"""
Our implementation of shortest_path_lengths in Code Fragment 14.13 relies
on use of “infinity” as a numeric value, to represent the distance bound
for vertices that are not (yet) known to be reachable from the source.
Reimplement that function without such a sentinel, so that vertices, other
than the source, are not added to the priority queue until it is evident that
they are reachable.
"""