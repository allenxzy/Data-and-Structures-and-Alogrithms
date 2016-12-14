#-*-coding: utf-8-*-
#假设一个空栈S共有25次S.push(e)操作，12次S.top()操作，10次S.pop()操作，3次raise Empty error.计算现在S的大小
"""
1.3次Empty error 都是S.top()造成
len(S) == 13
2.2次Empty error 是S.top()造成,1次是S.pop()造成
len(S) == 14
3.1次Empty error 是S.top()造成,2次是S.pop()造成
len(S) == 15
4.3次Empty error 都是S.pop()造成
len(S) == 16


"""