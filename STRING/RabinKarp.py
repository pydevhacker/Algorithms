'''
Rabin Karp pattern matching algorithm
based on hashing
calculate the hash of pattern
and calculate the hash of all possible sub-strings of text
if two hash are equal and compare pattern and sub-string char by char
- to calculate hash of sub-string
s[a+1,b+1] = rehash( hash(s[a,b] - hash(s[a]) + hash(s[b+1]))mod q
'''


def search(pat, txt, q):
    N = len(txt)
    M = len(pat)
    p = 0 #hash value for pattern p
    t = 0 #hash value for pattern t
    h = 1
    d = 256 # total char

    for i in range(M-1):
        h = (h*d) % q

    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q

    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if pat[j] != txt[j]:
                    break
            j += 1
            if j == M:
                print("pattern found")

        if i< N-M:
            t = (d*(t - ord(txt[i])*h) + ord(txt[i+M]))%q

            if t<0:
                t = t+ q