def searchinsertpos(arr, val):

    for i in range(len(arr)):
        if arr[i] == val:
            return i

        else:
            if arr[i] > val:
                return i
    return i+1


input = [1,3,5,6]
target_val = 0

print(searchinsertpos(input, target_val))