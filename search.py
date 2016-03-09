'''
Created on Mar 9, 2016

@author: sikarwar
'''

'''
Linear Search iterate over each element in an array
and return index if element is found else return -1
Complexity : O(n)
'''
def linearSearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def binarySearch(a, l, r, x):
    
    if r >= l:
        
        mid = int(l + (r-l)/2)
        
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            return binarySearch(a, l, mid-1, x)
        else:
            return binarySearch(a, mid+1, r, x)
        
    else:
        return -1
    
'''
binary search iterative
'''
   
def binarySearch(a, x):
