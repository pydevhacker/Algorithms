

def permute(a, l, r, perm):
    if l == r:
        perm.append(''.join(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, perm)
            a[l], a[i] = a[i] , a[l]

    return perm

str = "ABC"
perm = []
permute(list("ABC"), 0, len(str)-1, perm)
print(perm)