#-*-coding: utf-8 -*-
#C-4.9递归实现输出序列最大值和最小值

def find_min(s):
    if len(s) >= 2:
        a = max(s[0],s[1])
        s.remove(a)
        find_min(s)
        return s[0]

def find_max(s):
    if len(s) >= 2:
        a = min(s[0],s[1])
        s.remove(a)
        find_max(s)
        return s[0]









if __name__ == '__main__':

    p = find_min([5, 4, 5, 4, 1, 7, 2, 9, 5, 456, 21, 0,34,12343, 22 ])
    m = find_max([5, 4, 5, 4, 1, 7, 2, 9, 5, 456, 21, 0,34,12343, 22 ])
    print p
    print m

