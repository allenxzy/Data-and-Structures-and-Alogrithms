#-*-coding: utf-8 -*-

"""
Consider the page caching strategy based on the least frequently used
(LFU) rule, where the page in the cache that has been accessed the least
often is the one that is evicted when a new page is requested. If there are
ties, LFU evicts the least frequently used page that has been in the cache
the longest. Show that there is a sequence P of n requests that causes LFU
to miss Ω(n) times for a cache of m pages, whereas the optimal algorithm
will miss only O(m) times.
"""