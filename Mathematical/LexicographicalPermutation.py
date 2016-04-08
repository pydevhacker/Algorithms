'''
Find the permutation of string in lexicographical order
'''


def reverseString(string, start, end):

    while start<end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1


def sortString(string):
    strList = list(string)
    strList.sort()
    return ''.join(strList)


def sortedPermutation(string):
    result = []
    size = len(string)
    sortedString = sortString(string)
    string = list(sortedString)
    done = False
    while not done:
        result.append(''.join(string))
        firstChar = -1 #rightmost char which is smaller than its next char
        for i in range(size-2, -1, -1):
            if string[i] < string[i+1]:
                firstChar = i
                break
        if firstChar == -1: done = True
        else:
            secondChar = firstChar + 1 #smallest char in right
            for i in range(secondChar+1, size):
                if string[i] < string[secondChar] and string[i] > string[firstChar]:
                    secondChar = i

            #swap firstchar and second char
            string[firstChar], string[secondChar] = string[secondChar], string[firstChar]
            reverseString(string, firstChar+1, size-1)
    print(result)


def main():
    sortedPermutation('ABCD')

if __name__ == '__main__':
    main()
