def majorityalemant(arr):
    candidate_element = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] != candidate_element:
            count -= 1

            if count == 0:
                candidate_element = arr[i]
                count = 1

        else:
            count += 1

    if count == 0:
        return "No Majority element is present"

    count = 0

    for i in range(len(arr)):
        if arr[i] == candidate_element:
            count += 1

    if count > len(arr) // 2:
        return candidate_element
    else:
        return "No Majority element is present"


input = [4, 7, 4, 4, 7, 4, 4, 9, 4, 3]
print(majorityalemant(input))
