from collections import defaultdict


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


d = defaultdict(int)
def factorial_mem(n):
    global d

    if d[n]:
        return d[n]
    elif n <= 1:
        d[n] = 1
    else:
        d[n] = n * factorial(n - 1)

    return d[n]


count = 0
def fibonacci(n):
    # -------- counter --------
    global count
    count += 1
    # -------- counter --------

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


s = defaultdict(int)
def fibonacci_mem(n):
    global s

    if s[n]:
        return s[n]
    if n==0:
        s[n]=0
    elif n==1:
        s[n]=1
    else:
        s[n]=fibonacci(n-1)+fibonacci(n-2)
    return s[n]
