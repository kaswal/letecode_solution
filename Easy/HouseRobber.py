def houserobber(arr):

    sum_of_even = 0
    sum_of_odd = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            sum_of_even += arr[i]

        else:
            sum_of_odd += arr[i]

    if sum_of_even > sum_of_odd:
        return sum_of_even

    return sum_of_odd

input = [0,1,5,3,1,1]

print(houserobber(input))