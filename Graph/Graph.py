'''
Created on Mar 9, 2016

@author: sikarwar
'''

class Graph:
    def __init__(self, nodes=0):
        self.n = set()
        self.g = {}
        self.e = set()
        self.w = {}



    def add(self, a, b, weight):
        self.g.setdefault(a, [])
        self.g[a].append(b)
        edge = (a, b)
        self.e.add(edge)
        self.w.setdefault(edge, 0)
        self.w[edge] = weight

    def weight(self, f, t, order=True):
        if self.w[(f, t)] is not None:
            return self.w[(f, t)]
        if order is False:
            if self.w[(t, f)] is not None:
                return self.w[(t, f)]
        return 0

    def add_edge(self, f, t, w=0, undirected=False):
        self.add(f, t, w)

        self.n.add(f)
        self.n.add(t)

        if undirected:
            self.add(t, f, w)


    def hasNode(self, idx):
        if idx in self.n:
            return True
        return False

    def hasEdge(self, frm, to, weight = 0, order=True):
        if order and (frm, to, weight) in self.e:
            return True
        if order is False and ((frm, to, weight) in self.e or (to, frm) in self.e):
            return True
        return False
    
    def print(self):
        print(self.g)
        
    def size(self):
        return len(self.n)

    def nodes(self):
        return self.n

    def edges(self):
        return self.e

    def edges_size(self):
        return len(self.e)

    def children(self, idx):
        if idx not in self.g:
            return []
        return self.g[idx]

    def children_size(self, idx):
        return len(self.g[idx])

    def graph(self):
        return self.g