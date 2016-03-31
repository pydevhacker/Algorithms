'''
Recursion
Time Complexity : exponential
'''

def fibRec(n):
    if n <= 1:
        return n
    return fibRec(n-1) + fibRec(n-2)

#Dynamic programming O(n)
def fibDP(n):
    f = list() #space complexity O(n)
    f.append(0)
    f.append(1)
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

#optimized dynamic programming ; Space complexity O(1)
def fibDPOpt(n):
    f = 0
    a = 0
    b = 1
    if n == 0: return a
    for i in range(2, n+1):
        f = a + b
        a = b
        b = f
    return b

# Matrix Multiplication O(n)
def multiply(f, m):
    w = f[0][0]*m[0][0] + f[0][1]*m[1][0]
    x = f[0][0]*m[0][1] + f[0][1]*m[1][1]
    y = f[1][0]*m[0][0] + f[1][1]*m[1][0]
    z = f[1][0]*m[1][1] + f[1][1]*m[1][1]

    f[0][0] = w
    f[0][1] = x
    f[1][0] = y
    f[1][1] = z

def power(f, n):
    m = [[1,1],[1,0]]
    for i in range(2, n+1):
        multiply(f, m)

def fibMM(n):
    f = [[1,1],[1,0]]
    if n == 0: return 0
    power(f, n-1)
    return f[0][0]

# optimized matrix multiplication O(Logn)
def powerOpt(f, n):
    if n == 0 or n == 1:
        return
    m = [[1,1],[1,0]]
    powerOpt(f, n//2)
    multiply(f, f)
    if n%2 != 0:
        multiply(f, m)

