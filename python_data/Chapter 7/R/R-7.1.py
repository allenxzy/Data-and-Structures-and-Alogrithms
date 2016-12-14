#-*-coding: utf-8 -*-
"""
Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.

"""
class find_node:

    class _Node:
        """Lightweight nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        self._head = None
        self._size = 0

    def find_node(self):
        if self._head is None:
            raise Exception('The list is empty')
        elif self._head._next is None:
            return self._head._element
        else:
            while len(self._size):
                answer = self._head._next._element
                self._head = self._head._next
                self._size -= 1
                return answer


if __name__ == '__main__':
    pass







