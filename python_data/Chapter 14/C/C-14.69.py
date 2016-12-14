#-*-coding: utf-8 -*-

"""
NASA wants to link n stations spread over the country using communication
channels. Each pair of stations has a different bandwidth available,
which is known a priori. NASA wants to select n−1 channels (the minimum
possible) in such a way that all the stations are linked by the channels
and the total bandwidth (defined as the sum of the individual bandwidths
of the channels) is maximum. Give an efficient algorithm for this problem
and determine its worst-case time complexity. Consider the weighted
graph G = (V,E), where V is the set of stations and E is the set of channels
between the stations. Define the weight w(e) of an edge e in E as the
bandwidth of the corresponding channel
"""