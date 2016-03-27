'''
Generate all possible sorted arrays from alternate elements of two given sorted arrays
For Example
A = {10, 15, 25}
B = {1, 5, 20, 30}

The resulting arrays are:
  10 20
  10 20 25 30
  10 30
  15 20
  15 20 25 30
  15 30
  25 30
'''


def mergeHelper(a, b, c, i, j, m, n, l, flag):
    if flag:
        if l:
            temp = []
            for i in range(l+1):
                temp.append(c[i])
            print(temp)

        for k in range(i, m):
            if not l:
                c[l] = a[k]
                mergeHelper(a, b, c, k+1, j, m, n, l, not flag)
            else:
                if a[k] > c[l]:
                    c[l+1] = a[k]
                    mergeHelper(a, b, c, k+1, j, m, n, l+1, not flag)
    else:
        for k in range(j, n):
            if b[k] > c[l]:
                c[l+1] = b[k]
                mergeHelper(a, b, c, i, k+1, m, n, l+1, not flag)

def merge(a, b):
    m = len(a)
    n = len(b)
    c = [0]*(m+n)
    mergeHelper(a, b, c, 0, 0, m, n, 0, True)


a = [10, 15, 25]
b = [5, 20, 30]
merge(a, b)