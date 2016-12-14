#-*-coding: utf-8 -*-

"""
In our AVL implementation, each node stores the height of its subtree,
which is an arbitrarily large integer. The space usage for an AVL tree
can be reduced by instead storing the balance factor of a node, which is
defined as the height of its left subtree minus the height of its right subtree.
Thus, the balance factor of a node is always equal to −1, 0, or 1, except
during an insertion or removal, when it may become temporarily equal to
−2 or +2. Reimplement the AVLTreeMap class storing balance factors
rather than subtree heights.
"""