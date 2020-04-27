def sqrt(n):

    newstr = str(n ** (1 / 2))
    ind_of_decimal = newstr.index('.')

    return int(newstr[:ind_of_decimal])


num = 8

print(sqrt(num))
