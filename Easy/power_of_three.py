def power_of_three(n):

    while n % 3 == 0:
        n = n // 3

    return n == 1


num = 27
print(power_of_three(num))
