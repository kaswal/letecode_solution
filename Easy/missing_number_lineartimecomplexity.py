def missing_number(arr):

    min = sorted(arr)[0]
    max = sorted(arr)[-1]

    mydict = {}

    for num in arr:
        if num not in mydict.keys():
            mydict[num] = 1
        else:
            mydict[num] += 1

    for nums in range(min, max+1):
        if nums not in mydict.keys():
            return nums

input = [1, 1, 3, 4, 5]
print(missing_number(input))
