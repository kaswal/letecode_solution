# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string ""

def longestCommonPrefix(strs):

    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for items in strs:
            if items[i] != char:
                return f"'{shortest[:i]}'"
    return f"'{shortest}'"


list1 =["flower","flow","flight"]
print(longestCommonPrefix(list1))