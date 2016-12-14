#-*-coding: utf-8-*-
#R-5.2基于5.1代码，实现只输入，当内存扩充时的数据。
import sys
data = []
s = set()
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    if b not in s:
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    s.add(b)
    data.append(None)



