#-*-coding: utf-8 -*-

"""
In Section 11.1.2 we claim that the find range method of a binary search
tree executes in O(s+h) time where s is the number of items found within
the range and h is the height of the tree. Our implementation, in Code
Fragment 11.6 begins by searching for the starting key, and then repeatedly
calling the after method until reaching the end of the range. Each call
to after is guaranteed to run in O(h) time. This suggests a weaker O(sh)
bound for find_range, since it involves O(s) calls to after. Prove that this
implementation achieves the stronger O(s+h) bound.
"""