'''
Pythagorean Triplet in an array
Write a function that return true if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2, present in an array
'''


def is_triplet(a):
    #take square of all the element in an array
    a = [i*i for i in a]

    #sort array
    a.sort()

    for e in range(len(a)-1, 1, -1):
        l = 0
        r = e-1
        while l<r:
            if a[l] + a[r] == a[e]:
                return True
            if a[l] + a[r] < a[e]:
                l += 1
            else:
                r -= 1
    return False

a = [3, 1, 4, 6, 5]

print(is_triplet(a))

print(is_triplet([10, 4, 6, 12, 5]))