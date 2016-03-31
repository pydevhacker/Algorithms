'''
This Algo is to find the closest pair of point in the space of given points.
The solution is based on divide and concur approach.
First divide the points based on x asix
find the mid x-axis
create a strip of closest points from the mid x-axis
now find the closest point in that strip

Time Complexity : O(nLogn)
'''

import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def bruteForce(px, n):
    _min = 99999
    for i in range(n):
        for j in range(i+1, n):
            _min = min(dist(px[j], px[i]), _min)
    return _min

def stripClosestPoint(strip, d):
    _min = d
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][i] > _min:
                break
            _min = min(dist(strip[j], strip[i]), _min)
    return _min

def closest(px, py, n):
    if n <= 3: #if n is less than 3 then use the brute force to find the closes pair
        return bruteForce(px, n)
    #find the mid point
    mid = n//2
    midpoint = px[mid]

    #create two list pyl and pyr ie left point from mid x-axis and right points from mid x-aixs
    pyl = []
    pyr = []
    for i in range(n):
        if py[i][0] <= px[mid][0]:
            pyl.append(py[i])
        else:
            pyr.append(py[i])

    ld = closest(px[:mid], pyl, mid)
    rd = closest(px[mid:], pyr, n-mid)

    d = min(ld, rd)

    #create a strip array that will contain all the points which are closes to the mid point
    strip = []
    for i in range(n):
        if abs(py[i][0] - midpoint[0]) < d:
            strip.append(py[i])

    return min(d, stripClosestPoint(strip, d))

def main():
    p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    px = p[:]
    px.sort(key = lambda x : x[0])
    py = p[:]
    py.sort(key = lambda x : x[1])
    n = len(p)

    print(closest(px, py, n))

if __name__=='__main__':
    main()