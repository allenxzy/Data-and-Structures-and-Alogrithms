#-*-coding: utf-8 -*-

"""
Write a program that performs a simple n-body simulation, called “Jumping
Leprechauns.” This simulation involves n leprechauns, numbered 1 to
n. It maintains a gold value gi for each leprechaun i, which begins with
each leprechaun starting out with a million dollars worth of gold, that is,
gi = 1000000 for each i = 1,2,...,n. In addition, the simulation also
maintains, for each leprechaun, i, a place on the horizon, which is represented
as a double-precision floating-point number, xi. In each iteration
of the simulation, the simulation processes the leprechauns in order. Processing
a leprechaun i during this iteration begins by computing a new
place on the horizon for i, which is determined by the assignment

                              xi = xi +rgi,

where r is a random floating-point number between −1 and 1. The leprechaun
i then steals half the gold from the nearest leprechauns on either
side of him and adds this gold to his gold value, gi. Write a program that
can perform a series of iterations in this simulation for a given number,
n, of leprechauns. You must maintain the set of horizon positions using a
sorted map data structure described in this chapter
"""