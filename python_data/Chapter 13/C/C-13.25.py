#-*-coding: utf-8 -*-


"""
The Knuth-Morris-Pratt pattern-matching algorithm can be modified to
run faster on binary strings by redefining the failure function as:
f(k) = the largest j < k such that P[0: j]pj is a suffix of P[1:k+1],
where pj denotes the complement of the j
th bit of P. Describe how to
modify the KMP algorithm to be able to take advantage of this new failure
function and also give a method for computing this failure function. Show
that this method makes at most n comparisons between the text and the
pattern (as opposed to the 2n comparisons needed by the standard KMP
algorithm given in Section 13.2.3).
"""