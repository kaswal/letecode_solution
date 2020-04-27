def factorial_trailing_zeroes(n):
    count = 0
    i = 5

    while n / i >= 1:
        count += int(n / i)
        i *= 5

    return count


num = 74

print(factorial_trailing_zeroes(num))
