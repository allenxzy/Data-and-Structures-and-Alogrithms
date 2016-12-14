#-*-coding: utf-8 -*-
#队列操作7
"""
L = []
In:               Out:
  L.enqueue(5)        [5]
  L.enqueue(3)        [5, 3]
  L.dequeue()         [3]
  L.enqueue(2)        [3, 2]
  L.enqueue(8）       [3, 2, 8]
  L.dequeue()        [2, 8[
  L.dequeue()        [2]
  L.enqueue(9)       [2, 9]
  L.enqueue(1)       [2, 9, 1]
  L.dequeue()        [9, 1]7
  L.enqueue(6)       [9, 1, 7, 6]
  L.dequeue()        [1, 7, 6]
  L.dequeue()        [7, 6]
  L.enqueue(4)       [7, 6, 4]
  L.dequeue()        [6, 4]
  L.dequeue()        [4]

"""