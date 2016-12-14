#-*-coding: utf-8 -*-

"""
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def is_even(k):
    k = int(k)
    while k > 0:
        k = k - 2
    if k == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    # e = is_even(0)
    # print e
    # e1 = is_even(2)
    # print e1
    e2 = is_even(3)
    print e2
