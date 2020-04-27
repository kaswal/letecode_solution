# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def twosum(list1, tar):
    for i in range(len(list1)):
        if tar - list1[i] >= 1:
            if tar - list1[i] in list1:
                return [i, list1.index(tar - list1[i])]
    return None


mylist = list()

x = int(input("enter how many elements you want in an array: "))

for i in range(x):
    y = int(input(f"num at {i}: "))
    mylist.append(y)

target = int(input("target: "))

print(twosum(mylist, target))
