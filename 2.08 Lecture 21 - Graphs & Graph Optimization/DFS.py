from graph import *


def DFS(graph, start, end, path = []):
    """ Depth First Search.
        Works with a Stack.
        Last In -> First Out.
        Push -> Pop
        assumes graph is a Digraph
        assumes start and end are nodes in graph
    """
    path = path + [start]
    print('Current dfs path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            newPath = DFS(graph, node, end, path)
            if newPath is not None:
                return newPath


def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print('Current dfs path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles
            if shortest is None or len(path) < len(shortest):
                newPath = DFSShortest(graph, node, end, path, shortest)
                if newPath is not None:
                    shortest = newPath
    return shortest


def DFS_Found(graph, start, end, path = []):
    path = path + [start]
    print()
    print('Current dfs path:', printPath(path))
    if start == end:
        print('=' * 60)
        print('Found path: {}'.format(path))
        yield path
    if end not in path:
        children = graph.childrenOf(start)
        print('~' * 60)
        print('children of {}: {}'.format(start, children))
        print(start, end, path)
        print('~' * 60)
        for i in range(len(children)):
            print('{}== Child # {} of: {}'.format((len(path) - 1) * '\t', i+1, start))
            if children[i] not in path:  # avoid cycles
                print('>>>', children[i], 'not in path', list(path))
                for p in DFS_Found(graph, children[i], end, path):
                    # print('add node: {} to path {}'.format(children[i], path))
                    print(p)
                    yield p
            else:
                print('>>>', children[i], 'is in path', list(path))


def testSP():
    nodes = []
    for name in range(7):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))

    g.addEdge(Edge(nodes[5], nodes[4]))
    g.addEdge(Edge(nodes[5], nodes[6]))

    sp = DFSShortest(g, nodes[0], nodes[5])
    print('Shortest path found by DFS:', printPath(sp))
    print()
    fp = DFS_Found(g, nodes[0], nodes[5])
    for p in fp:
        print('+' * 60)
        print('OUTPUT :::: {}'.format(p))
        print('+' * 60)

if __name__ == '__main__':
    testSP()