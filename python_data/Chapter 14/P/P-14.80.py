#-*-coding: utf-8 -*-

"""
One way to construct a maze starts with an n×n grid such that each grid
cell is bounded by four unit-length walls. We then remove two boundary
unit-length walls, to represent the start and finish. For each remaining
unit-length wall not on the boundary, we assign a random value and create
a graph G, called the dual, such that each grid cell is a vertex in G
and there is an edge joining the vertices for two cells if and only if the
cells share a common wall. The weight of each edge is the weight of the
corresponding wall. We construct the maze by finding a minimum spanning
tree T for G and removing all the walls corresponding to edges in
T. Write a program that uses this algorithm to generate mazes and then
solves them. Minimally, your program should draw the maze and, ideally,
it should visualize the solution as well.
"""