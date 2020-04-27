
def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    return s

input= ["h" ,"e" ,"l" ,"o"]


print(reverseString(input))
