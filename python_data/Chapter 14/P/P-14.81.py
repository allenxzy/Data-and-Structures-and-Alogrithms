#-*-coding: utf-8 -*-

"""
Write a program that builds the routing tables for the nodes in a computer
network, based on shortest-path routing, where path distance is measured
by hop count, that is, the number of edges in a path. The input for this
problem is the connectivity information for all the nodes in the network,
as in the following example:

241.12.31.14: 241.12.31.15 241.12.31.18 241.12.31.19

which indicates three network nodes that are connected to 241.12.31.14,
that is, three nodes that are one hop away. The routing table for the node at
address A is a set of pairs (B,C), which indicates that, to route a message
from A to B, the next node to send to (on the shortest path from A to B)
is C. Your program should output the routing table for each node in the
network, given an input list of node connectivity lists, each of which is
input in the syntax as shown above, one per line.
"""