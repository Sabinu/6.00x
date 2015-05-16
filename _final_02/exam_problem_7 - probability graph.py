import random
import pylab


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
        return self.name.__hash__()


class c_Node(Node):
    def __init__(self, name):
        self.name = str(name)
        self.outbound = set([])
        self.inbound = set([])

    def get_outbound(self):
        return self.outbound

    def get_inbound(self):
        return self.inbound

    def get_in_degree(self):
        return len(self.inbound)

    def get_out_degree(self):
        return len(self.outbound)


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.src.outbound.add(dest)
        self.dest.inbound.add(src)

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)


class Digraph(object):
    """ A directed graph """
    def __init__(self):
        self.allNodes = set([])
        self.edges = set([])
        self.allEdges = set([])

    def addNode(self, node):
        if node in self.allNodes:
            raise ValueError('Duplicate node')
        else:
            self.allNodes.add(node)

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.allNodes and dest in self.allNodes):
            raise ValueError('Node not in graph')
        self.edges.add(edge)
        self.allEdges.add((src, dest))

    def addEdges(self, nEdges):
        # new_edges = 0
        # initial_edges = len(self.allEdges)
        for i in range(nEdges):
            z = random.choice(list(self.allNodes))
            allEdgesExceptZ = []
            for (x, y) in self.allEdges:
                if y != z:
                    allEdgesExceptZ.append((x, y))
            (x, y) = random.choice(allEdgesExceptZ)
            # if (z, y) not in self.allEdges:
            #     new_edges += 1
            e = Edge(z, y)
            self.edges.add(e)
            self.allEdges.add((z, y))
        # print('Added {} of {} requested edges.'.format(new_edges, nEdges))
        # final_edges = len(self.allEdges)
        # diff_edges = final_edges - initial_edges
        # print('Initial, Final, Diff: {} | {} | {}'.format(initial_edges,
              # final_edges, diff_edges))

    def variance(self, X):
        mean = sum(X)/float(len(X))
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        return tot/len(X)

    def mean(self, X):
        return sum(X)/float(len(X))

    def maxDegree(self):
        degrees = []
        for n in self.allNodes:
            degrees.append(n.get_in_degree())
        return max(degrees)

    def meanDegree(self):
        degrees = []
        for n in self.allNodes:
            degrees.append(n.get_in_degree())
        return self.mean(degrees)

    def meanDegreeVariances(self):
        degrees = []
        for n in self.allNodes:
            degrees.append(n.get_in_degree())
        return self.variance(degrees)

    def meanShortestPath(self):
        # Mean Shortest Path of Nodes PowerSet
        # Too complex
        pass

    def hasNode(self, node):
        return node in self.allNodes

    def __str__(self):
        res = ''
        for e in self.allEdges:
            res = '{}{}\n'.format(res, e)
        return res[:-1]


def initializeGraph(n):
    # n is an integer, the number of nodes in the graph
    G = Digraph()
    for i in range(n):
        node = c_Node(i)
        G.addNode(node)
    nodes = list(G.allNodes)
    for i in range(n):
        x = nodes[i]
        y = nodes[(i+1) % n]
        x.outbound.add(y)
        y.inbound.add(x)
        e = Edge(x, y)
        G.edges.add(e)
        G.allEdges.add((x, y))
    return G

if __name__ == '__main__':
    n = 10
    maxDegrees, meanDegrees = [], []
    meanDegreeVariances, meanShortestPaths = [], []
    graph = initializeGraph(n)
    for nEdges in range(n, n*n, int(n*n/10)):
        graph.addEdges(nEdges)
        maxDegrees.append(graph.maxDegree())
        meanDegrees.append(graph.meanDegree())
        meanDegreeVariances.append(graph.meanDegreeVariances())
        meanShortestPaths.append(graph.meanShortestPath())
        print('yei {}'.format(nEdges))
    print(maxDegrees)
    print(meanDegrees)
    print(meanDegreeVariances)
    print(meanShortestPaths)

    pylab.figure('hello')
    pylab.subplot(2, 2, 1)
    pylab.plot(maxDegrees)
    pylab.subplot(2, 2, 2)
    pylab.plot(meanDegrees)
    pylab.subplot(2, 2, 3)
    pylab.plot(meanDegreeVariances)
    pylab.subplot(2, 2, 4)
    pylab.plot(meanShortestPaths)
    pylab.show()