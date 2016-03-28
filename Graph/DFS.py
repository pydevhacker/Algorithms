'''
Created on Mar 10, 2016

@author: sikarwar
'''

from Graph import graph

def DFS(g, s):
    visited = [False]*g.size()
    
    stack = []
    stack.append(s)
    path = []
    
    while len(stack) != 0:
        e = stack.pop()
        visited[e] = True
        path.append(e)
        #getChilds
        childs = g.children(e)
        for c in childs:
            if visited[c] == False:
                stack.append(c)
                
    
    print("Path : ", path)
    
def test_DFS():
    g = graph(4)
    
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    DFS(g, 2)
    
if __name__ == '__main__':
    test_DFS()