#-*-coding: utf-8 -*-

"""
Consider the following greedy strategy for finding a shortest path from
vertex start to vertex goal in a given connected graph.

1: Initialize path to start.
2: Initialize set visited to {start}.
3: If start=goal, return path and exit. Otherwise, continue.
4: Find the edge (start,v) of minimum weight such that v is adjacent to
start and v is not in visited.
5: Add v to path.
6: Add v to visited.
7: Set start equal to v and go to step 3.

Does this greedy strategy always find a shortest path from start to goal?
Either explain intuitively why it works, or give a counterexample.
"""