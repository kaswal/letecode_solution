def max_pro_subarray(arr):
    max_product_so_far = arr[0]
    current_max = arr[0]

    for i in range(1, len(arr)):
        current_max = max(arr[i], arr[i] * current_max)
        max_product_so_far = max(current_max, max_product_so_far)

    return max_product_so_far


print(max_pro_subarray([2,3,-2,4]))
