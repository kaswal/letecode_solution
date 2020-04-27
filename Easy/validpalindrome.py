def validpalindrome(mystr):

    newstr = ''

    for i in range(len(mystr)):
        if mystr[i].isalpha():
            if mystr[i].isupper():
                newstr += mystr[i].lower()
            else:
                newstr += mystr[i]
        elif mystr[i].isnumeric():
            newstr += mystr[i]

    return newstr == newstr[::-1]


input = "0ni1iN0"
print(validpalindrome(input))
