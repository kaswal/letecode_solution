def three_sum(arr):
    final_arr = []

    for i in range(len(arr)-2):

        temp = []

        for j in range(i + 1, len(arr)):

            k = j + 1

            while k < len(arr):

                if arr[i] + arr[j] + arr[k] == 0:
                    temp.append(arr[i])
                    temp.append(arr[j])
                    temp.append(arr[k])
                    if sorted(temp) not in final_arr:
                        final_arr.append(temp)
                    temp = []
                    break

                else:
                    k += 1


    return final_arr


input_list = [-1, 0, 1, 2, -1, -4]

print(three_sum(input_list))
