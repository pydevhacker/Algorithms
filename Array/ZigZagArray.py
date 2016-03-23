'''
Convert array into Zig-Zag fashion
a < b > c < d > e < f
Time Complexity : O(n)
'''

def zig_zag(a):
    flag = True

    for i in range(len(a)-1):
        if flag:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            elif a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        flag = not flag

a = [4, 3, 7, 8, 6, 2, 1]
print("Input : ", a)
zig_zag(a)
print("Output : ", a)

'''
Can be done in O(nlogn) time complexity.
Sort the array and skip first element and swap rest of the elements in pairs.
However, above implementation is O(n)
'''