#-*-coding: utf-8 -*-

"""
An independent set of an undirected graph G = (V,E) is a subset I of V
such that no two vertices in I are adjacent. That is, if u and v are in I, then
(u,v) is not in E. A maximal independent set M is an independent set
such that, if we were to add any additional vertex to M, then it would not
be independent any more. Every graph has a maximal independent set.
(Can you see this? This question is not part of the exercise, but it is worth
thinking about.) Give an efficient algorithm that computes a maximal
independent set for a graph G. What is this method’s running time?
"""