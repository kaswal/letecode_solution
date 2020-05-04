def word_break(s, wd):
    dp = [False] * (len(s) + 1)

    dp[0] = True

    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i:j+1] in wd:
                dp[j+1] = True

    return dp


mystr = 'catsandog'
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(word_break(mystr, wordDict))
