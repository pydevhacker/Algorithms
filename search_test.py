'''
Created on Mar 9, 2016

@author: sikarwar
'''
import Algorithms.search as search

def test_binarySearch():
    a = [2, 3, 4, 10, 40]
    x = 20
    
    result = search.binarySearch(a, 0, len(a)-1, x)
    
    if result == -1:
        print("Element is not found")
    else:
        print("Element is found at index :", result)
        

        

if __name__ == '__main__':
    test_binarySearch()
