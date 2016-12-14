#-*-coding: utf-8 -*-

"""
For an ideal compression function, the capacity of the bucket array for a
hash table should be a prime number. Therefore, we consider the problem
of locating a prime number in a range [M,2M]. Implement a method for
finding such a prime by using the sieve algorithm. In this algorithm, we
allocate a 2M cell Boolean array A, such that cell i is associated with the
integer i. We then initialize the array cells to all be “true” and we “mark
off” all the cells that are multiples of 2, 3, 5, 7, and so on. This process
can stop after it reaches a number larger than √
2M. (Hint: Consider a
bootstrapping method for finding the primes up to √2M.)
"""