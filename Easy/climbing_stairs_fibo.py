def climb_stairs(n):
    if n == 1 or n == 2:
        return n

    else:
        return climb_stairs(n-1) + climb_stairs(n-2)

n = 6

print(climb_stairs(n))

# 1 1 2 3 5 8 13