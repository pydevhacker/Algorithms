'''
Use topological sort
'''

from Graph import graph

def topologicalSort(g):

    color = ['WHITE']*g.size()
    path = []
    stack = []
    for n in g.nodes():
        if color[n] != 'WHITE':
            continue
        stack.append(n)
        color[n] = 'GRAY'
        while stack:
            ele = stack[-1]

            childs = []
            for c in g.children(ele):
                if color[c] == 'WHITE':
                    childs.append(c)
                    color[c] = 'GRAY'

            if len(childs) > 0:
                stack = stack + childs
            else:
                color[ele] = 'BLACK'
                path.append(ele)
                stack.pop()

    print("topological sorted path : " , path)
    return path

def longestPath(g, s):
    path = topologicalSort(g)

    dist = [-9999]*g.size()
    dist[s] = 0

    while path:
        ele = path.pop()

        if dist[ele] != -9999:
            for c in g.children(ele):
                if dist[c] < dist[ele] + g.weight(ele, c):
                    dist[c] = dist[ele] + g.weight(ele, c)

    print(dist)

g = graph()
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 5, 1)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

longestPath(g, 1)