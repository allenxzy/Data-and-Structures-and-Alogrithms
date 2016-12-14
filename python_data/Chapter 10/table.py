#-*-coding: utf-8 -*-

"""
Table 10.1
"""

"""

                     Collisions
Shift            Total     Max

0                234735    623
1                165076    43
2                38471     13
3                7174      5
4                1379      3
5                190       3
6                502       2
7                560       2
8                5546      4
9                393       3
10               5194      5
11               11559     5
12               822       2
13               900       4
14               2001      4
15               19251     8
16               211781    37

"""

"""
Table 10.2
"""

"""

Operation         List         Hash Table
                            expected  worst case

__getitem__       O(n)      O(1)      O(n)
__setitem__       O(n)      O(1)      O(n)
__delitem__       O(n)      O(1)      O(n）
__len__           O(1)      O(1)      O(n)
__iter__          O(n)      O(n)      O(n)

"""

"""
Table 10.3
"""

"""

Opertation                                Running Time

len(M)                                    O(1)
k in M                                    O(logn)
M[k] = v                                  O(n) worst case: O(logn) if existing k
del M[k]                                  O(n) worst case
M.find_min(), M.find_max()                O(1)
M.find_lt(k), M.find_gt(k)                O(logn)
M.find_le(k), M.find_ge(k)
M.find_range(start, stop)                 O(s + logn) where s items are reported
iter(M), reversed(M)                      O(n)

"""

"""
Table 10.4
"""

"""

Operation                                Running Time

len(M)                                   O(1)
k in M                                   O(logn) expected
M[k] = v                                 O(logn) expected
del M[k]                                 O(logn) expected
M.find_min(), M.find_max()               O(1)
M.find_lt(k), M.find_gt(k)               O(logn) expected
M.find_le(k), M.find_ge(k)
M.find_range(start, stop)                O(s + logn) expected, with s items reported
iter(M), reversed(M)                     O(n)

"""


