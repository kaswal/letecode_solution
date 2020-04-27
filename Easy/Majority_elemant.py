def majorityelemant(arr):
    mydict = {}

    for i in range(len(arr)):
        if arr[i] not in mydict.keys():
            mydict[arr[i]] = 1
        else:
            mydict[arr[i]] += 1

    for k, v in mydict.items():
        if v == max(mydict.values()) and v > len(arr) // 2:
            return k
    return None


input = [1, 7, 8, 2, 6, 8, 1, 3, 2, 8]
print(majorityelemant(input))
