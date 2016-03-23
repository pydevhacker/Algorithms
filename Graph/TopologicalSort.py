'''

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

    print(path)
    return path

if __name__ == '__main__':
    g = Graph()
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    topologicalSort(g)
