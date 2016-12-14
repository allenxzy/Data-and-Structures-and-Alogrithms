#-*-coding: utf-8 -*-

"""
Write a program that can play Tic-Tac-Toe effectively. (See Section 5.6.)
To do this, you will need to create a game tree T, which is a tree where
each position corresponds to a game configuration, which, in this case,
is a representation of the Tic-Tac-Toe board. (See Section 8.4.2.) The
root corresponds to the initial configuration. For each internal position p
in T, the children of p correspond to the game states we can reach from
p’s game state in a single legal move for the appropriate player, A (the
first player) or B (the second player). Positions at even depths correspond
to moves for A and positions at odd depths correspond to moves for B.
Leaves are either final game states or are at a depth beyond which we do
not want to explore. We score each leaf with a value that indicates how
good this state is for player A. In large games, like chess, we have to use a
heuristic scoring function, but for small games, like Tic-Tac-Toe, we can
construct the entire game tree and score leaves as +1, 0, −1, indicating
whether player A has a win, draw, or lose in that configuration. A good
algorithm for choosing moves is minimax. In this algorithm, we assign a
score to each internal position p in T, such that if p represents A’s turn, we
compute p’s score as the maximum of the scores of p’s children (which
corresponds to A’s optimal play from p). If an internal node p represents
B’s turn, then we compute p’s score as the minimum of the scores of p’s
children (which corresponds to B’s optimal play from p).
"""