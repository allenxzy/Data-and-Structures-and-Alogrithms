#-*-coding: utf-8 -*-

"""
An array A is sparse if most of its entries are empty (i.e., None). A list
L can be used to implement such an array efficiently. In particular, for
each nonempty cell A[i], we can store an entry (i,e) in L, where e is the
element stored at A[i]. This approach allows us to represent A using O(m)
storage, where m is the number of nonempty entries in A. Provide such
a SparseArray class that minimally supports methods__getitem__(j) and
__setitem__(j, e) to provide standard indexing operations. Analyze the
efficiency of these methods.
"""