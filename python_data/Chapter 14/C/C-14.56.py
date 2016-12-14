#-*-coding: utf-8 -*-

"""
Tamarindo University and many other schools worldwide are doing a joint
project on multimedia. A computer network is built to connect these
schools using communication links that form a tree. The schools decide
to install a file server at one of the schools to share data among all the
schools. Since the transmission time on a link is dominated by the link
setup and synchronization, the cost of a data transfer is proportional to the
number of links used. Hence, it is desirable to choose a “central” location
for the file server. Given a tree T and a node v of T, the eccentricity of v
is the length of a longest path from v to any other node of T. A node of T
with minimum eccentricity is called a center of T.

a. Design an efficient algorithm that, given an n-node tree T, computes
a center of T.
b. Is the center unique? If not, how many distinct centers can a tree
have?
"""