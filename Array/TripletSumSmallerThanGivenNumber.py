'''
Count triplets with sum smaller than a given value
'''

def triplet(lst, sum):
    lst.sort()
    ans = 0
    for i in range(len(lst)-2):
        j = i+1
        k = len(lst)-1

        while j<k:
            if lst[i] + lst[j] + lst[k] <= sum:
                k -= 1
            else:
                ans += (k-j)
                j += 1

    return ans

ans = triplet([5, 1, 3, 4, 7], 12)
print(ans)