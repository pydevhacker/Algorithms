

def editDistance(s1, s2):
    m = len(s1)
    n = len(s2)

    d = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] == i
            elif s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1])
    return d[m][n]

def main():
    s1 = 'sunday'
    s2 = 'saturday'

    print(editDistance(s1, s2))

if __name__ == '__main__':
    main()