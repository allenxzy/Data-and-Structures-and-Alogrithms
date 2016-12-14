#-*-coding: utf-8 -*-

"""
Table 14.1
"""

"""

Operation              Edge List        Adj. List      Adj. Map      Adj. Matrix

vertex_count()         O(1)             O(1)           O(1)          O(1)
edge_count()           O(1)             O(1)           O(1)          O(1)
vertices()             O(n)             O(n)           O(n)          O(n)
edges()                O(m)             O(m)           O(m)          O(m)
get_edge(u, v)         O(m)             O(min(du, dv)) O(1) exp.     O(1)
degree(v)              O(m)             O(1)           O(1)          O(n)
incident_edges(v)      O(m)             O(dv)          O(dv)         O(n)
insert_vertex(x)       O(1)             O(1)           O(1)          O(n ** 2)
remove_vertex(v)       O(m)             O(dv)          O(dv)         O(n ** 2)
insert_edge(u, v, x)   O(1)             O(1)           O(1) .exp     O(1)
remove_edge(e)         O(1)             O(1)           O(1) .exp     O(1)

"""

"""
Table 14.2
"""

"""

Operation                                                            Running Time

vertex_count(), edge_count()                                         O(1)
vertices()                                                           O(n)
edges()                                                              O(m)
get_edge(u, v) degree(v), incident_edges(v)                          O(m)
insert_vertex(x), insert_edge(u, v, x) remove_edge(e)                O(1)
remove_vertex(v)                                                     O(m)

"""

"""
Table 14.3
"""

"""

Operation                                             Running Time

vertex_count(), edge_count()                          O(1)
vertices()                                            O(n)
edges()                                               O(m)
get_edge(u, v)                                        O(min(deg(u), deg(v)))
degree(v)                                             O(1)
incident_edges(v)                                     O(deg(v))
insert_vertex(x), insert_edge(u, v, x)                O(1)
remove_edge(e)                                        O(1)
remove_vertex(v)                                      O(deg(v))

"""



