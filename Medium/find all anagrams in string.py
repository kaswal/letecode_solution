def anagram(pdict1, sub_str):
    mydict = {}

    for i in range(len(sub_str)):
        if sub_str[i] not in mydict.keys():
            mydict[sub_str[i]] = 1
        else:
            mydict[sub_str[i]] += 1

    for key, value in mydict.items():
        if key not in pdict1:
            return False
        elif mydict[key] != pdict1[key]:
            return False

    return True


def find_anagram(s, p):
    dp = []
    pdict = {}

    for i in range(len(p)):
        if p[i] not in pdict.keys():
            pdict[p[i]] = 1
        else:
            pdict[p[i]] += 1

    for i in range((len(s) - len(p)) + 1):
        if anagram(pdict, s[i:i + len(p)]):
            dp.append(i)

    return dp


s = "bacdeabcda"
p = "abcd"

print(find_anagram(s, p))
