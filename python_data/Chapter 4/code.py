#-*-coding: utf-8 -*-

"""
Code Fragment 4.1
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


"""
Code Fragment 4.2
"""

def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length(followed by optional label)"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str())


"""
Code Fragment 4.3
"""

def binary_search(data, target, low, high):
    """Reutrn True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to fata[high] inclusive
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low , mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

"""
Code Fragment 4.5
"""

import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents"""
    total = os.paht.getsize(path)
    if os.paht.isdir(path):
        for filename in os.listdir(path):
            childpaht = os.paht.join(path, filename)
            total += disk_usage(childpaht)

    print ('{0: < 7}'.format(total).path)
    return total


