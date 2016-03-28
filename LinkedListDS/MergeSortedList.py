'''
Merge two sorted linked lists such that merged list is in reverse order
'''

def merge(l1, l2):
    res = list()
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1

    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            res.append(l2[j])
            j += 1

    if i < len(l1):
        for k in range(i, len(l1)):
            res.append(l1[k])
    if j < len(l2):
        for k in range(j, len(l2)):
            res.append(l2[k])

    return res

a = [5, 10, 15]

b = [2, 3, 20]

r = merge(a, b)
print(r[::-1])
