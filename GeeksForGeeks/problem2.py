
def solve(a, n, k):
    i = 0
    j = n
    while i<j:
        mid = (i+j)//2
        if k == a[mid]:
            return mid+1, n-mid
        elif k<a[mid]:
            j = mid
        else:
            i = mid+1
    return i, n-mid

testCases = int(input())
for i in range(1, testCases*2, 2):
    n, k = input().split()
    a = [int(x) for x in input().split()]
    print(' '.join([str(x) for x in solve(a, int(n), int(k))]))


