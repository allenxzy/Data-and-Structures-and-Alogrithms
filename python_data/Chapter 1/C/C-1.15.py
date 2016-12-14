#-*-coding: utf-8 -*-

"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

def unique(data):
    new_data = []
    for i in range(len(data) - 1):
        n = data[i]
        if n not in new_data:
            new_data.append(n)
    if len(data) == len(new_data):
        return True
    else:
        return False

if __name__ == '__main__':
    # e = unique([1,2,3,4,5,6,7])
    # print e
    e1 = unique([1,2,3,4,5,6,2,5,7,8])
    print e1

