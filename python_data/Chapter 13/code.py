#-*-coding: utf-8 -*-

"""
Code Fragment 13.1
"""

def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else - 1)."""
    n, m = len(T), len(P)          #introuduce convenient notations
    for i in range(n - m + 1):     #try every potential starting index within T
        k = 0                     #an index into pattern P
        while k < m and T[i + k] == P[k]:      #kth character of P matches
            k += 1
        if k == m:               #if we reached the end of pattern.
            return i             #substring T[i:i + m] matches P
    return -1                    #failed to find a match starting with any i


"""
Code Fragment 13.2
"""

def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)          #introduce convenient notations
    if m == 0: return 0            #trivial search for empty string
    last = {}                      #build 'last' dictionary
    for k in range(m):
        last[P[k]] = k            #later occurrence overwrites
    #align end of pattern at index m - 1 of text
    i = m -1                    #an index into T
    k = m -1                    #an index into P
    while i < n:
        if T[i] == P[k]:        #a matching character
            if k == 0:
                return i        #pattern begins at index i of text
            else:
                i -= 1          #examine previous character
                k -= 1          #of both T and P
        else:
            j = last.get(T[i], -1)      #last(T[i]) is -1 if not found
            i += m - min(k, j + 1)      #case analysis for jump step
            k = m -1                    #restart at end of pattern
    return -1


"""
Code Fragment 13.3
"""

def find_kmp(T, P):
    """Return the lowest index of T at which substring P begins (or else - 1)."""
    n, m = len(T), len(P)             #introduce convenient notations
    if m == 0: return 0               #trivial search for empty string
    fail = compute_kmp_fail(P)        #rely on utility to precompute
    j = 0                             #index into text
    k = 0                             #index into pattern
    while j < n:
        if T[j] == P[k]:              #P[0:1 + k] matched thus far
            if k == m - 1:            #match is complete
                return j - m + 1
            j += 1                    #try to extend match
            k += 1
        elif k > 0:
            k = fail[k - 1]           #reuse suffix of P[0:k]
        else:
            j += 1
    return -1                         #reached end without match


"""
Code Fragment 13.4
"""

def compute_kmp_fail(P):
    """Utility that computes and returns KMP 'fail' list."""
    m = len(P)
    fail = [0] * m           #by default, presume overlap of 0 ererywhere
    j = 1
    k = 0
    while j < m:           #compute f(j) during this pass, if nonzero
        if P[j] == P[k]:   #k + 1 characters match thus far
            fail[i] = k + 1
            j += 1
            k += 1
        elif k > 0:       #k follows a matching prefix
            k = fail[k - 1]
        else:             #no match found starting at j
            return fail


"""
Code Fragment 13.5
"""

def matrix_chain(d):
    """d is a list of n + 1 mumbers such that size of kth matrix is d[k]-by-d[k + 1].

    Return an n-by-n table such that N[i][j] represents the minimun number of
    multiplications needed to compute the product of Ai throug Aj inclusive.
    """

    n = len(d) - 1                       #number of matrices
    N = [[0] * n for i in range(n)]     #initialize n-by-n result to zero
    for b in range(1, n):               #number of produxts in subchain
        for i in range(n - b):          #start of subchain
            j = i + b                   #end of subchain
            N[i][j] = min(N[i][k] + N[k + 1][j] + d[i] * d[k + 1] *d[j + 1] for k in range(i, j))
    return N


"""
Code Fragment 13.6
"""

def LCS(X, Y):
    """Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]."""
    n, m = len(X), len(Y)           #inctroduce convenient notations
    L = [[0] * (m + 1) for k in range(n + 1)]   #(n+ 1) x ( m + 1) table
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:              #align this match
                L[j + 1][k + 1] = L[j][k] + 1
            else:                          #choose to ignore one character
                L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])
        return L


"""
Code Fragment 13.7
"""

def LCS_solution(X, Y, L):
    """Return the longest common substring of X and Y, given LCS table L."""
    solution = []
    j,k = len(X), len(Y)
    while L[j][k] > 0:            #common characters remain
        if X[j - 1] == Y[k - 1]:
            solution. append(X[j - 1])
            j -= 1
            k -= 1
        elif L[j -1][k] >= L[j][k -1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))     #return left-to-right version




