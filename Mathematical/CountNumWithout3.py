'''
Count numbers that don’t contain 3
Given a number n, write a function that returns count of numbers from 1 to n that don’t contain digit 3 in their decimal representation

Solve using recursion
msd <- most significant digit
d <- number of digits in n

if n < 3 result n
if n >=3 and n<10 return n-1
else  msd is not 3
count = count(msd)*count(10^(d-1)-1) + count(msd) + count(n % 10^(d-1))
else
count = count(msd * (10^(d-1)) - 1)
'''

def count(n):
    if n < 3: return n
    if n >= 3 and n < 10: return n-1

    p = 1
    while n//p > 9: p *= 10

    msd = n//p
    if msd != 3:
        return count(msd)*count(p-1) + count(msd) + count(n%p)
    else:
        return count(msd*p -1)

def main():
    print(count(578))

if __name__ == '__main__':
    main()