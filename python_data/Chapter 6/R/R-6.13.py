#-*-coding: utf-8 -*-
"""
Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1,2,3,5,4,6,7,8).

"""
D.add_last(D.delete_first())
D.add_last(D.delete_first())
D.add_last(D.delete_first())  # D = [4,5,6,7,8,1,2,3]

Q.enqueue(D.delete_first())  # Q = [4], D = [5,6,7,8,1,2,3]
D.add_last(D.delete_first())  # Q = [4], D = [6,7,8,1,2,3,5]
D.add_first(Q.dequeue())  # Q = [], D = [4,6,7,8,1,2,3,5]

D.add_first(D.delete_last())
D.add_first(D.delete_last())
D.add_first(D.delete_last())  # D = [1,2,3,5,4,6,7,8]









