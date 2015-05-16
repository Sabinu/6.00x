# 6.00.2x Problem Set 5
# Graph optimization
# A set of data structures to represent graphs


class Node(object):
    def __init__(self, name):
        self.name = str(name)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if other is None:
            return None
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)


class Digraph(object):
    """ A directed graph """
    def __init__(self):
        """ A Python Set is basically a list that doesn't allow duplicates.
            Entries into a set must be hashable(where have we seen this before?)
            Because it is backed by a hashtable, lookups are O(1)
            as opposed to the O(n) of a list (nifty!)
        http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        """
        self.nodes = set([])
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this; make sure we
            # don't add a duplicate entry for the same node in self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedEdge(Edge):
    """ A weighted edge. """
    def __init__(self, src, dest, weight1, weight2):
        self.src = src
        self.dest = dest
        self.total_dist = weight1
        self.outdoor_dist = weight2

    def getTotalDistance(self):
        return self.total_dist

    def getOutdoorDistance(self):
        return self.outdoor_dist

    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest,
               self.total_dist, self.outdoor_dist)


class WeightedDigraph(Digraph):
    """ A weighted directed graph. """
    def __init__(self):
        self.nodes = set([])
        self.edges = {}

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        dist = edge.getTotalDistance()
        outd = edge.getOutdoorDistance()
        # if not(src in self.nodes and dest in self.nodes):
        #     raise ValueError('Node not in graph')
        if src not in self.nodes:
            raise ValueError('Node {0}not in graph'.format(src))
        elif dest not in self.nodes:
            raise ValueError('Node {0} note in graph'.format(dest))
        self.edges[src].append([dest, (dist, outd)])

    def getEdge(self, src, dest):
        if src not in self.nodes:
            raise ValueError('Node {0}not in graph'.format(src))
        elif dest not in self.nodes:
            raise ValueError('Node {0} note in graph'.format(dest))
        for e in self.edges[src]:
            if e[0] == dest:
                return e

    def childrenOf(self, node):
        edges_list = []
        for e in self.edges[node]:
            edges_list.append(e[0])
        return edges_list
        # return self.edges[node]

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} ({3:.1f}, {4:.1f})\n'.format(res, k, d[0], d[1][0], d[1][1])
        return res[:-1]


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result

if __name__ == '__main__':
    # TESTS from edX
    """
    g = WeightedDigraph()
    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    g.addNode(na)
    g.addNode(nb)
    g.addNode(nc)
    e1 = WeightedEdge(na, nb, 15, 10)
    print(e1)
    print(e1.getTotalDistance())
    print(e1.getOutdoorDistance())
    e2 = WeightedEdge(na, nc, 14, 6)
    e3 = WeightedEdge(nb, nc, 3, 1)
    print(e2)
    print(e3)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    print(g)
    print(g.childrenOf(na))
    # a->b (15, 10)
    # 15
    # 10
    # a->c (14, 6)
    # b->c (3, 1)

    # a->b (15, 10)
    # a->c (14, 6)
    # b->c (3, 1)
    """
    """
    nh = Node('h')
    nj = Node('j')
    nk = Node('k')
    nm = Node('m')
    ng = Node('g')
    g = WeightedDigraph()
    g.addNode(nh)
    g.addNode(nj)
    g.addNode(nk)
    g.addNode(nm)
    g.addNode(ng)
    randomEdge = WeightedEdge(nk, nm, 14, 11)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nj, nk, 48, 12)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nh, nm, 12, 7)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nk, nm, 25, 22)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nh, nj, 22, 22)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nk, nm, 87, 24)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nk, nh, 72, 62)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(nh, nm, 83, 15)
    g.addEdge(randomEdge)
    print(g.childrenOf(nh))  # [[m, (12, 7)], [j, (22, 22)], [m, (83, 15)]]
    print(g.childrenOf(nj))  # [[k, (48, 12)]]
    print(g.childrenOf(nk))  # [[m, (14, 11)], [m, (25, 22)], [m, (87, 24)], [h, (72, 62)]]
    print(g.childrenOf(nm))  # []
    print(g.childrenOf(ng))  # []
    """
    # """
    nx = Node('x')
    ny = Node('y')
    nz = Node('z')
    e1 = WeightedEdge(nx, ny, 18, 8)
    e2 = WeightedEdge(ny, nz, 20, 1)
    e3 = WeightedEdge(nz, nx, 7, 6)
    g = WeightedDigraph()
    g.addNode(nx)
    g.addNode(ny)
    g.addNode(nz)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    print(g)
    # y->z (20, 1)
    # x->y (18, 8)
    # z->x (7, 6)
    # """