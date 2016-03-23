'''
Time Complexity : O(1)

Shift the number by 3 bits and substract the number from original number
'''

def multiply(n):
    return ((n<<3) - n)

print(multiply(4))