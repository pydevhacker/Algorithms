'''
divide a set in two subset of equal sums
'''

def findPartitionRecHelper(a, n, sum):

    if sum == 0: return True # best case

    if n == 0 and sum!= 0: return False

    if a[n-1] > sum:
        return findPartitionRecHelper(a, n-1, sum)

    return findPartitionRecHelper(a, n-1, sum) or findPartitionRecHelper(a, n-1, sum-a[n-1])


def findPartitionRec(a):
    n = len(a)
    _sum = sum(a)

    if _sum%2 != 0: #if sum of element of array is odd then array can not be divide into two sub array
        return False

    return findPartitionRecHelper(a, n, _sum//2)


def findPartitionDP(a):
    n = len(a)
    _sum = sum(a)

    if _sum%2 != 0: return False

    if _sum == 0: return True

    if n == 0 and _sum != 0: return False

    l = [[False for x in range(n + 1)] for x in range(_sum//2 + 1)]

    for i in range(n+1):
        l[0][i] = True

    for i in range(1, _sum//2+1):
        for j in range(1, n+1):
            l[i][j] = l[i][j-1]
            if i >= a[j-1]:
                l[i][j] = l[i][j] or l[i-a[j-1]][j-1]

    return l[_sum//2][n]


def main():
    a = [3, 1, 1, 2, 2, 1]
    print(findPartitionDP(a))


if __name__ == '__main__':
    main()