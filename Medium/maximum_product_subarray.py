def max_pro_subarray(arr):
    max_product = arr[0]
    largest = max_product

    for i in range(1, len(arr)):
        if arr[i] < arr[i] * max_product:
            max_product = arr[i] * max_product
            largest = max_product

        else:
            max_product = arr[i]
            if largest < max_product:
                largest = max_product

    return largest


print(max_pro_subarray([2, 3, -2, -4]))
