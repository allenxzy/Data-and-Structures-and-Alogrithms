#-*-coding: utf-8 -*-

"""
Our Position classes for lists and trees support the__eq__method so that
two distinct position instances are considered equivalent if they refer to the
same underlying node in a structure. For positions to be allowed as keys
in a hash table, there must be a definition for the__hash__method that
is consistent with this notion of equivalence. Provide such a__hash__
method.
"""