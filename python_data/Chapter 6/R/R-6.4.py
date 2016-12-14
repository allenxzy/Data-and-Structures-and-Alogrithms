#-*-coding: utf-8 -*-
#R-6.4递归方法移除栈中的所有元素

def recursive_remove(s):
    if not s:
        return True
    else:
        s.pop()
        recursive_remove(s)
    return True

if __name__ == '__main__':
    a = recursive_remove([]) # s is None
    print a
    b = recursive_remove([1,2,3,4,5,6,7]) # s is not None
    print b