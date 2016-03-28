'''
http://www.geeksforgeeks.org/bridge-in-a-graph/
An edge in an undirected connected graph is a bridge iff removing it disconnects the graph. For a disconnected undirected graph, definition is similar, a bridge is an edge removing which increases number of connected components.
Like Articulation Points,bridges represent vulnerabilities in a connected network and are useful for designing reliable networks. For example, in a wired computer network, an articulation point indicates the critical computers and a bridge indicates the critical wires or connections.

DFS + check if no back edge is present
The condition for an edge (u, v) to be a bridge is, “low[v] > disc[u]”.
'''

from Graph import graph

time = 0


def dfs(u, g, visited, disc, low, parent, bridges):
    global time
    visited[u] = True
    disc[u] = low[u] = time = time + 1

    for v in g.children(u):
        if visited[v] is False:
            parent[v] = u
            dfs(v, g, visited, disc, low, parent, bridges)

            low[u] = min(low[u], low[v])

            if low[v] > disc[u]:
                bridges.append((u, v))
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


def bridge(g):
    n = g.size()
    visited = [False]*n
    disc = [0]*n
    low = [0]*n
    parent = [-1]*n
    bridges = []

    for i in g.nodes():
        if visited[i] is False:
            dfs(i, g, visited, disc, low, parent, bridges)

    print(bridges)


g1 = graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
bridge(g1)


g2 = graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
bridge(g2)