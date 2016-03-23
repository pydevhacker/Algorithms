'''
Created on Mar 9, 2016

@author: sikarwar
'''
from Graph import Graph

# O(V+E)
def BFS(g, s):
    path = []
    visited = [False]*g.size()
    queue = []
    queue.append(s)
    visited[s] = True
    
    while len(queue)!= 0:
        s = queue.pop(0)
        path.append(s)
        visited[s] = True
        #get child
        childs = g.childs(s)
        for c in childs:
            if visited[c] == False:
                queue.append(c)
                
    
    print("Path : ", path)
                
def test_BFS():
    g = Graph(4)
    
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    BFS(g, 2)
    
if __name__ == '__main__':
    test_BFS()