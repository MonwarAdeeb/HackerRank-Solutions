if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


    numbers = student_marks[query_name]
    
    avg = float(sum(numbers) / len(numbers))

    print ("{0:.2f}".format(avg)) 
