def maximal_square(arr):
    # dp = []

    rows, cols = len(input_arr) - 1, len(input_arr[0]) - 1

    largest = 0
    for i in range(rows):
        m = i + 1
        # row = []
        for j in range(cols):
            # row.append(arr[m][j] + arr[m][j + 1] + arr[m - 1][j] + arr[m - 1][j + 1])
            sum_of_square = arr[m][j] + arr[m][j + 1] + arr[m - 1][j] + arr[m - 1][j + 1]
            if sum_of_square >= largest:
                largest = sum_of_square

        # dp.append(row)

    # return(dp)
    return(largest)


input_arr = [

    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]

]

print(maximal_square(input_arr))
