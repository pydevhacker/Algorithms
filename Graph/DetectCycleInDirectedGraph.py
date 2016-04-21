

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

def detectCycleUtil(g, n, color):
    stack = []
    stack.append(n)
    color[n] = 1
    path = []

    while stack:
        element = stack.pop()

        nChild = 0
        for child in g.children(element):
            if color[child] == 0:
                stack.append(child)
                color[child] = 1
                nChild += 1
            else:
                if color[child] == 1:
                    return True
        #color[n] == 2
    return False

def detectCycle(g):
    color = [0]*g.size()

    for n in range(g.size()):
        if color[n] == 0:
            if detectCycleUtil(g, n, color):
                return True
    return False



g = graph.Graph(4)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(detectCycle(g))
'''
if cycle:
    print("Graph contains cycle ", path)
else:
    print("Graph does not contains cycle")
'''