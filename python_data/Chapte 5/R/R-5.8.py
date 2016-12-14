#-*-coding: utf-8 -*-
#pop方法的效率

from time import time

# def use(func):
#     def use_time():
#         start = time()
#         func()
#         end = time()
#         print (start - end)
#         return (start - end)
#     return use_time


#在列表末尾执行pop方法

# l = [1,3,4,5,6,7,8,9]
# start = time()
# l.pop()
# end = time()
# print (start - end)
#cost: -1.90734863281e-06

#在列表末尾执行pop方法
# l = [1,3,4,5,6,7,8,9]
# start = time()
# l.pop(l[3])
# end = time()
# print (start - end)
# cost: -2.86102294922e-06

#在列表开头执行pop方法
# l = [1,3,4,5,6,7,8,9]
# start = time()
# l.pop(l[0])
# end = time()
# print (start - end)
# cost: -3.09944152832e-06


