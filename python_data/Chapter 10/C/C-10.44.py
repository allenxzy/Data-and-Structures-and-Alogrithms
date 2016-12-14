#-*-coding: utf-8 -*-

"""
Show that the methods above(p) and prev(p) are not actually needed to
efficiently implement a map using a skip list. That is, we can implement
insertions and deletions in a skip list using a strictly top-down, scanforward
approach, without ever using the above or prev methods. (Hint:
In the insertion algorithm, first repeatedly flip the coin to determine the
level where you should start inserting the new entry.)
"""