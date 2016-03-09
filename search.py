'''
Created on Mar 9, 2016

@author: sikarwar
'''

#O(log(log(n))
def interpolationSearch(a, key):
    low = 0
    high = len(a)-1
    mid = 0
    
    while a[high] != a[low] and key>=a[low] and key<=a[high]:
        mid = low + int((key - a[low])*(high - low)/(a[high] - a[low]))
        
        if a[mid] < key:
            low = mid+1
        elif a[mid] > key:
            high = mid - 1
        else:
            return mid
        
    if key == a[low]:
        return low
    else:
        return -1

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
http://geeksquiz.com/binary-search/
'''
# O(log(n))
def binarySearch_itr(a, l, r, x):
    
    while r >= l:
        
        mid = int(l + (r-l)/2)
        
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            r = mid-1
        else:
            l = mid+1
            
    return -1
    