#-*-coding: utf-8 -*-

"""
Say that a pattern P of length m is a circular substring of a text T of length
n > m if P is a (normal) substring of T, or if P is equal to the concatenation
of a suffix of T and a prefix of T, that is, if there is an index 0 ≤ k < m,
such that P = T[n−m+k :n]+T [0:k]. Give an O(n+m)-time algorithm
for determining whether P is a circular substring of T.
"""