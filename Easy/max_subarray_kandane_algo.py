def maximumsubarray(arr):
    max_so_far = 0
    max_ending_here = 0

    for i in range(len(arr)):

        max_ending_here = arr[i] + max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


arr = [1,2,3,-2,5]

print(maximumsubarray(arr))
