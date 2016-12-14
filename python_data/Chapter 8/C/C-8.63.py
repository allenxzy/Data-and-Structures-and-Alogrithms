#-*-coding: utf-8 -*-

"""
As mentioned in Exercise C-6.22, postfix notation is an unambiguous way
of writing an arithmetic expression without parentheses. It is defined so
that if “(exp1)op(exp2)” is a normal (infix) fully parenthesized expression
with operation op, then its postfix equivalent is “pexp1 pexp2 op”,
where pexp1 is the postfix version of exp1 and pexp2 is the postfix version
of exp2. The postfix version of a single number or variable is just
that number or variable. So, for example, the postfix version of the infix
expression “((5 + 2) ∗ (8 − 3))/4” is “5 2 + 8 3 − ∗ 4 /”. Implement a
postfix method of the ExpressionTree class of Section 8.5 that produces
the postfix notation for the given expression
"""