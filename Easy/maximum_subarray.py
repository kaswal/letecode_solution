def maximumsubarray(arr):
    largest_sum = arr[0]
    mydict = {}

    for i in range(len(arr)):

        temp = [arr[i]]
        t = 0

        for j in range(i + 1, len(arr)):
            t = sum(temp) + arr[j]

            if t >= largest_sum:
                temp.append(arr[j])
                largest_sum = t

            else:
                key = str(temp)
                if len(mydict) == 0:
                    mydict[key] = largest_sum
                    break
                else:
                    if max(mydict.values()) < largest_sum:
                        mydict[key] = largest_sum
                        break
                    else:
                        break

    return max(mydict.keys())


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maximumsubarray(arr))