#-*-coding: utf-8 -*-

"""
Code Fragment 14.1
"""

#---------------------nested Vertex class--------------------------------
class Vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_elememt'

    def __init__(self, x):
        """Do not call constructor directly. Use Graph's insert_vertex(x)."""
        self._element = x

    def element(self):
        """Return element associated with this vertex."""
        return self._element

    def __hash__(self):       #will allow vertex to be a map/set key
        return hash(id(self))

#--------------nested Edge class---------------------------------------
class Edge:
    """Lighweight edge structure for graph."""
    __slots__ = '-origin', '_destination', '_element'

    def __init__(self, u, v, x):
        """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """Return (u,v) tuple for vertices u and v."""
        return (self._origin, self._destination)

    def opposite(self, v):
        """Return the vertex that is opposite v on this edge."""
        return self._destination if v is self._origin else self._origin

    def element(self):
        """Return element associated with this edge."""
        return self._element

    def __hash__(self):      #will allow edge to be a map/set key
        return hash((self._origin, self._destination))


"""
Code Fragment 14.2
"""

class Graph:
    """Representation of a simple graph using an adjacency map."""

    def __init__(self, directed=False):
        """Create an empty graph (undirected, by default).

        Graph is derected if optional paramter is set to True
        """
        self._outgoing = { }
        #only create second map for dirested graph; use alias for undirected
        self._incoming = { } if directed else self._outgoing

    def is_directed(self):
        """Return True if this is a directed graph; False if indirected.

        Property is based on the original declaration of the graph, not its contents.
        """
        return self._incoming is not self._outgoing      # directed if maps are distinct

    def vertex_cout(self):
        """Return an iteration of all vertices the graph."""
        return self._outgoing.keys()

    def dege_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v] for v in self._outgoing))
        #for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edge(self):
        """Return a set of all edges of the graph."""
        result = set()    #avoid double-reporting edges of indirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())       #add edges to resulting set
        return result

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        return self._outgoing[u].get(v)         #returns None if v not adjacent

    def degree(self, v, outgoing=True):
        """Return number of (outgoing) edges incident to vertex v in the graph.

        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self._outgoing if outgoing else self._outgoing
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._outgoing[v][u] = e


"""
Code Fragment 14.5
"""

def DFS(g, u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices vertices will be added to the dictionary as a result.
    """



for e in g.incident_edges(u):        #for every outgoing edge from u
    v = e.opposite(u)
    if v not in discovered:          #v is an unvisited vertex
        discovered[v] = e            # e is the tree edge that discovered v
        DFS(g, v, discovered)        #recursively explore from v


"""
Code Fragment 14.6
"""

def construct_path(u, v, discovered):
    path = []               #empty path by default
    if v in discovered:     #we build list form v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]        #find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()          #reorient path from u to v
    return path


"""
Code Fragment 14.7
"""

def DFS_complete(g):
    """Perform DFS for entire graph and return forest as a dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DSF tree are mapped to None.)
    """
    forest = { }
    for u in g.vertices():
        if u not in forest:
            forest[u] = None         #u will be the root of a tree
            DFS(g, u, forest)
    return forest


"""
Code Fragment 14.8
"""

def BFS(g, s, discovered):
    """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

    discovered is a sictionary mappiong each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]    # find level includes only s
    while len(level) > 0:
        next_level = []   #prepare to gather newly found vertices
        for u in level:
            for e in g.incidnt_edges(u):   #for  every outgong edge from u
                v = e.opposite(u)
                if v not in discovered:   #v is an unvisited vertex
                    discovered[v] = e    #e is the tree edge that  discovered v
                    next_level.append(v)   #v will be further considered in next pass
        level = next_level         #relabe 'next' level to become current


"""
Code Fragment 14.10
"""

