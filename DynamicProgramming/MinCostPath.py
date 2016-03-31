'''
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination). You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.
'''

def minCost(m, n, cost):
    d = [[0 for x in range(m+1)]for x in range(n+1)]
    d[0][0] = cost[0][0]

    for i in range(1, m+1):
        d[i][0] = d[i-1][0] + cost[i][0]

    for j in range(1, n+1):
        d[0][j] = d[0][j-1] + cost[0][j]

    for i in range(1, m+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1]) + cost[i][j]
    return d[m][n]

def main():
    cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    print(minCost(2,2,cost))

if __name__ == '__main__':
    main()