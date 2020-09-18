import textwrap

def wrap(string, max_width):
    count = 0
    wrapped = ''
    for letter in string:
        if count == max_width:
            wrapped += '\n'
            count = 0
        
        wrapped += letter
        count += 1

    return wrapped

if __name__ == '__main__':