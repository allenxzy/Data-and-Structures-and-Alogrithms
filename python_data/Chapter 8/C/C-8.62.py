#-*-coding: utf-8 -*-

"""
Note that the build_expression_tree function of the ExpressionTree class
is written in such a way that a leaf token can be any string; for example,
it parses the expression '(a*(b+c))' . However, within the evaluate
method, an error would occur when attempting to convert a leaf token to
a number. Modify the evaluate method to accept an optional Python dictionary
that can be used to map such string variables to numeric values,
with a syntax such as T.evaluate({ 'a' :3, 'b' :1, 'c' :5}). In this way,
the same algebraic expression can be evaluated using different values.
"""