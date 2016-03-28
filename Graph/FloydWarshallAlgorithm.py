'''
Created on Mar 11, 2016

@author: sikarwar
'''
#TODO
INF = 99999


graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]


dist = map(lambda i : map(lambda j : j , i) , graph)



print(dist)