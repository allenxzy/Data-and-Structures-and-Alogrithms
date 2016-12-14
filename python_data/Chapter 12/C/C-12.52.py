#-*-coding: utf-8 -*-

"""
Space aliens have given us a function, alien_split, that can take a sequence
S of n integers and partition S in O(n) time into sequences S1,S2,...,Sk of
size at most [n/k] each, such that the elements in Si are less than or equal
to every element in Si+1, for i = 1,2,...,k −1, for a fixed number, k < n.
Show how to use alien split to sort S in O(nlog n/logk) time.
"""