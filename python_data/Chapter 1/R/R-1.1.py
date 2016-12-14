#-*-coding: utf-8 -*-

"""
Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise
"""

def is_multiple(n, m):
    n = int(n)
    m = int(m)
    if n % m == 0 and n != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    e = is_multiple(4, 2)
    print e
    # e1 = is_multiple(4, 4)
    # print e1
    # e2 = is_multiple(0, 4)
    # print e2
    # e3 = is_multiple(4, 0)
    # print e3
    # e4 = is_multiple(4, 5)
    # print e4




