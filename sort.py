'''
Created on Mar 9, 2016

@author: sikarwar
'''

def mergeSort(a, p, r):
    
    if p < r:
        q = int((p+r)/2)
        mergeSort(a, p, q)
        mergeSort(a, q+1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    n1 = (q - p + 1)        
    n2 = (r - q)

    left = [None]*(n1)
    right = [None]*(n2)
    
    for i in range(n1):
        left[i] = a[i+p]
    
    for i in range(n2):
        right[i] = a[i+q+1]
        
    
    i = 0
    j = 0
    k = p
    
    while(i < n1 and j < n2):
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j+1
        k = k+1
    
    while i < n1:
        a[k] = left[i]
        i = i+ 1
        k = k+1
    
    while j<n2:
        a[k] = right[j]
        j = j+1
        k = k+1
    

def mergesort_test():
    a = [12, 11, 14, 5, 6, 7]
    print("input array : ", a)
    mergeSort(a, 0, len(a)-1)
    print("sorted array : ", a)
    

if __name__ == '__main__':
    mergesort_test()
    