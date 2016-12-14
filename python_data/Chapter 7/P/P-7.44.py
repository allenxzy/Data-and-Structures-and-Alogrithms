#-*-coding: utf-8 -*-

"""
Write a simple text editor that stores and displays a string of characters
using the positional list ADT, together with a cursor object that highlights
a position in this string. A simple interface is to print the string and then
to use a second line of output to underline the position of the cursor. Your
editor should support the following operations:

• left: Move cursor left one character (do nothing if at beginning).
• right: Move cursor right one character (do nothing if at end).
• insert c: Insert the character c just after the cursor.
• delete: Delete the character just after the cursor (do nothing at end).
"""