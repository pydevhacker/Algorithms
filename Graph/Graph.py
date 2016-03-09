'''
Created on Mar 9, 2016

@author: sikarwar
'''

class Graph:
    def __init__(self, nodes):
        self.n_nodes = nodes
        self.g = {}
        for i in range(nodes):
            self.g.setdefault(i, set())
                
    def addEdge(self, f, t):
        self.g[f].add(t)
    
    def print(self):
        print(self.g)
        
    def size(self):
        return len(self.g)
    
    def childs(self, idx):
        return self.g[idx]
        
