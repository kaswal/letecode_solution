arr = [3, 4, 2, 1]
dp = []
rows = 4
cols = 11

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
            dp[i][j] = dp[i-1][j]

print(dp)
