def add_one(arr):
    carry = 0
    unit_ind = len(arr)-1
    for i in range(len(arr) - 1, -1, -1):
        val = arr[i] + carry
        if i == unit_ind and (val + 1) % 10 == 0:
            arr[i] = 0
            carry = 1
        elif i == unit_ind:
            arr[i] = val + 1
        elif arr[i] == 0 and (val % 10) == 0:
            arr[i] = 0
            carry = 0
        elif arr[i] != 0 and (val % 10) == 0:
            arr[i] = 0
            carry = 1
        else:
            arr[i] = val
            carry = 0

    if carry:
        arr.insert(0, carry)
        return arr
    return arr


print(add_one([9, 9, 9]))
