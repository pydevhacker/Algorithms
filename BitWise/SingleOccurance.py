

def single(a, n):
    ones = 0
    twos = 0
    common_bit_mask = 0

    for i in range(n):

        twos = twos | ones & a[i]

        ones = ones ^ a[i]

        common_bit_mask = ~(ones & twos)

        ones = ones & common_bit_mask

        twos = twos & common_bit_mask

    return ones


a = [3, 3, 2, 3]
n = len(a)
#print(single(a, n))


def countSetBit(n):
    count = 0
    temp = n
    while temp >= 1:
        temp = temp>>1
        count+=1

    setBit = 0
    while count>=0:
        temp = n>>count
        if temp == 1:
            setBit += 1
            temp = temp << count
            n = n^temp
        count -= 1
    return setBit

for i in range(10):
    print(i, countSetBit(i))
    