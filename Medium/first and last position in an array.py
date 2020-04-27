def first_last(arr, target):
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        mp = upper + lower // 2

        if target == arr[mp]:
            start_ind = mp
            end_ind = mp
            np = mp - 1
            while arr[np] == target:
                start_ind = np
                np -= 1
            np = mp + 1
            while arr[np] == target:
                end_ind = np
                np += 1
            return [start_ind, end_ind]

        if target >= arr[mp]:
            lower = mp + 1

        else:
            upper = mp - 1

    if lower > upper:
        return [-1, -1]


print(first_last([5,8,8,9,10], 8))
