def longest_increasing_subseq(arr):

    myarr = []

    i = 1

    while i < len(arr):
        if arr[i] > arr[i - 1]:
            if len(myarr) == 0:
                myarr.append(arr[i - 1])
                myarr.append(arr[i])
            else:
                if myarr[-1] >= arr[i - 1]:
                    myarr.append(arr[i])
                else:
                    myarr.append(arr[i - 1])
                    myarr.append(arr[i])

        i += 1

    return myarr


print(longest_increasing_subseq([3,4,-1,0,6,2,3]))
