#-*-coding: utf-8 -*-

"""
The build_expression_tree method of the ExpressionTree class requires
input that is an iterable of string tokens. We used a convenient example,
(((3+1)x4)/((9-5)+2)) , in which each character is its own token,
so that the string itself sufficed as input to build_expression_tree.
In general, a string, such as (35 + 14) , must be explicitly tokenized
into list [ '( ', '35' , '+ ', '14' ,' )' ] so as to ignore whitespace and to
recognize multidigit numbers as a single token. Write a utility method,
tokenize(raw), that returns such a list of tokens for a raw string.
"""