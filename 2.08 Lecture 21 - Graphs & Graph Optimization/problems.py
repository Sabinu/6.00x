from graph import *
from depth_first import *

nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

# Problem 2
for a, n1 in enumerate(nodes):
    for n2 in nodes[a+1:]:
        if not(n1.name == n2.name):
            for i in range(len(n1.name) - 1):
                if n1.name[i] == n2.name[i+1] and n1.name[i+1] == n2.name[i]:
                    e = Edge(n1, n2)
                    g.addEdge(e)
                    break
# print(g)


# Problem 5
DFS(g, nodes[0], nodes[4], [])
print()
DFS(g, nodes[4], nodes[1], [])
print()
DFS(g, nodes[1], nodes[1], [])
print()
DFS(g, nodes[2], nodes[4], [])
print()
DFS(g, nodes[2], nodes[3], [])
print()
DFS(g, nodes[3], nodes[1], [])