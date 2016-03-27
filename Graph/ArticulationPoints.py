'''
http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

Articulation Points (or Cut Vertices) in a Graph
A vertex in an undirected connected graph is an articulation point (or cut vertex) iff removing it (and edges through it) disconnects the graph. Articulation points represent vulnerabilities in a connected network – single points whose failure would split the network into 2 or more disconnected components. They are useful for designing reliable networks.
For a disconnected undirected graph, an articulation point is a vertex removing which increases number of connected components.

A O(V+E) algorithm to find all Articulation Points (APs)
The idea is to use DFS (Depth First Search). In DFS, we follow vertices in tree form called DFS tree. In DFS tree, a vertex u is parent of another vertex v, if v is discovered by u (obviously v is an adjacent of u in graph). In DFS tree, a vertex u is articulation point if one of the following two conditions is true.
1) u is root of DFS tree and it has at least two children.
2) u is not root of DFS tree and it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u.
'''

from Graph import Graph

time = 0

def dfs(u, g, visited, disc, low, parent, ap):
    visited[u] = True
    global time
    disc[u] = low[u] = time = time + 1

    childs = g.children(u)
    for v in childs:
        if visited[v] is False:
            parent[v] = u
            dfs(v, g, visited, disc, low, parent, ap)

            low[u] = min(low[u], low[v])

            #condition 1 if u is root and has two children then its ap
            if parent[u] is -1 and len(childs) > 1: ap[u] = True

            #condition 2 if u is not root and no back edge present from child of u to u
            if parent[u] is not -1 and low[v] >= disc[u]: ap[u] = True

        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

def articulation_points(g):

    global time
    time = 0
    n = g.size()
    visited = [False]*n
    disc = [0]*n
    low = [0]*n
    parent = [-1]*n
    ap = [False]*n

    for i in range(n):
        if visited[i] is False:
            dfs(i, g, visited, disc, low, parent, ap)

    print("Articulation Points : ", [i for i in range(n) if ap[i] is True])



g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
articulation_points(g1)

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
articulation_points(g2)

g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
articulation_points(g3)