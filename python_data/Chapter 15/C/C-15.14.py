#-*-coding: utf-8 -*-

"""
Describe a modified version of the B-tree insertion algorithm so that each
time we create an overflow because of a split of a node w, we redistribute
keys among all of w’s siblings, so that each sibling holds roughly the same
number of keys (possibly cascading the split up to the parent of w). What
is the minimum fraction of each block that will always be filled using this
scheme?
"""