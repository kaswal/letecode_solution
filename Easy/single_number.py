def single(arr):

    mydict = {}

    for i in range(len(arr)):
        if arr[i] not in mydict.keys():
            mydict[arr[i]] = 1
        else:
            mydict[arr[i]] += 1

    for k, v in mydict.items():
        if v == 1:
            return k
    return None

input = [1, 2, 1, 2, 4]

print(single(input))