#-*-coding: utf-8 -*-

"""
An old MST method, called Baruvka’s algorithm ˚ , works as follows on a
graph G having n vertices and m edges with distinct weights:
Let T be a subgraph of G initially containing just the vertices in V.

while T has fewer than n−1 edges do
for each connected component Ci of T do
Find the lowest-weight edge (u,v) in E with u in Ci and v not in
Ci.
Add (u,v) to T (unless it is already in T).
return T

Prove that this algorithm is correct and that it runs in O(mlogn) time
"""