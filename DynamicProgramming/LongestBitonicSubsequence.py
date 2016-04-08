'''
subsequence which is first increasing and then decreasing
it could be prossible that increasing seq is missing or dec seq is missing
'''

def lbs(a):
    n = len(a)
    lis = [1]*(n+1)
    lds = [1]*(n+1)

    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    for i in range(1, n):
        for j in range(i):
            if a[i] < a[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    _max = lis[0] + lds[0] + 1
    for i in range(1, n):
        _max = max((lis[i] + lds[i] - 1), _max)

    return _max

def main():
    a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(lbs(a))

if __name__ == '__main__':
    main()