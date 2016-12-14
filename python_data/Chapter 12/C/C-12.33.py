#-*-coding: utf-8 -*-

"""
Our high-level description of quick-sort describes partitioning the elements
into three sets L, E, and G, having keys less than, equal to, or
greater than the pivot, respectively. However, our in-place quick-sort implementation
of Code Fragment 12.6 does not gather all elements equal
to the pivot into a set E. An alternative strategy for an in-place, threeway
partition is as follows. Loop through the elements from left to right
maintaining indices i, j, and k and the invariant that all elements of slice
S[0:i] are strictly less than the pivot, all elements of slice S[i:j] are equal
to the pivot, and all elements of slice S[j:k] are strictly greater than the
pivot; elements of S[k:n] are yet unclassified. In each pass of the loop,
classify one additional element, performing a constant number of swaps
as needed. Implement an in-place quick-sort using this strategy.
"""