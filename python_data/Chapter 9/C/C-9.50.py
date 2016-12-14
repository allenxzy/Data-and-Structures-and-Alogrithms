#-*-coding: utf-8 -*-

"""
An online computer system for trading stocks needs to process orders of
the form “buy 100 shares at $x each” or “sell 100 shares at $y each.” A
buy order for $x can only be processed if there is an existing sell order
with price $y such that y ≤ x. Likewise, a sell order for $y can only be
processed if there is an existing buy order with price $x such that y ≤ x.
If a buy or sell order is entered but cannot be processed, it must wait for a
future order that allows it to be processed. Describe a scheme that allows
buy and sell orders to be entered in O(logn) time, independent of whether
or not they can be immediately processed.
"""