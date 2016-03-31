'''
Babylonian method for a square root
Newton-Raphson method
'''

def sqrt(n):
    x = n
    y = 1
    e = 0.000001 # decides the accuracy level
    while x-y > e:
        x = (x+y)/2
        y = n/x
    return x

def main():
    print(sqrt(50))

if __name__ == '__main__':
    main()