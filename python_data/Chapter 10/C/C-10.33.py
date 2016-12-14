#-*-coding: utf-8 -*-

"""
Our implementation of separate chaining in ChainHashMap conserves
memory by representing empty buckets in the table as None, rather than
as empty instances of a secondary structure. Because many of these buckets
will hold a single item, a better optimization is to have those slots of
the table directly reference the_Item instance, and to reserve use of secondary
containers for buckets that have two or more items. Modify our
implementation to provide this additional optimization.
"""