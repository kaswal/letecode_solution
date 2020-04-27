def jump_game(arr):

    j = 0
    final_destination = len(arr) - 1

    for i in range(j, len(arr)):
        j = arr[i] + i

        if j > final_destination:
            return False

        elif j == 0:
            return False

        elif j == final_destination:
            return True


print(jump_game([3,2,1,0,4]))