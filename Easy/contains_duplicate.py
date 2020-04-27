def contains_duplicate(arr):
    return len(arr) != len(set(arr))

nums = [1,2,3,4]
print(contains_duplicate(nums))