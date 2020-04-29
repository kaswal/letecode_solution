def word_break(s, wordDict):

    newstr = ''
    i = 0
    while i < len(s) - 1:
        for j in range(i+1, len(s)):
            if s[i:j] in wd:
                newstr += s[i:j]
                i = j
                print(newstr)
                break
            i += 1

    print(newstr)
    if len(newstr) == len(s):
        return True
    return False


mystr = "catsandog"
wd = ["cats", "dog", "sand", "and", "cat"]

print(word_break(mystr, wd))