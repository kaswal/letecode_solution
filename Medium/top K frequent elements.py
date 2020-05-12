def top_k_freq_elements(arr, k):

    mydict = {}
    for i in range(len(arr)):
        if arr[i] not in mydict.keys():
            mydict[arr[i]] = 1
        else:
            mydict[arr[i]] += 1

    bucket = [None] * (max(mydict.values()) + 1)

    for key in mydict.keys():
        val = mydict[key]
        if bucket[val] is None:
            bucket[val] = [key]

        else:
            bucket[val].append(key)

    result = []

    y = k
    for num in reversed(bucket):
        if num is not None:
            while y > 0 and len(num) != 0:
                result.append(num.pop(0))
                y = k - len(result)

    return result


print(top_k_freq_elements([1, 2, 2, 2, 3, 3, 4, 4, 4], 2))

print(top_k_freq_elements([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 4, 5, 5], 3))

# print(top_k_freq_elements([1], 1))

# print(top_k_freq_elements([1, 1, 1, 2, 2, 3, 3, 3], 2))

# print(top_k_freq_elements([5, 5, 4, 5, 6, 8, 6], 3))
