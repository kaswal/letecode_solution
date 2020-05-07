def longest_sub_without_repeating_char(mystr):
    greatest = 1


    for i in range(len(mystr) - 1):
        flag = True
        newstr = ''
        newstr += mystr[i]

        for j in range(i + 1, len(mystr)):
            if mystr[j] not in newstr:
                newstr += mystr[j]

            else:
                if len(newstr) > greatest:
                    greatest = len(newstr)
                flag = False
                break

        if flag:
            if len(newstr) > greatest:
                greatest = len(newstr)
                return greatest

    return greatest


print(longest_sub_without_repeating_char('pwwkew'))
