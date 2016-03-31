'''
To check if the point (p) lies inside polygon or not
create a line from p to INF, if that line intersect polygon then count number of interection
if count is even then lie outside polygon
if count is odd or point lies on an edge of polygon then inside else outside of polygon
'''

from Geometric.LineSegmentIntersection import intersect
from Geometric.Orientation import orientation
from Geometric.LineSegmentIntersection import onSegment

def inside(poly, p):
    if len(poly) < 3:
        return False

    extremePoint = (9999, p[1])

    prev = poly[0]
    count = 0
    for i in range(1, len(poly)):
        next = poly[i]
        if intersect(prev, next, p, extremePoint):
            #check if point is colinear
            if orientation(prev, p, next) == 0:
                return onSegment(prev, p, next)
            count += 1
        prev = next
    next = poly[0]
    if intersect(prev, next, p, extremePoint):
        #check if point is colinear
        if orientation(prev, p, next) == 0:
            return onSegment(prev, p, next)
        count += 1


    return count % 2 == 1 #count%2 == 1; return true if count is odd else false



def main():
    ploy = [(0, 0), (10, 0), (10, 10), (0, 10)]
    p = (20, 20)
    print(inside(ploy, p))

    p = (5, 5)
    print(inside(ploy, p))

    poly = [()]

if __name__ == '__main__':
    main()
