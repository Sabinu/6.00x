from graph import *


def DFS_Found(graph, start, end, path = []):
    path = path + [start]
    # print()
    # print('Current dfs path:', printPath(path))
    if start == end:
        # print('=' * 60)
        # print('Found path: {}'.format(path))
        yield path
    if end not in path:
        children = graph.childrenOf(start)
        # print('~' * 60)
        # print('children of {}: {}'.format(start, children))
        # print(start, end, path)
        # print('~' * 60)
        for i in range(len(children)):
            # print('{}== Child # {} of: {}'.format((len(path) - 1) * '\t', i+1, start))
            if children[i] not in path:  # avoid cycles
                # print('>>>', children[i], 'not in path', list(path))
                for p in DFS_Found(graph, children[i], end, path):
                    # print('add node: {} to path {}'.format(children[i], path))
                    # print(path)
                    # print(p)
                    yield p
            # else:
                # print('>>>', children[i], 'is in path', list(path))


def DFS_Directed(graph, start, end, max_d, max_o, path = [[], 0, 0]):
    path[0] = path[0] + [start]
    if len(path[0]) > 1:
        edge = graph.getEdge(path[0][-2], start)
        path[1] += edge[1][0]
        path[2] += edge[1][1]
    # print()
    print('Current dfs path:', path)
    if path[1] > max_d:
        return None
    if path[2] > max_o:
        return None
    if start == end:
        # print('=' * 60)
        # print('Found path: {}'.format(path))
        yield path
    if end not in path[0]:
        children = graph.childrenOf(start)
        # print('~' * 60)
        # print('children of {}: {}'.format(start, children))
        # print(start, end, path)
        # print('~' * 60)
        for i in range(len(children)):
            # print('{}== Child # {}/{} of: {}'.format((len(path) - 1) * '\t', i+1,len(children), start))
            if children[i] not in path[0]:  # avoid cycles
                print('>>>', children[i], 'not in path', list(path))
                for p in DFS_Directed(graph, children[i], end, max_d, max_o,
                                      [path[0], path[1], path[2]]):
                    # print('add node: {} to path {}'.format(children[i], path))
                    # print(path)
                    # print(p)
                    yield p
            # else:
                # print('>>>', children[i], 'is in path', list(path))


def testSP():
    nodes = []
    for name in range(7):
        nodes.append(Node(str(name)))
    g = WeightedDigraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(WeightedEdge(nodes[0], nodes[1], 10, 10))
    g.addEdge(WeightedEdge(nodes[1], nodes[2], 10, 10))
    g.addEdge(WeightedEdge(nodes[2], nodes[3], 10, 10))
    g.addEdge(WeightedEdge(nodes[2], nodes[4], 10, 10))
    g.addEdge(WeightedEdge(nodes[3], nodes[4], 10, 10))
    g.addEdge(WeightedEdge(nodes[3], nodes[5], 10, 10))
    g.addEdge(WeightedEdge(nodes[0], nodes[2], 30, 10))
    g.addEdge(WeightedEdge(nodes[1], nodes[0], 10, 10))
    g.addEdge(WeightedEdge(nodes[3], nodes[1], 10, 10))
    g.addEdge(WeightedEdge(nodes[4], nodes[0], 10, 10))

    g.addEdge(WeightedEdge(nodes[4], nodes[5], 0, 10))
    g.addEdge(WeightedEdge(nodes[4], nodes[6], 0, 0))
    g.addEdge(WeightedEdge(nodes[5], nodes[4], 10, 10))
    g.addEdge(WeightedEdge(nodes[5], nodes[6], 10, 10))

    fp = DFS_Found(g, nodes[0], nodes[5])
    for p in fp:
        print('OUTPUT :::: {}'.format(p))

    print()
    max_d = 50
    max_o = 50
    print('Finding D: {}, O: {}'.format(max_d, max_o))
    fp = DFS_Directed(g, nodes[0], nodes[5], max_d, max_o)
    for p in fp:
        print('OUTPUT :::: {}'.format(p))

if __name__ == '__main__':
    testSP()