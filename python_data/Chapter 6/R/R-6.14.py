#-*-coding: utf-8 -*-
"""
Repeat the previous problem using the deque D and an initially empty
stack S
"""
S.append(D.delete_first())
S.append(D.delete_first())
S.append(D.delete_first())
S.append(D.delete_first())# S = [1,2,3,4];D = [5,6,7,8]

D.add_last(D.delete_first())  # S = [1,2,3,4]; D = [6,7,8,5]
D.add_first(S.pop())  # Q = [4],  S = [1,2,3]; D = [4,6,7,8,5]
D.add_first(D.delete_last())  # S = [1,2,3], D = [5,4,6,7,8]

D.add_first(S.pop())
D.add_first(S.pop())
D.add_first(S.pop())  #  S = [] D = [1,2,3,5,4,6,7,8]
