'''
http://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
'''


def all_possible_palindrome_partition(s):
    str = list(s)
    length = len(s)
    result = []
    for i in range(1, length+1):
        for j in range(length-i+1):
            temp_str = s[j:j+i]
            if is_palindrome(temp_str):
                result.append(temp_str)
    return result


def is_palindrome(s):

    if len(s) == 1:
        return True

    l = 0
    r = len(s)-1
    while l<r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def longestPalPartition(s):

    maxLength = 1
    str = list(s)

    start = 0
    length = len(str)

    low = 0
    high = 0

    for i in range(1, length):
        #even length
        low = i-1
        high = i
        while low>=0 and high < length and str[low] == str[high]:
            if high-low + 1 > maxLength:
                maxLength = high-low+1
                start = low
            low -= 1
            high += 1

        #odd
        low = i-1
        high = i+1
        while low >= 0 and high < length and str[low] == str[high]:
            if high-low+1 > maxLength:
                maxLength = high-low+1
                start = low
            low -= 1
            high += 1

    print(s[start:start+maxLength])
    print("Lenght : ", maxLength)

string = "forgeeksskeegfor"
longestPalPartition(string)

string = "nitin"
result = all_possible_palindrome_partition(string)
print(result)