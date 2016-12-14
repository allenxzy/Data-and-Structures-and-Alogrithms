#-*-coding: utf-8 -*-


"""
Table 5.1
"""

"""
Code    C Data Type         Typical Number of Bytes
'b'     signed char         1
'B'     unsigned char       1
'u'     Unicode char        2 or 4
'h'     signed short int    2
'H'     unsigned short int  2
'i'     signed int          2 or 4
'I'     unsigned int        2 or 4
'l'     signed long int     4
'L'     unsigned long int   4
'f'     float               4
'd'     float               8
"""


"""
Table 5.3
"""

"""
Operation                           Running Time
len(data)                           O(1)
data[j]                             O(1)
data.count(value)                   O(n)
data.index(value)                   O(k + 1)
value in data                       O(k + 1)
data1 == data2                      O(K + 1)
(similarly !=, <, <=, >, >=)
data[j:k]                           O(k - j + 1)
data1 + data2                       O(n1 + n2)
c * data                            O(cn)
"""


