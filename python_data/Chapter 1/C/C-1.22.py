#-*-coding: utf-8 -*-

"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
"""

def product(a, b):
    c = []
    for i in range(len(a)):
        d = a[i] * b[i]
        c.append(d)
    return c

if __name__ == '__main__':
    e = product([1,2,3,4], [1,2,3,4])
    print e
