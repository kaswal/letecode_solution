def subarray_sum_equals_k(arr, k):
    mydict = {}
    count = 0
    prefix_sum = 0
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == k:
            count += 1
        if prefix_sum - k not in mydict.keys():
            mydict[prefix_sum] = 1
        else:
            count += 1
            if prefix_sum not in mydict.keys():
                mydict[prefix_sum] = 1
            else:
                mydict[prefix_sum] += 1

    return count


# print(subarray_sum_equals_k([3, 4, 7, 2, -3, 1, 4, 2], 7))
print(subarray_sum_equals_k([1, 1, 1], 2))
