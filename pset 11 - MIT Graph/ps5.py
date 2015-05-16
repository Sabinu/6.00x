# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings

from graph import *


def DFS_Found(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        # print('=' * 60)
        # print('Found path: {}'.format(path))
        yield path
    if end not in path:
        children = graph.childrenOf(start)
        # print('-' * 60)
        # print('children of {}: {}'.format(start, children))
        for i in range(len(children)):
            if children[i] not in path:  # avoid cycles
                for p in DFS_Found(graph, children[i], end, path):
                    yield p


# Problem 2: Building up the Campus Map
def load_map(mapFilename):
    """ Parses the map file and constructs a directed graph
        Parameters:
            mapFilename : name of the map file
        Assumes:
            Each entry in the map file consists of the following four positive
            integers, separated by a blank space:
                From To TotalDistance DistanceOutdoors
            e.g.
                32 76 54 23
            This entry would become an edge from 32 to 76.
        Returns:
            a directed graph representing the map
    """
    print("Loading map from file...")
    inFile = open(mapFilename, 'r')
    line = inFile.readline()
    g = WeightedDigraph()
    while line:
        data = line.split()
        # print(data)
        nodes = [Node(data[0]), Node(data[1])]
        for n in nodes:
            try:
                g.addNode(n)
            except:
                pass
        e = WeightedEdge(nodes[0], nodes[1], float(data[2]), float(data[3]))
        g.addEdge(e)
        line = inFile.readline()
    return g


# Problem 3: Finding the Shortest Path using Brute Force Search
# State the optimization problem as a function to minimize
def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """ Finds the shortest path from start to end using brute-force approach.
        The total distance travelled on the path must not exceed maxTotalDist, &
        the distance spent outdoor on this path must not exceed maxDistOutdoors.
        Parameters:
            digraph: instance of class Digraph or its subclass
            start, end     : start & end building numbers (strings)
            maxTotalDist   : maximum total distance on a path (integer)
            maxDistOutdoors: maximum distance spent outdoors on a path (integer)
        Assumes:
            start and end are numbers for existing buildings in graph
        Returns:
            The shortest-path from start to end, represented by
            a list of building numbers (in strings), [n_1, n_2, ..., n_k],
            where there exists an edge from n_i to n_(i+1) in digraph,
            for all 1 <= i < k.
            If there exists no path that satisfies maxTotalDist and
            maxDistOutdoors constraints, then raises a ValueError.
    """
    s_node = Node(start)
    e_node = Node(end)
    small_path = None
    small_dist = None
    tries = 0
    for c in DFS_Found(digraph, s_node, e_node, []):
        tries += 1
        flag = True
        cons_dist = 0
        cons_outd = 0
        for i in range(len(c) - 1):
            edge = digraph.getEdge(c[i], c[i+1])
            cons_dist += edge[1][0]
            if cons_dist > maxTotalDist:
                flag = False
                break
            elif small_dist is not None and cons_dist > small_dist:
                flag = False
                break
            cons_outd += edge[1][1]
            if cons_outd > maxDistOutdoors:
                flag = False
                break
        if flag:
            if small_dist is None or cons_dist < small_dist:
                small_path = c
                small_dist = cons_dist
                # print('Found smallest! {}'.format(c))
                # print('Found @ Try # {}'.format(tries))
    print('    tried: {}'.format(tries))
    if small_path is not None:
        path = []
        for n in small_path:
            path.append(n.name)
        return path
    else:
        raise ValueError('No path satisfies condition.')


def DFS_Directed(graph, start, end, max_d, max_o, path = [[], 0, 0]):
    path[0] = path[0] + [start]
    # print('Hello path: {}'.format(path))
    if len(path[0]) > 1:
        edge = graph.getEdge(path[0][-2], start)
        # print('Tried to find edge between {} <> {}'.format(path[0][-2], start))
        # print(edge, path[1], path[2])
        path[1] += edge[1][0]
        path[2] += edge[1][1]
    # print()
    # print('Current dfs path: {}'.format(path))
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
                # print('>>>', children[i], 'not in path', list(path))
                for p in DFS_Directed(graph, children[i], end, max_d, max_o,
                                      [path[0], path[1], path[2]]):
                    # print(path)
                    # print(p)
                    yield p
            # else:
                # print('>>>', children[i], 'is in path', list(path))


# Problem 4: Finding the Shorest Path using Optimized Search Method
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """ Finds the shortest path from start to end using directed depth-first.
        search approach. The total distance travelled on the path must not
        exceed maxTotalDist, and the distance spent outdoor on this path must
        not exceed maxDistOutdoors.

        Parameters:
            digraph: instance of class Digraph or its subclass
            start, end: start & end building numbers (strings)
            maxTotalDist : maximum total distance on a path (integer)
            maxDistOutdoors: maximum distance spent outdoors on a path (integer)

        Assumes:
            start and end are numbers for existing buildings in graph

        Returns:
            The shortest-path from start to end, represented by
            a list of building numbers (in strings), [n_1, n_2, ..., n_k],
            where there exists an edge from n_i to n_(i+1) in digraph,
            for all 1 <= i < k.

            If there exists no path that satisfies maxTotalDist and
            maxDistOutdoors constraints, then raises a ValueError.
    """
    s_node = Node(start)
    e_node = Node(end)
    small_path = None
    small_dist = None
    tries = 0
    for c in DFS_Directed(digraph, s_node, e_node, maxTotalDist,
                          maxDistOutdoors, [[], 0, 0]):
        tries += 1
        print('choice: {}'.format(c))
        flag = True
        cons_dist = c[1]
        if flag:
            if small_dist is None or cons_dist < small_dist:
                small_path = c[0]
                small_dist = cons_dist
                # print('Found smallest! {}'.format(c))
                # print('Found @ Try # {}'.format(tries))
    print('    tried: {}'.format(tries))
    if small_path is not None:
        path = []
        for n in small_path:
            path.append(n.name)
        return path
    else:
        raise ValueError('No path satisfies condition.')


# Uncomment below when ready to test
if __name__ == '__main__':
    # Test cases
    mitMap = load_map("mit_map.txt")
    # print(isinstance(mitMap, Digraph))
    # print(isinstance(mitMap, WeightedDigraph))
    # print('nodes: {}\n{}', len(mitMap.nodes), mitMap.nodes,)
    # print('edges:', mitMap.edges)
    # print('edges_keys:', sorted(mitMap.edges.keys()))

    LARGE_DIST = 1000000

    # # Test case 1
    # print("---------------")
    # print("Test case 1:")
    # print("Find the shortest-path from Building 32 to 56")
    # expectedPath1 = ['32', '56']
    # print('STARTING BRUTE-FORCE SEARCH')
    # brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    # # brutePath1 = []
    # print('STARTING DIRECTED SEARCH')
    # dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    # print("Expected   : ", expectedPath1)
    # print("Brute-force: ", brutePath1)
    # print("DFS        : ", dfsPath1)
    # print("Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1,
    #                                            expectedPath1 == dfsPath1))

    # # Test case 2
    # print("---------------")
    # print("Test case 2:")
    # print("Find the shortest-path from Building 32 to 56 w/out going outdoors")
    # expectedPath2 = ['32', '36', '26', '16', '56']
    # print('STARTING BRUTE-FORCE SEARCH')
    # brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    # print('STARTING DIRECTED SEARCH')
    # dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    # print("Expected   : ", expectedPath2)
    # print("Brute-force: ", brutePath2)
    # print("DFS        : ", dfsPath2)
    # print("Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2,
    #                                            expectedPath2 == dfsPath2))

    # # Test case 3
    # print("---------------")
    # print("Test case 3:")
    # print("Find the shortest-path from Building 2 to 9")
    # expectedPath3 = ['2', '3', '7', '9']
    # print('STARTING BRUTE-FORCE SEARCH')
    # brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    # print('STARTING DIRECTED SEARCH')
    # dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    # print('STARTING DIRECTED SEARCH')
    # print("Expected: ", expectedPath3)
    # print("Brute-force: ", brutePath3)
    # print("DFS        : ", dfsPath3)
    # print("Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3,
    #                                            expectedPath3 == dfsPath3))

    # # Test case 4
    # print("---------------")
    # print("Test case 4:")
    # print("Find the shortest-path from Building 2 to 9 without going outdoors")
    # expectedPath4 = ['2', '4', '10', '13', '9']
    # print('STARTING BRUTE-FORCE SEARCH')
    # brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    # print('STARTING DIRECTED SEARCH')
    # dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    # print("Expected   : ", expectedPath4)
    # print("Brute-force: ", brutePath4)
    # print("DFS        : ", dfsPath4)
    # print("Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4,
    #                                            expectedPath4 == dfsPath4))

    # # Test case 5
    # print("---------------")
    # print("Test case 5:")
    # print("Find the shortest-path from Building 1 to 32")
    # expectedPath5 = ['1', '4', '12', '32']
    # print('STARTING BRUTE-FORCE SEARCH')
    # brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    # print('STARTING DIRECTED SEARCH')
    # dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    # print("Expected   : ", expectedPath5)
    # print("Brute-force: ", brutePath5)
    # print("DFS        : ", dfsPath5)
    # print("Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5,
    #                                            expectedPath5 == dfsPath5))

    # # Test case 6
    # print("---------------")
    # print("Test case 6:")
    # print("Find the shortest-path from Building 1 to 32 without going outdoors")
    # expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    # print('STARTING BRUTE-FORCE SEARCH')
    # brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    # print('STARTING DIRECTED SEARCH')
    # dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    # print("Expected   : ", expectedPath6)
    # print("Brute-force: ", brutePath6)
    # print("DFS        : ", dfsPath6)
    # print("Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6,
    #                                            expectedPath6 == dfsPath6))

    # # Test case 7
    # print("---------------")
    # print("Test case 7:")
    # print("Find the shortest-path from Building 8 to 50 without going outdoors")
    # bruteRaisedErr = 'No'
    # dfsRaisedErr = 'No'
    # try:
    #     bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    # except ValueError:
    #     bruteRaisedErr = 'Yes'

    # try:
    #     directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    # except ValueError:
    #     dfsRaisedErr = 'Yes'

    # print("Expected: No such path! Should throw a value error.")
    # print("Did brute force search raise an error?", bruteRaisedErr)
    # print("Did DFS search raise an error?", dfsRaisedErr)

    # # Test case 8
    # print("---------------")
    # print("Test case 8:")
    # print("Find the shortest-path from Building 10 to 32 without walking")
    # print("more than 100 meters in total")
    # bruteRaisedErr = 'No'
    # dfsRaisedErr = 'No'
    # try:
    #     bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    # except ValueError:
    #     bruteRaisedErr = 'Yes'

    # try:
    #     directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    # except ValueError:
    #     dfsRaisedErr = 'Yes'

    # print("Expected: No such path! Should throw a value error.")
    # print("Did brute force search raise an error?", bruteRaisedErr)
    # print("Did DFS search raise an error?", dfsRaisedErr)