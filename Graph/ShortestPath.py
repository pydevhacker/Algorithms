'''
Created on Mar 10, 2016

@author: sikarwar
'''

max_int = 10**10

def minDistance(dist, spt):
    min = max_int
    min_idx = -1
    
    for i in range(len(dist)):
        if spt[i] == False and dist[i] <= min:
            min = dist[i]
            min_idx = i
    
    return min_idx

def dijkstra(g, s):
    n_v = len(g)
    
    dist = [max_int]*n_v
    spt = [False]*n_v
    dist[s] = 0
    
    for i in range(n_v):
        
        u = minDistance(dist, spt)
        spt[u] = True
        
        for v in range(n_v):
            if spt[v] == False and g[u][v] != 0 and dist[u] != max_int and dist[u] + g[u][v] <= dist[v]:
                dist[v] = dist[u] + g[u][v]
                
    return dist
                
def test_dijkstra():
    g = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 0, 10, 0, 2, 0, 0],
         [0, 0, 0, 14, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    
    s = 0
    
    d = dijkstra(g, s)
    print("distancce from source : ", s, "\n ", [(i, d[i]) for i in range(len(d))])
    
if __name__ == '__main__':
    test_dijkstra()
