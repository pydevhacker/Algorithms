'''

'''


def findlength(a):
    maxlen = 0
    #sort array
    a.sort()

    low = 0
    high = 0
    for i in range(1, len(a)):
        if a[i-1] + 1 == a[i]:
            high += 1
        else:
            low = i
            high = i
    maxlen = max(maxlen, high-low+1)

    return maxlen

print(findlength([1, 56, 58, 57, 90, 92, 94, 93, 91, 45]))

