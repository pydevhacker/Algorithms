'''
Reverse an array without affecting special characters
'''

def reverse(s):
    str = list(s)

    r = len(str)-1
    l = 0

    while l<r :
        if not str[l].isalpha():
            l += 1
        elif not str[r].isalpha():
            r -= 1
        else:
            str[l], str[r] = str[r], str[l]
            l += 1
            r -= 1
    return ''.join(str)

inputStr = "a!!!b.c.d,e'f,ghi"
outputStr = reverse(inputStr)

print("Input String : ", inputStr)
print("Output String: ", outputStr)