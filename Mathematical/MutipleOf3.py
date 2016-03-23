'''
Time Complexity : O(logn)
'''
def multipleOf3(n):

    odd_count = 0
    even_count = 0

    if n < 0 : n = -n
    if n == 0: return True
    if n == 1: return False

    while n:
        #Odd digit
        if n & 1:
            odd_count += 1

        n >>= 1
        #Even digit
        if n & 1:
            even_count += 1

        n >>= 1

    return multipleOf3(abs(odd_count - even_count))

print(multipleOf3(21))