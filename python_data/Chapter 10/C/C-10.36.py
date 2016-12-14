#-*-coding: utf-8 -*-

"""
The quadratic probing strategy has a clustering problem related to the way
it looks for open slots. Namely, when a collision occurs at bucket h(k), it
checks buckets A[(h(k) +i**2) mod N], for i = 1,2,...,N −1.
a. Show that i**2 mod N will assume at most (N + 1)/2 distinct values,
for N prime, as i ranges from 1 to N − 1. As a part of this justification,
note that i**2 mod N = (N −i)2 mod N for all i.

b. A better strategy is to choose a prime N such that N mod 4 = 3 and
then to check the buckets A[(h(k) ± i**2) mod N] as i ranges from 1
to (N − 1)/2, alternating between plus and minus. Show that this
alternate version is guaranteed to check every bucket in A.
"""