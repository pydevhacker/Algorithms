'''

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

    print(path)
    return path

if __name__ == '__main__':
    g = graph()
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    topologicalSort(g)
