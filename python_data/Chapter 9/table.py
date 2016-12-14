#-*-coding: utf-8 -*-

"""
Table 9.1
"""

"""

Operation              Running Time

len                    O(1)
is_empty               O(1)
add                    O(1)
min                    O(1)
remove_min             O(n)

"""

"""
Table 9.2
"""

"""

Operation           Unsorted List         Sorted List

len                 O(1)                  O(1)
is_empty            O(1)                  O(1)
add                 O(1)                  O(1)
min                 O(1)                  O(1)
remove_min          O(1)                  O(1)

"""

"""
Table 9.3
"""

"""

Operation                    Running Time

len(P), P.is_empty()         O(1)
P.min()                      O(1)
P.add()                      O(logn)*
P.remove_min()               O(logn)*
                             * amortized, if array-based

"""

"""
Table 9.4
"""

"""

Operation                             Running Time

len(P), P.is_empty(), P.min()         O(1)
P.add(k, v)                           0(logn)*
P.update(loc, k, v)                   O(logn)
P.remove(loc)                         O(logn)*
P.remove_min()                        O(logn)*
                                      *amortized with dynamic array
"""

