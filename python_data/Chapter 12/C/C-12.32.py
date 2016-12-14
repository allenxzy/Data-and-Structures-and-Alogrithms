#-*-coding: utf-8 -*-

"""
Another way to analyze randomized quick-sort is to use a recurrence
equation. In this case, we let T(n) denote the expected running time
of randomized quick-sort, and we observe that, because of the worst-case
partitions for good and bad splits, we can write

T(n) ≤1/2 (T(3n/4) +T(n/4)) + 1/2 (T(n−1)) +bn,

where bn is the time needed to partition a list for a given pivot and concatenate
the result sublists after the recursive calls return. Show, by induction,
that T(n) is O(nlog n).
"""