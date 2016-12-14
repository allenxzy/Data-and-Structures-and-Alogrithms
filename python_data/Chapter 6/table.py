#-*-coding: utf-8 -*-

"""
Table 6.1
"""

"""

Stack Method          Realization with Python list

S.push(e)             L.append(e)
S.pop()               L.pop()
S.top()               L[-1]
S.is_empty()          len(L) == 0
len(S)                len(L)

"""

"""
Table 6.2
"""

"""

Operation           Running Time

S.push(e)           O(1)*
S.pop()             O(1)*
S.top()             O(1)
S.is_empty()        O(1)
len(S)              O(1)
                    * amortized

"""

"""
Table 6.3
"""

"""

Operation            Running Time

Q.enqueue(e)         O(1)*
Q.dequeue()          O(1)
Q.first()            O(1)
Q.is_empty()         O(1)
len(Q)               O(1)
                     *amoritized


"""

"""
Table 6.4
"""

"""

Our Deque ADT        collections.deque           Description

len(D)               len(D)                      number of elements
D.add_first()        D.appendleft()              add to beginning
D.add_last()         D.append()                  add to end
D.delete_first()     D.popleft()                 remove from beginning
D.delete_last()      D.pop()                     remove from end
D.first()            D[0]                        access first element
D.last()             D[-1]                       access last element
                     D[j]                        access arbitrary entry by index
                     D[j] = val                  modify arbitrary entry by index
                     D.clear()                   clear all contents
                     D.rotate(k)                 circularly shift rightward k steps
                     D.remove(e)                 remove first matching element
                     D.count(e)                  count number of matches for e


"""
