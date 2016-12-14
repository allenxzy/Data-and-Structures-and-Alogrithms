#-*-coding: utf-8 -*-

"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

def sum_squar_small(n):
    n = abs(int(n))
    s = []
    if n > 1:
        for i in range(1, n, 2):
            a = i * i
            s.append(a)
        return sum(s)
    else:
        return 0


if __name__ == '__main__':
    # e = sum_squar_small(1)
    # print e
    # e1 = sum_squar_small(3)
    # print e1
    e2 = sum_squar_small(5)
    print e2