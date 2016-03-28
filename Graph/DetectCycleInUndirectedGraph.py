'''
Detect cycle in undirected graph.
    - We can use Union Find solution to find cycle in undirected graph. O(ELogV)
    - We can use DFS to find cycle
        - For every visited V, if there is an adjacent u such that u is visited and u is not parent of V.
        - O(E + V)
'''

from Graph import graph

def iscycle(g):
    visited = [False]*g.size()

    for n in g.nodes():
        if visited[n] is False:
            if cycleUtil(g, visited, n) is True:
                return True
    return False

def cycleUtil(g, visited, n):
    visited[n] = True

    stack = list()
    stack.append(n)
    while stack:
        ele = stack.pop()

        childs = g.children(ele)
        for c in childs:
            if visited[c] is False:
                stack.append(c)
            elif c != ele:
                return True
    return False

g = graph()
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if iscycle(g) is True:
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")

g = graph()
g.addEdge(0, 1)
g.addEdge(1, 2)

if iscycle(g) is True:
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")