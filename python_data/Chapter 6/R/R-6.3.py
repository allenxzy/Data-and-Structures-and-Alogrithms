#-*-coing: utf-8 -*-
'''
Implement a function with signature transfer(S, T) that transfers all elements
from stack S onto stack T, so that the element that starts at the top
of S is the first to be inserted onto T, and the element at the bottom of S
ends up at the top of T.
'''

def transfer(s,t):
    v = []
    if len(s) == 0:
        raise IndexError
    if len(t) != 0:
        v = t
        t = []
        while len(s) > 1:
            a = s.pop()
            t.append(a)
        for i in v:
            t.append(i)
        b = s[0]
        t.append(b)
        return t
    else:
        while len(s):
            c = s.pop()
            t.append(c)
        return t

if __name__ == '__main__':
    # d = transfer([],[]) # s is None
    # print d
    # f = transfer([1,2,3,5,7], []) # t is None
    # print f
    e = transfer([1,2,3,4], [5,6,7]) # t is not None
    print e



