#-*-coding: utf-8 -*-

"""
Computer networks should avoid single points of failure, that is, network
vertices that can disconnect the network if they fail. We say an undirected,
connected graph G is biconnected if it contains no vertex whose
removal would divide G into two or more connected components. Give an
algorithm for adding at most n edges to a connected graph G, with n ≥ 3
vertices and m ≥ n − 1 edges, to guarantee that G is biconnected. Your
algorithm should run in O(n+m) time.
"""