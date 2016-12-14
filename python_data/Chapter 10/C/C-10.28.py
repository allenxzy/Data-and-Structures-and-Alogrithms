#-*-coding: utf-8 -*-

"""
On page 406 of Section 10.1.3, we give an implementation of the method
setdefault as it might appear in the MutableMapping abstract base class.
While that method accomplishes the goal in a general fashion, its effi-
ciency is less than ideal. In particular, when the key is new, there will be
a failed search due to the initial use of__getitem__, and then a subsequent
insertion via__setitem__. For a concrete implementation, such as
the UnsortedTableMap, this is twice the work because a complete scan
of the table will take place during the failed__getitem__, and then another
complete scan of the table takes place due to the implementation of__setitem__.
A better solution is for the UnsortedTableMap class to override
setdefault to provide a direct solution that performs a single search.
Give such an implementation of UnsortedTableMap.setdefault.
"""