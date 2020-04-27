def buyandsellstock(arr):

    min_p = min(arr)
    ind_min = arr.index(min_p)
    max_p = max(arr[ind_min: ])

    if max_p > min_p:
        return max_p - min_p

    return 0


input = [2, 1, 5, 3, 6, 4]

print(buyandsellstock(input))