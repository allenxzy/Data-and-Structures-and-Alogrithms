#-*-coding: utf-8 -*-

"""
Suppose we are given a directed graph G with n vertices, and let M be the
n×n adjacency matrix corresponding to G .
a. Let the product of M with itself (M**2) be defined, for 1 ≤ i, j ≤ n, as
follows:
M**2(i, j) = M(i,1) M(1, j)⊕···⊕ M(i,n) M(n, j),
where “⊕” is the Boolean or operator and “” is Boolean and.
Given this definition, what does M**2(i, j) = 1 imply about the vertices
i and j? What if M2(i, j) = 0?
b. Suppose M4 is the product of M**2 with itself. What do the entries of
M4 signify? How about the entries of M**5 = (M**4)(M)? In general,
what information is contained in the matrix Mp?
c. Now suppose that G is weighted and assume the following:
1: for 1 ≤ i ≤ n, M(i,i) = 0.
2: for 1 ≤ i, j ≤ n, M(i, j) = weight(i, j) if (i, j) is in E.
3: for 1 ≤ i, j ≤ n, M(i, j) = ∞ if (i, j) is not in E.
Also, let M2 be defined, for 1 ≤ i, j ≤ n, as follows:
M2
(i, j) = min{M(i,1) + M(1, j),...,M(i,n) + M(n, j)}.
If M**2(i, j) = k, what may we conclude about the relationship between
vertices i and j?
"""