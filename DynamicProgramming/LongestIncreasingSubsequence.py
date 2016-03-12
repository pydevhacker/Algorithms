'''
Created on Mar 11, 2016

@author: sikarwar
'''

def binarySearch(a, k):
    p = 0
    r = len(a)
    while(r>=p):
        q = int((p+r)/2)
        if k == a[q]:
            return (p, q, r, 1)
        elif k < a[q]:
            r = q-1
        else:
            p = q+1
    return (p, q, r, -1)

def lis(a):
    t = []
    path = {}
    #add first element to t list
    t.append(a[0])
    path.setdefault(len(t), [a[0]])
    for i in range(1, len(a)):
        #extend t
        if a[i] > t[-1]:
            t.append(a[i])
            path.setdefault(len(t), [j for j in path[len(t)-1]]+[a[i]])
            print(path[len(t)-1])
        elif a[i] < t[0]:
            t[0] = a[i]
            path[1] = [a[i]]
        else:
            #find position of a[i]
            (p, q, r, z) = binarySearch(t, a[i])
            if z == -1: 
                t[p] = a[i]
                path[p+1] = [j for j in path[r+1]] + [a[i]]
    
    return path


a = [10, 22, 9, 33, 21, 50, 41, 60, 80, 5]
print("Length of Longest increasing subsequence is ", lis(a))