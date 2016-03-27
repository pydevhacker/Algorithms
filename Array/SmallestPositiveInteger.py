'''
Find the smallest positive integer value that cannot be represented as sum of any subset of a given array

Given a sorted array (sorted in non-decreasing order) of positive numbers, find the smallest positive integer value that
cannot be represented as sum of elements of any subset of given set.
Expected time complexity is O(n).
'''


def find_smallest(a):
    res = 1
    for i in range(len(a)):
        if a[i] <= res:
            res += a[i]

    return res

print(find_smallest([1, 3, 4, 5]))
print(find_smallest([1, 2, 6, 10, 11, 15]))
print(find_smallest([1, 1, 1, 1]))
print(find_smallest([1, 1, 3, 4]))
