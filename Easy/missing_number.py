def missing_number(arr):
    min = sorted(arr)[0]
    max = sorted(arr)[-1]

    for num in range(min, max + 1):
        if num not in arr:
            return num


input = [1,1,3,4,5]
print(missing_number(input))
