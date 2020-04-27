def maximumsubarray(arr):

    max_subarray = arr[0]
    largest = max_subarray

    for i in range(1, len(arr)):

        if arr[i] > arr[i] + max_subarray:
            max_subarray = arr[i]
            largest = max_subarray

        else:
            max_subarray = arr[i] + max_subarray
            if largest < max_subarray:
                largest = max_subarray

    return largest



arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maximumsubarray(arr))
