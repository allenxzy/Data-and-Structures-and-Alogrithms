#-*-coding: utf-8 -*-

"""
An inverted file is a critical data structure for implementing a search engine
or the index of a book. Given a document D, which can be viewed
as an unordered, numbered list of words, an inverted file is an ordered list
of words, L, such that, for each word w in L, we store the indices of the
places in D where w appears. Design an efficient algorithm for constructing
L from D
"""