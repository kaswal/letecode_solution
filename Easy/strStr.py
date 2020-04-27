def needlehaystack(hay, need=''):
    if need == '':
        return 0

    if need in hay:
        return hay.index(need)
    else:
        return -1


haystack = 'hello'
needle = 'll'

print(needlehaystack(haystack, needle))
