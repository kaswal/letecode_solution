
def longest_palindromic_substring(mystr):
    dp = []
    rows, cols = len(mystr), len(mystr)

    for i in range(rows):
        col = []
        for j in range(cols):
            if i == j:
                col.append(True)
            else:
                col.append(0)
        dp.append(col)

    arr = []
    for j in range(1, len(mystr)):
        for i in range(j):
            if mystr[i] == mystr[j] and j - i <= 2:
                # longest = len(mystr[i: j + 1])
                arr.append(mystr[i: j + 1])
                dp[i][j] = True
            elif mystr[i] == mystr[j] and j - i > 2:
                if dp[i + 1][j - 1]:
                    # longest = len(mystr[i: j+1])
                    arr.append(mystr[i: j+1])
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
    # print(longest)
    return arr


print(longest_palindromic_substring('cbbd'))
