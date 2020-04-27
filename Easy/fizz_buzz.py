def fizzbuzz(n):

    mylist = []

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            mylist.append("fizzbuzz")
        elif i % 3 == 0:
            mylist.append("fizz")
        elif i % 5 == 0:
            mylist.append("buzz")
        else:
            mylist.append(str(i))

    return mylist

num = 15
print(fizzbuzz(num))