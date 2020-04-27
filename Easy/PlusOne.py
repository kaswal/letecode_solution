def plusone(num):

    newstr = str(int("".join(map(str, num))) + 1)

    newlist = " ".join(newstr).split(" ")

    result = map(int, newlist)

    return list(result)


input = [1, 0, 2]

print(plusone(input))
