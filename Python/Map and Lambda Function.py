def cube(x): return pow(x, 3)  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers

    fibo = [0, 1]

    for i in range(2, n):
        fibo.append(fibo[i-2] + fibo[i-1])

    return(fibo[0:n])


if __name__ == '__main__':
