#Detect cycle in undirected graph
'''
the implementation of union() and find() is naive and takes O(n) time in worst case.
These methods can be improved to O(Logn) using Union by Rank or Height.

Time Complexity : O(ELogV)
'''
from Graph import Graph

def find(parent, i):
    if parent[i] == -1:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    x_parent = find(parent, x)
    y_parent = find(parent, y)

    if x_parent == y_parent:
        return False
    else:
        parent[x_parent] = y_parent
    return True

def isCycle(g):
    parent = [-1]*g.size()

    for e in g.edges():
        if union(parent, e[0], e[1]) is False:
            return True
    return False

g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(0, 2)

if isCycle(g) is True:
    print("Graph Contains Cycle")
else:
    print("Graph does not contains cycle")