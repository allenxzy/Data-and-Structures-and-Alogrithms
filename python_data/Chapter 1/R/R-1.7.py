#-*-coding: utf-8 -*-

"""
Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.
"""
sum_ = sum([x ** 2 for x in range(1, 5, 2)])
print sum_