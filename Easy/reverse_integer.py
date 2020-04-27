def reverseinteger(num):

    num_in_str = str(num)

    rev = num_in_str[::-1]

    if rev[-1] == '-':
        return int(rev[-1] + rev[:-1])

    elif rev[0] == '0':
        return int(rev[1:])

    elif rev[0] == '0' and rev[-1] == '-1':
        return int(rev[-1] + rev[1:-1])

    else:
        return int(rev)

input = -120

print(reverseinteger(input))