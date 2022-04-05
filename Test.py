

def fib(x):
    result = (0, 1)
    i = 2
    for i in x:
        result[0] = 0
        result[1] = 1
        result[i] = result[i - 1] + result[i - 2]
    return print(result[x])


fib(3)




