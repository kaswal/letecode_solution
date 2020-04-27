def reverseinteger(num):
    if -2 ** 31 <= num <= 2 ** 31 - 1:
        newnum = str(num)
        if num >= 0:
            revst = newnum[:: -1]
        else:
            temp = newnum[1:]
            temp2 = temp[:: -1]
            revst = '-' + temp2
        return int(revst)
    else:
        return 0


x = int(input("input your integer value: "))

print(f'Input: {x}')

print(reverseinteger(x))
