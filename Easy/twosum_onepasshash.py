def twosum(nums, target):

    mydict = {}

    for i in range(len(nums)):
        t = target-nums[i]

        if t not in mydict.keys():
            mydict[nums[i]] = i
        else:
            return [mydict[t], i]

    return None

nums = [2, 7, 11, 15]
target = 9

print(twosum(nums, target))