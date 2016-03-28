

from Graph import graph

def isCycle(g):
    n = g.size()
    visited = [False]*n
    path = []
    stack = []

    for e in g.g:
        if visited[e] == False:
            stack.append(e)

            while stack:
                ele = stack.pop()

                if ele in path:
                    path.append(ele)
                    return (True, path)

                path.append(ele)
                if visited[ele]:
                    path.pop()
                    continue

                childs = g.children(ele)
                if childs:
                    for c in childs:
                        if visited[c] == False:
                            stack.append(c)
                else:
                    path.pop()
    return (False, path)

g = graph(4)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

cycle, path = isCycle(g)

if cycle:
    print("Graph contains cycle ", path)
else:
    print("Graph does not contains cycle")