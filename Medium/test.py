mydict = {1: 3, 2: 2, 3: 1}
# mydict = {1: 1}
k = 2
i = 0
arr = []
while i < k:

    arr.append(mydict.get(max(mydict.values())))
    del mydict[mydict.get(max(mydict.values()))]

    k -= 1

print(arr)