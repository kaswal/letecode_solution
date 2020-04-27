def remdup(arr):
    current = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] != current:
            count += 1
            current = arr[i]

    return count


test = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(remdup(test))
