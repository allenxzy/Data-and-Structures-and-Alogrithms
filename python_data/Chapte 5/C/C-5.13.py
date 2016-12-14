#-*-coding: utf-8 -*-
#C-5.13对代码5.1分析，当data非空时，内存的扩展是否受影响

import sys
data = [1,2,3,4]
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)


"""
data = []:

Length:   0; Size in bytes:   72
Length:   1; Size in bytes:  104
Length:   2; Size in bytes:  104
Length:   3; Size in bytes:  104
Length:   4; Size in bytes:  104
Length:   5; Size in bytes:  136
Length:   6; Size in bytes:  136
Length:   7; Size in bytes:  136
Length:   8; Size in bytes:  136
Length:   9; Size in bytes:  200
Length:  10; Size in bytes:  200
Length:  11; Size in bytes:  200
Length:  12; Size in bytes:  200
Length:  13; Size in bytes:  200
Length:  14; Size in bytes:  200
Length:  15; Size in bytes:  200
Length:  16; Size in bytes:  200
Length:  17; Size in bytes:  272
Length:  18; Size in bytes:  272
Length:  19; Size in bytes:  272
"""
"""
data = [1]:

Length:   1; Size in bytes:   80
Length:   2; Size in bytes:  112
Length:   3; Size in bytes:  112
Length:   4; Size in bytes:  112
Length:   5; Size in bytes:  112
Length:   6; Size in bytes:  144
Length:   7; Size in bytes:  144
Length:   8; Size in bytes:  144
Length:   9; Size in bytes:  144
Length:  10; Size in bytes:  208
Length:  11; Size in bytes:  208
Length:  12; Size in bytes:  208
Length:  13; Size in bytes:  208
Length:  14; Size in bytes:  208
Length:  15; Size in bytes:  208
Length:  16; Size in bytes:  208
Length:  17; Size in bytes:  208
Length:  18; Size in bytes:  280
Length:  19; Size in bytes:  280
Length:  20; Size in bytes:  280
"""

"""
data = [1,2]

Length:   2; Size in bytes:   88
Length:   3; Size in bytes:  120
Length:   4; Size in bytes:  120
Length:   5; Size in bytes:  120
Length:   6; Size in bytes:  120
Length:   7; Size in bytes:  152
Length:   8; Size in bytes:  152
Length:   9; Size in bytes:  152
Length:  10; Size in bytes:  152
Length:  11; Size in bytes:  216
Length:  12; Size in bytes:  216
Length:  13; Size in bytes:  216
Length:  14; Size in bytes:  216
Length:  15; Size in bytes:  216
Length:  16; Size in bytes:  216
Length:  17; Size in bytes:  216
Length:  18; Size in bytes:  216
Length:  19; Size in bytes:  288
Length:  20; Size in bytes:  288
Length:  21; Size in bytes:  288
"""