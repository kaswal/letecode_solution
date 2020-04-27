def find_factorial(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * find_factorial(n - 1)


def trailing_zeroes(number):
    mystr = str(find_factorial(number))

    count = 0

    if mystr[-1] == '0':
        count = 1
        for i in range(1, len(mystr)):
            if mystr[-i - 1] == '0':
                count += 1
            else:
                return count

    return count


num = 3

print(trailing_zeroes(num))
