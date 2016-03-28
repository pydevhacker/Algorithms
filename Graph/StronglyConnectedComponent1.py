'''
Strongly Connected Components
http://www.geeksforgeeks.org/strongly-connected-components/

A directed graph is strongly connected if there is a path between all pairs of vertices. A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph. For example, there are 3 SCCs in the following graph.

Kosaraju’s algorithm
1) Create an empty stack ‘S’ and do DFS traversal of a graph. In DFS traversal, after calling recursive DFS for adjacent vertices of a vertex, push the vertex to stack.
2) Reverse directions of all arcs to obtain the transpose graph.
3) One by one pop a vertex from S while S is not empty. Let the popped vertex be ‘v’. Take v as source and do DFS (call DFSUtil(v)). The DFS starting from v prints strongly connected component of v.
'''

from Graph import graph


def dfs(v, g, visited, scc):
    visited[v] = True
    scc.append(v)
    for c in g.children(v):
        if visited[c] is False:
            dfs(c, g, visited, scc)


def reverse_graph(g):
    new_graph = graph(g.size())
    for v in g.nodes():
        for c in g.children(v):
            new_graph.addEdge(c, v)
    return new_graph


def fill_order(n, g, stack, visited):
    visited[n] = True
    childs = g.children(n)
    for c in childs:
        if visited[c] is False:
            fill_order(c, g, stack, visited)
    stack.append(n)


def strongly_connected_components(g):
    stack = []
    visited = [False]*g.size()

    for i in range(g.size()):
        if visited[i] is False:
            fill_order(i, g, stack, visited)

    rev_g = reverse_graph(g)

    visited = [False]*rev_g.size()
    print("Strongly Connected Components : ")
    while stack:
        v = stack.pop()
        if visited[v] is False:
            scc = []
            dfs(v, rev_g, visited, scc)
            print(scc)


g = graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

strongly_connected_components(g)