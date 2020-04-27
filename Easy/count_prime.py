def countprimes(n):
    if n == 1 or n == 2:
        return n - 1

    else:
        total_count = 1

        for i in range(3, n + 1):
            if i % 2 != 0:
                j = 3
                flag = True

                while j < i:
                    if i % j == 0:
                        flag = False
                        break

                    else:
                        j += 1

                if flag:
                    total_count += 1

        return total_count


num = 50

print(countprimes(num))
