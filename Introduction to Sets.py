def average(array):
    
    distinct = set(array)

    sum = 0
    
    for num in distinct:
        sum += num

    average = sum / len(distinct)

    return average


