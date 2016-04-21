
def search(a, key):
    l = 0
    h = len(a)-1
    mid = -1
    while(l<h):
        mid = (l+h)//2
        if a[mid] == key: return mid
        if a[i] <= a[mid]:
            if key >= a[i] and key <= a[mid]:
                h = mid-1
            else:
                l = mid+1
        else:
            if key>=a[mid] and key<=a[h]:
                l = mid+1
            else:
                h = mid-1
    return mid

a = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
print(search(a, 6))