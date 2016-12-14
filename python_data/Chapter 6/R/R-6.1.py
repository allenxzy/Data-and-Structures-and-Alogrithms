#-*-coding: utf-8 -*-
#一些栈操作
"""
L = []:
In:                Out:
   push(5)             [5]
   push(3)             [5, 3]
   pop()               [5]
   push(2)             [5, 2]
   push(8)             [5,2,8]
   pop()               [5, 2]
   pop()               [5]
   push(9)             [5, 9]
   push(1)             [5, 9, 1]
   pop()               [5, 9]
   push(7)             [5. 9, 7]
   push(6)             [5, 9, 7, 6]
   pop()               [5, 9, 7]
   pop()               [5, 9]
   push(4)             [5, 9, 4]
   pop()               [5, 9]
   pop()               [5]

"""