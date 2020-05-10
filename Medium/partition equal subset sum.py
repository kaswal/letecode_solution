def part_eq_subset_sum(arr):
    sum_of_arr = 0

    for i in range(len(arr)):
        sum_of_arr += arr[i]

    if sum_of_arr % 2 != 0:
        return False

    dp = []

    rows, cols = len(arr), sum_of_arr + 1

    for i in range(rows):
        col = []
        for j in range(cols):
            if j == 0:
                col.append(True)
            else:
                col.append(False)
        dp.append(col)

    dp[0][arr[0]] = True

    for i in range(1, rows):
        for j in range(1, cols):
            if arr[i] <= j and dp[i - 1][j] == False:
                dp[i][j] = dp[i - 1][j - arr[i]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[rows - 1][cols - 1]


print(part_eq_subset_sum([1, 5, 11, 5]))
print(part_eq_subset_sum([1, 2, 3, 5]))
print(part_eq_subset_sum([1, 2, 3, 4]))
