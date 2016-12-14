#-*-coding: utf-8-*-
#C-4.16-字符串翻转
def overturn(s):
    s = list(s)
    if len(s) != 0 and len(s) % 2 == 0:
        s[0], s[-1] = s[-1], s[0]





if __name__ == '__main__':
    p = overturn('hello,world')
    print p