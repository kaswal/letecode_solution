def len_of_last_word(mystr):

    if len(mystr) == 0:
        return 0

    elif len(mystr.split()) == 1:
        return len(mystr)

    else:
        return len(mystr.split()[-1])

input = "hello world"

print(len_of_last_word(input))