def palindromic_substring(mystr):

    dp = []
    num = len(mystr)
    rows, cols = num, num
    count = 0
    for i in range(rows):
        col = []
        for j in range(cols):
            if i == j:
                count += 1
                col.append(True)
            else:
                col.append(0)
        dp.append(col)

    for j in range(1, len(mystr)):

        for i in range(j):
            if mystr[i] == mystr[j] and j - i <= 2:
                dp[i][j] = True
                count += 1
            elif mystr[i] == mystr[j] and j - i > 2:
                if dp[i + 1][j - 1]:
                    count += 1
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
    return count

print(palindromic_substring('abba'))
