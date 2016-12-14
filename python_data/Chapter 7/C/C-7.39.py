#-*-coding: utf-8 -*-

"""
To better model a FIFO queue in which entries may be deleted before
reaching the front, design a PositionalQueue class that supports the complete
queue ADT, yet with enqueue returning a position instance and support
for a new method, delete(p), that removes the element associated
with position p from the queue. You may use the adapter design pattern
(Section 6.1.2), using a PositionalList as your storage.
"""