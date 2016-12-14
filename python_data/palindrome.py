#-*-coding: utf-8-*-
#C-4.17递归判定回文字符串
def Palindrome(s):
    s = list(s)
    if len(s) == 0:
        print 'This string is None'
    elif len(s) % 2 == 0:
        mid = (len(s) / 2) - 1
        if s[mid] == s[mid + 1]:
            s.remove(s[mid])
            s.remove(s[mid + 1])
            Palindrome(s)
        else:
            return False
    else:
        mid = (len(s) - 1) / 2
        if s[mid - 1] == s[mid + 1]:
            s.remove(s[mid - 1])
            s.remove(s[mid + 1])
            Palindrome(s)
        else:
            return False
    return 'OK'

if __name__ == '__main__':
    p = Palindrome('hekkkofdeodddddddddddddddddd')
    print p
    m = Palindrome('abccbadd')
    print m

