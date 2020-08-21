def mutate_string(string, position, character):

    mylist = list(string)
    mylist[position] = character

    output = ''.join(mylist)

    return output

