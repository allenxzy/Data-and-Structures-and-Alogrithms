#-*-coding: utf-8 -*-
#R-5.3基于代码5.1证明Python的列表偶尔会缩小(当元素被从列表弹出式）底层数组的大小
import sys
data = []
for k in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(a)
print "This is the depart lines\n-------------------------------"
while len(data) > 0:
    c = len(data)
    d = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(c, d))
    data.pop()





