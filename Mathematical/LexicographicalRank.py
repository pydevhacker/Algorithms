'''
Find Lexicographical Rank of a String
if a string is given then find all possible permutation of that string which are lexicographically smaller than original string.
'abc' - rank 1
'acb' - rank 2 and so on

Solution :
find the number of chars which are smaller than the current string char
and find the empty position after that char.
small permulation will be char * (empty position)!
'''

def fact(n):
    if n<=1: return 1
    return n*fact(n-1)

def rank(s):
    l = len(s)
    f = fact(l)

    count = [0]*256
    for i in list(s):
        count[ord(i)] += 1
    for i in range(1, 256):
        count[i] += count[i-1]

    r = 1
    for i in range(l):
        f = f//(l-i)
        small_chars = count[ord(s[i]) - 1]
        r += (small_chars*f)

        #update count for char greater than ith
        for j in range(ord(s[i]), 256): count[j] -= 1
    return r

def main():
    r = rank('string')
    print(r)

if __name__ == '__main__':
    main()

