from graph import *


def DFS(graph, start, end, path=[]):
    # Assumes graph is a Digraph
    # Assumes start and end are nodes in graph
    path.append(start)
    print('Current dfs path: {}'.format(printPath(path)))

    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # Avoid cycles
            newPath = DFS(graph, node, end, path)
            if newPath is not None:
                return newPath
    return None