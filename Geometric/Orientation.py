'''
Orientation of three points depends on slop
first find the slope of two point p1 and p2 = s1
s1 = (y2 - y1)/(x2 - x1)
and then find the slop of p2 and p3 = s2
s2 = (y3 - y2)/(x3 - x2)
s1 < s2 then the orientation is counterclockwise (left turn)
s1 == s2 then the points are colinear
s1 > s2 then the orientation is clockwise (right turn)

we can combine above into
o = (y2-y1)*(x3-x2) - (y3-y2)*(x2-x1)
if o < 0 then counterclockwise (left turn)
if o == 0 then colinear
if o > 0 then clockwise (right turn)
'''


def orientation(p1, p2, p3):
    return (p2[1]-p1[1])*(p3[0]-p2[0]) - (p3[1]-p2[1])*(p2[0]-p1[0])


def main():
    p1 = (0,0)
    p2 = (4,4)
    p3 = (1,2)
    o = orientation(p1, p2, p3)
    if o < 0:
        print('Counter Clock Wise')
    elif o > 0:
        print('Clock Wise')
    else:
        print('Colinear')

if __name__ == '__main__':
    main()
