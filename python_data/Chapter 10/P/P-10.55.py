#-*-coding: utf-8 -*-

"""
Write a spell-checker class that stores a lexicon of words, W, in a Python
set, and implements a method, check(s), which performs a spell check
on the string s with respect to the set of words, W. If s is in W, then
the call to check(s) returns a list containing only s, as it is assumed to
be spelled correctly in this case. If s is not in W, then the call to check(s)
returns a list of every word in W that might be a correct spelling of s. Your
program should be able to handle all the common ways that s might be a
misspelling of a word in W, including swapping adjacent characters in a
word, inserting a single character in between two adjacent characters in a
word, deleting a single character from a word, and replacing a character in
a word with another character. For an extra challenge, consider phonetic
substitutions as well.
"""