#-*-coding: utf-8 -*-

"""
Let S be a set of n points in the plane with distinct integer x- and ycoordinates.
Let T be a complete binary tree storing the points from S
at its external nodes, such that the points are ordered left to right by increasing
x-coordinates. For each node v in T, let S(v) denote the subset of
S consisting of points stored in the subtree rooted at v. For the root r of
T, define top(r) to be the point in S = S(r) with maximum y-coordinate.
For every other node v, define top(r) to be the point in S with highest ycoordinate
in S(v) that is not also the highest y-coordinate in S(u), where
u is the parent of v in T (if such a point exists). Such labeling turns T into
a priority search tree. Describe a linear-time algorithm for turning T into
a priority search tree. Implement this approach.
"""