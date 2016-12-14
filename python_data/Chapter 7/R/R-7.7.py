#-*-coding: utf-8 -*-

"""
Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that
has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty
queue. Implement such a method for the LinkedQueue class of Section
7.1.2 without the creation of any new nodes.
"""

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly liked node.
        (omitted here; identical to that of LinkedStack._Node)
        """

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0   #number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove)the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element   #front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue(i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():   #special case as queue is empty
            self._tail = None
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)   #node will be new tail node
        if self.is_empty():
            self._head = newest   #special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest   #updata refrence to tail node
        self._size += 1

    # def rotate(self):
    #     if self.is_empty():
    #         raise Empty('Queue is empty')
    #     else:
    #         return self.enqueue(self.dequeue())