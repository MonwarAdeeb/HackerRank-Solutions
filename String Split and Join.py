def split_and_join(line):
    
    line.split()
    output = ''

    for letter in line:
        if letter == ' ':
            output += '-'
        else:
            output += letter

    return output

