'''
Algorithm to check if the graph is bipartite or note.

bfs

'''

def isBipartitle(g, s):
    color = [-1]*len(g)

    color[s] = 1
    queue = list()
    queue.append(s)

    while queue:
        e = queue.pop(0)

        childs = g[e]
        for c in childs:
            if c == 1 and color[c] == -1:
                color[c] = 1-color[e]
                queue.append(c)
            elif childs[c] == 1 and color[c] == color[e]:
                return False
    return True

g = [[0, 1, 0, 1],
     [1, 0, 1, 0],
     [0, 1, 0, 1],
     [1, 0, 1, 0]]

print(isBipartitle(g, 0))

