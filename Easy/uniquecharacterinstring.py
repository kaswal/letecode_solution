def firstuniqchar(str1):

    for i in range(len(str1)):

        flag = True

        for j in range(i+1, len(str1)):

            if str1[j] == str1[i]:
                i += 1
                flag = False
                break

        if flag:
            return i

    return 0

s = "leetcode"

print(firstuniqchar(s))