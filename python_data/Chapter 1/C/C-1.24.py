#-*-coding: utf-8 -*-

"""
Write a short Python function that counts the number of vowels in a given
character string.
"""

def count_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for i in s:
        if i in v:
            count += 1
    return count

if __name__ == '__main__':
    # e = count_vowels('aaaaaaaastiobcdefghiuuuuzk')
    # print e
    e1 = count_vowels('AaaaaaDEEUIIOFRHaastiobcdefghiuuuuzk')
    print e1

