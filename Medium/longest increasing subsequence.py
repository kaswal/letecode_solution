def longest_increasing_subseq(arr):
    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(longest_increasing_subseq([3, 4, -1, 0, 6, 2, 3]))
