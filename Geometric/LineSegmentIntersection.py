'''
Two line (p1, q1) and (p2, q2) intersect if :
(p1, q1, p2) and (p1, q1, q2) 's orientation is different
(p2, q2, p1) and (p2, q2, q1) 's orientation is different

Case 2:
 (p1, q1, p2), (p1, q1, q2), (p2, q2, p1) and (p2, q2, q1) are colinear and
x-projection on (p1, q1) and (p2, q2) intersect
y-projection on (p1, q1) and (p2, q2) intersect
'''

from Geometric.Orientation import orientation

# checks in q lines on line segment 'pr'
def onSegment(p, q, r):
    return (q[0] <= max(p[0],r[0]) and q[0] >= min(p[0],r[0]) and
            q[1] <= max(p[1],r[1]) and q[1] >= min(p[1],r[1]))


def intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onSegment(p1, p2, q1): return True

    if o2 == 0 and onSegment(p1, q2, q1): return True

    if o3 == 0 and onSegment(p2, p1, q2): return True

    if o4 == 0 and onSegment(p2, q1, q2): return True

    return False

def main():
    p1 = (1, 1)
    q1 = (10, 1)
    p2 = (1, 2)
    q2 = (10, 2)
    print(intersect(p1, q1, p2, q2))

    p1 = (10, 0)
    q1 = (0, 10)
    p2 = (0, 0)
    q2 = (10, 10)
    print(intersect(p1, q1, p2, q2))

    p1 = (-5, -5)
    q1 = (0, 0)
    p2 = (1, 1)
    q2 = (10, 10)
    print(intersect(p1, q1, p2, q2))

if __name__ == '__main__':
    main()