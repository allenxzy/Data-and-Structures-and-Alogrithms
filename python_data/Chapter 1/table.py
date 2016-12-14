#-*-coding: utf-8 -*-


"""
Table1.1
"""

"""
Reserved Words

False  as       continue   else       from     in       not     return    yield
None   assert   def        except     global   is       or      try
True   break    del        finally    if       lambda   pass    while
and    class    elif       for        import   nonlocal raise   with
"""

"""
Table 1.2
"""

"""
Class            Description                               Immutable
bool             Boolean value                                ok
int              integer (arbitrary magnitude)                ok
float            floating-point number                        ok
list             mutable sequence of object                   no
tuple            immutable sequence of objects                ok
str              character string                             ok
set              inordered set of distinct objects            no
frozenset        immutable form of set class                  ok
dict             associative mapping (aka dictionary)         no
"""


"""
Table 1.3
"""

"""
Type                                Symbols
memeber access                      expr.member
function/method calls               expr(...)
container subscripts/slices         expr[...]
exponentiation                      **
unary operators                     +expr, -expr, ~expr
multiplication, division            *, /, //, %
addition, subtraction               +, -
bitwise shifting                    <<, >>
bitwise-and                         &
bitwise-xor                         ^
bitwise-or                          |
comparisons                         is, is not, ==, !=, <, <=, >, >=
containment                         in, not in
logical-not                         not expr
logical-and                         and
logical-or                          or
conditional                         val1 if cond else val2
assignments                         =, +=, -=, *=, etc.
"""


"""
Table 1.4
"""

"""
Calling Syntax             Description

abs(x)                     Return the absolute value of a number.
all(iterable)              Return True if bool(e) is True for each element e.
any(iterable)              Return True if bool(e) is True for at least one element e.
chr(integer)               Return a one-character string with the given Unicode code point
divmod(x, y)               Return (x // y, x % y) as tuple, if x and y are integer
hash(obj)                  Return an integer hash value for the object(see Chapter 10).
id(obj)                    Return the unique integer serving as an "identity" for the object.
input(prompt)              Return a string from standard input; the prompt is optional.
isinstance(obj, cls)       Determine if obj is an instanve of the class (or a subclass).
iter(iterable)             Return a new iterator object for the parameter (see Section 1.8).
len(iterable)              Return the number of elements in the given iteration.
map(f, iter1, iter2, ...)  Return an iterator yielding the result of function calls(e1, e2,...)
                           for respective elements e1 ∈ iter1,e2 ∈ iter2,...
max(iterable)              Return the largest element of the given iteration.
max(a, b, c,....)          Return the largest of the arguments
min(iterable)              Return the smallest element of the given iteration
min(a, b, c, ...)          Return the smallest of the arguments.
next(iterator)             Return the next element reported by the iterator(see Section 1.8).
open(filename, mode)       Open a file with the given name and access mode.
ord(char)                  Return the Unicode code point of the given character.
pow(x, y)                  Return the value x**y (as an integer if x and y are integers);
                           equivalent to x ** y
pow(x, y, z)               Return the value (x ** y mod z) as an integer.
print(obj1, obj2)          Print the arguments, with separating spaces and trailing newline.
range(stop)                Construct an iteration of values 0,1,..., stop - 1
range(start, stop)         Construct an iteration of values start, start + 1,..., stop - 1.
reversed(sequence)         Return an iteration of the sequence in reverse.
round(x)                   Return the nearest int value (a tie is broken toward the even value).
round(x, k)                Return the value rounded to the nearest 10 ** (-k) (return-type matches x).
sorted(iterable)           Return a list containing elements of the iterable in sorted order.
sum(iterable)              Return the sum of the elements in the iterable (must be numeric).
type(obj)                  Return the class to which the instance obj belongs.

"""


"""
Table 1.5
"""

"""
Calling Syntax                     Description
fp.read()                          Return the (remaining) contents of a readable file as a string.
fp.read(k)                         Return the next k types of a readable file as a string
fp.readline()                      Return (remainder of) the current line of a readable file as a string
for line in fp:                    Iterate all (remaining)lines of a readable file.
fp.seek(k)                         Change the current position to be at the kth byte of the file
fp.tell()                          Return the current position, ,measured as byte-offset from the start
fp.write(string)                   Write given string at current position of the writable file
fp.writelines(seq)                 write each of the strings of the given sequence at the current
                                   position of the writable file. This command does not insert
                                   any newlines, beyond those that are embeded in the strings
print(..., file=fp)                Return output of print functon to the file.
"""


"""
Table 1.6
"""

"""
Class                   Description
Exception               A base class for most error types
AttributeError          Raised by syntax obj.foo, if obj has no memner named foo
EOFError                Rsised if "end of file" reached for console or file input
IOError                 Raised upon failure of I/O operation (e.g., opening file)
IndexError              Raised if index to sequence is out of bounds
KeyError                Raised if nonexistent key requested for set or dictionary
KeyboardInterrupt       Raised if user types ctrl-C while program is executing
NameError               Raised if nonexistent identifier used
StopIteration           Raised by next(iterator) if no element; see Section 1.8
TypeError               Raised when wrong type of parameter is sent to  a function
ValueError              Raised when parameter has invalid value (e.g., sqrt(-5))
ZeroDivisionError       Raised when any division operator used with 0 as divisor
"""


"""
Table 1.7
"""

"""
Module Name         Description
array               Provides compact array storage for primitive types.
collections         Defines additional data structures and abstract base classes
                    involving collections of objects.
copy                Defines general functions for making copies of objects.
heapq               Provides heap-based priority queue functions (see Section 9.3.7).
math                Defines common mathematical constants and functions.
os                  Provides support for interactions with the poerting system.
random              Provides random number generation.
re                  Provides support for processing regular expressions.
sys                 Provides additional level of interaction with the Python interpreter.
time                Provides support for measuring time, or delaying a program.
"""


"""
Table 1.8
"""

"""
Syntax                       Description
seed(hashable)               Initializes the pseudo-random number generator
                             based upon the hash value of the parameter
random()                     Returns a pseudo-random floating-point
                             value in the interval(0.0, 1.0).
randint(a, b)                Returns a pseudo-random integer
                             in the closed interval[a, b]
randrange(start, stop, stop) Returns a pseudo-random integer in the standard
                             Python range indicated by the parameters
choice(seq)                  Returns an element of the given sequence
                             chosen pseudo-randomly.
shuffle(seq)                 Reorders the elements of the given
                             sequence pseudo-randomly.
"""



