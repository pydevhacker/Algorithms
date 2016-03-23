'''
Use topological sort
'''

from Graph import Graph

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

g = Graph()
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 6)
g.add_edge(1, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(2, 5, 2)
g.add_edge(2, 3, 7)
g.add_edge(3, 5, 1)
g.add_edge(3, 4, -1)
g.add_edge(4, 5, -2)

longestPath(g, 1)