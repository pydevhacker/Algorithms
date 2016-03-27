'''
http://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

Tarjan’s Algorithm to find Strongly Connected Components
A directed graph is strongly connected if there is a path between all pairs of vertices. A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph. For example, there are 3 SCCs in the following graph.

Tarjan Algorithm is based on following facts:
1. DFS search produces a DFS tree/forest
2. Strongly Connected Components form subtrees of the DFS tree.
3. If we can find head of such subtrees, we can print/store all the nodes in that subtree (including head) and that will be one SCC.
4. There is no back edge from one SCC to another (There can be cross edges, but cross edges will not be used while processing the graph).

Disc = discovery time of a node. This time is based on DFS Tree Edge, while moving forward in tree this time will increase and hence the discovery time of node will increase.
A -> b -> c -> b => disc[] array for this tree will be [1, 2, 3, 4]
for root node low == disc

low = this array based on the back edge. it gives the discovery time of the node which is reachable from the back-edge of a subtree
tree a -> b -> c -> d => b has sub tree c, d, if any of the node c, d has a back edge that connects a then the low value of b will be disc time of a.
'''

from Graph import Graph

time = 0
scc = []

def dfs(u, g, disc, low, stack, stack_mem):
    global time
    time = time + 1
    disc[u] = low[u] = time
    stack.append(u)
    stack_mem[u] = True

    childs = g.children(u)
    for v in childs:
        if disc[v] == -1:
            dfs(v, g, disc, low, stack, stack_mem)

            low[u] = min(low[u], low[v])
        elif stack_mem[v] is True:
            low[u] = min(low[u], disc[v])

    global scc
    if low[u] == disc[u]:
        scc_temp = []
        while stack[-1] != u:
            w = stack[-1]
            scc_temp.append(w)
            stack_mem[w] = False
            stack.pop()
        w = stack[-1]
        scc_temp.append(w)
        stack_mem[w] = False
        stack.pop()
        scc.append(scc_temp)

def strongly_connected_component(g):
    n = g.size()
    stack_mem = [False]*n
    stack = []
    disc = [-1]*n
    low = [0]*n

    global time
    time = 0

    global scc
    scc = []

    for i in g.nodes():
        if disc[i] == -1:
            dfs(i, g, disc, low, stack, stack_mem)
    return scc

print("Graph 1")
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print(strongly_connected_component(g1))

print("Graph 2")
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print(strongly_connected_component(g2))

print("Graph 3")
g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print(strongly_connected_component(g3))

print("Graph 4")
g4 = Graph(11)
g4.addEdge(0,1)
g4.addEdge(0,3)
g4.addEdge(1,2)
g4.addEdge(1,4)
g4.addEdge(2,0)
g4.addEdge(2,6)
g4.addEdge(3,2)
g4.addEdge(4,5)
g4.addEdge(4,6)
g4.addEdge(5,6)
g4.addEdge(5,7)
g4.addEdge(5,8)
g4.addEdge(5,9)
g4.addEdge(6,4)
g4.addEdge(7,9)
g4.addEdge(8,9)
g4.addEdge(9,8)
print(strongly_connected_component(g4))
