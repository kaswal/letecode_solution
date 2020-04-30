def anagram(w, s):
    mydict = {}

    for i in range(len(s)):
        if s[i] not in mydict.keys():
            mydict[s[i]] = 1
        else:
            mydict[s[i]] += 1

    for key, value in mydict.items():
        if key not in w:
            return False
        elif mydict[key] != w[key]:
            return False

    return True


word = {'a': 1, 'b': 1, 'c': 1}
print(anagram(word, 'abc'))
