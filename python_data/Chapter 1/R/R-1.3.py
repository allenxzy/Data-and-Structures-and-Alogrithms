#-*-coding: utf-8 -*-

"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
"""

def minmax(data):
    if len(data) > 2:
        for i in range(len(data) - 1):
            if data[i] >= data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        a = data[-1]
        for j in range(len(data) - 2):
            if data[j] <= data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        b = data[-2]
        return (b, a)
    elif len(data) == 2:
        if data[0] > data[1]:
            return (data[1], data[0])
        else:
            return (data[0], data[1])
    else:
        return (data[0], data[0])


if __name__ =='__main__':
    # e = minmax([2,4,5,6,4,7,12,2,8,1,33,44,23])
    # print e
    # e1 = minmax([0])
    # print e1
    e2 = minmax([4, 3])
    print e2
    #



