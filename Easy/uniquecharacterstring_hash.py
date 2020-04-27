def firstuniqchar(str1):

    mydict = {}

    for i in range(len(str1)):
        if str1[i] not in mydict.keys():
            mydict[str1[i]] = 1
        else:
            mydict[str1[i]] += 1

    for i in range(len(str1)):
        if mydict[str1[i]] == 1:
            return i



s = "loveleetcode"

print(firstuniqchar(s))