def floyd_warshall(g):
    """Return a new graph that is the transitive closure of g."""
    closure = deepcopy(g)          #imported from copy module
    verts = list(closure.vertices())    #make indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):      #verify that edge(i,k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):      #verify that edge(k,j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:   #if (i,j) not yet included, add it to the closure
                        if closure.get_edge(verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure


"""
Code Fragment 14.11
"""

def topological_sort(g):
    """Return a list of verticies of directed acyclic graph g in topological order.

    If graph g has a cycle, the result will be incomplete.
    """
    topo = []   #a list of vertices placed in topological order
    ready = []   #list of vertices that have no remaining constraints
    incount = { } #keep track of in-degree for each vertex
    for u in g.vertices():
        incount[u] = g.degree(u, False)   #parameter requests incoming degree
        if incount[u] == 0:    #if u has no incoming edges,
            ready.append(u)     #it is free of contraints
    while len(ready) > 0:
        u = ready.pop()         #u is free of constraints
        topo.append(u)          #add u to the topological order
        for e in g.incident_edge(u):    #consider all outgoing neighbors of u
            v = e.opposite(u)
            incount[v] -= 1       #v has one less constraint without u
            if incount[v] == 0:
                ready.append(v)
    return topo


"""
Code Fragment 14.13
"""

def shortest_path_lengths(g, src):
    """Compute shortest-path distances from src to reachable vertices of g.

    Graph g can be undirected or directed, but must be weighted such that
    e.element() returns a numeric weight for each edge e.

    Return dictionary mapping each reachable vertex to its distance from src.
    """
    d = { }             #d[v] is upper bound from s to vue
    pq = AdaptableHeapPriorityQueue()    #vertex v will have key d[v]
    pqlovator = { }     #map from vertex to its pq locator

    #for each vertex v of the graph, add an entry to the priority queue, with
    #the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')     #syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v)    #save locator for future update

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key      #its correct d[u] value
        del pqlocator[u]    #u is no longer in pq
        for e in g.incident_edges(u):     #outgoing edges(u, v)
            v = e.opposite(u)
            if v not in cloud:     #perform relaxation step on edge(u,v)
                wgt = e.element()
                if d[u] + wgt < d[v]:   #better path to v
                    d[v] = d[u] + wgt   #update the distance
                    pq.update(pqlocator[v], d[v], v)   #update the pq entry
    return cloud       #only includes reachable vertices


"""
Code Fragment 14.14
"""

def shortest_path_tree(g, s, d):
    """Reconstruct shortest-path tree rooted at vertex s,given distance map d

    Return tree as a map from each rachable vertex v (other than s ) to the
    edge e=(u,v) that is used to reach  v from its parent u in the tree.
    """
    tree = { }
    for v in d:
        if v is not s:
            for e in g.incidnet_edges(v, False):    #consider INCOMING edges
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:
                    tree[v] = e       #edge e is used to reach v
    return tree


"""
Code Fragment 14.16
"""

def MST_PrimJarnik(g):
    """Compute a minimum spanning tree of weighted graph g.

    Return a list of edge that comprise the MST (in arbitrary order)
    """
    d = { }              #d[v] is bound on distance to tree
    tree = []            #list of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()     #d[v] maps to value (v, e=(u,v))
    pqlocator = { }          #map from vertex to its pq locator

    #for each vertex v of the graph, add an entry to the priority queue, with
    #the source having sistance 0 and all others having infinite distance
    for v in g.vertices():
        if len(d) == 0:            #this is the first node
            d[v] = 0               #make it the root
        else:
            d[v] = float('inf')       #positive infinity
        pqlocator[v] = pq.add(d[v], (v, None))

    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value
        #unpack tuple from pq
        del pqlocator[u]            #u is no longer in pq
        if edge is not None:
            tree.append(edge)       #add edge to tree
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:       #thus v not  yet in tree #see if edge(u, v) better connects v to the growing tree
                wgt = link.element()
                if wgt < d[v]:      #better edge to v
                    d[v] = wgt      #update the distance
                    pq.update(pqlocator[v], d[v], (v, link))   #update the pq entry
    return tree



"""
Code Fragment 14.18
"""

def MST_Kruskal(g):
    """Compute a minimum spanning tree of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.

    The elements of the graph's edges are assumed to be weights.
    """
    tree = []        #list of edges in spanning tree
    pq = HeapPriorityQueue()    #entries are edges in G, with weights as key
    forest = Partition()       #keeps track of forest clusters
    position = { }             #map each node to its Partition entry

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)    #edge's element is assumed to be its weight

    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():   #tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)


    return tree


"""
Code Fragment 14.19
"""

class Partition:
    """Union-find structure for maintaining disjoint sets."""

    #--------------------nested Position class------------------------
    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            """Create a new position that is the leader of its own group."""
            self._container = container   #reference to Partition instance
            self._element = e
            self._size = 1
            self._parent = self          #convention for a group leader

        def element(self):
            """Return element stored at this position."""
            return self._element

    #------------public Partition methods-------------------------------
    def make_group(self, e):
        """Makes a new group containing element e,and returns its Position."""
        return self.Position(self, e)

    def find(self, p):
        """Find the group containing p and return the position of its leader."""
        if p._parent != p:
            p._parent = self.find(p._parent)   # overwrite p._parent after recursion
        return p._parent

    def union(self, p, q):
        """Merges the groups containg elements p and q(if distinct)."""
        a = self.find(p)
        b = self.find(q)
        if a is not b:       #only merge if different groups
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size















