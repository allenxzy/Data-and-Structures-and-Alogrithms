#-*-coding: utf-8 -*-

"""
In the FavoritesListMTF class, we rely on public methods of the positional
list ADT to move an element of a list at position p to become the first element
of the list, while keeping the relative order of the remaining elements
unchanged. Internally, that combination of operations causes one node to
be removed and a new node to be inserted. Augment the PositionalList
class to support a new method, move_to_front(p), that accomplishes this
goal more directly, by relinking the existing node.
"""