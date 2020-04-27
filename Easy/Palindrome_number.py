def palindrome(num):
    return str(num)[::] == str(num)[::-1]

input = 10

print(palindrome(input))