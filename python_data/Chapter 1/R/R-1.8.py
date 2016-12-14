#-*-coding: utf-8 -*-

"""
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
"""
s = [1,2,3,4,5,6,7,8]
k = -2
print s[k]
# s[j] = s[k + len(s)]
print s[k + len(s)]
