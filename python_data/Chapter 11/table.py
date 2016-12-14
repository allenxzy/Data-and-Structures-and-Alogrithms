#-*-coding: utf-8 -*-

"""
Table 11.1
"""

"""

Operation                                                 Running Time

k in T                                                    O(h)
T[k], T[k] = v                                            O(h)
T.delete(p), del T[k]                                     O(h)
T.find_position(k)                                        O(h)
T.first(), T.last(), T.find_min(), T.find_max()           O(h)
T.before(p), T.after(p)                                   O(h)
T.find_lt(k), T.find_le(k), T.find_gt(k), T.find_ge(k)    O(h)
T.find_range(start, stop)                                 O(s + h)
iter(T), reversed(T)                                      O(n)

"""

"""
Table 11.2
"""

"""

Operation                                                 Running Time

k in T                                                    O(logn)
T[k] = v                                                  O(logn)
T.delete(p), del T[k]                                     O(logn)
T.find_position(k)                                        O(logn)
T.first(), T.last(), T.find_min(), T.find_max()           O(logn)
T.before(p), T.after(p)                                   O(logn)
T.find_lt(k), T.find_le(), T.find_gt(k), T.find_ge(k)     O(logn)
T.find_range(star, stop)                                  O(s + logn)
iter(T), reversed(T)                                      O(n)

"""



