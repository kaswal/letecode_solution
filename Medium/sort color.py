def sort_color(arr):
    mydict = {}

    for i in range(len(arr)):
        if arr[i] not in mydict.keys():
            mydict[arr[i]] = 1
        else:
            mydict[arr[i]] += 1

    arr = []

    i = 0

    while i < len(mydict):
        min_obj = min(mydict.keys())
        min_obj_val = mydict[min_obj]
        for j in range(min_obj_val):
            arr.append(min_obj)
        del mydict[min_obj]

    return arr

print(sort_color([2,0,2,1,1,0]))