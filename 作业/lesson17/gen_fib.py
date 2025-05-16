def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

t=filter(lambda n: n > 2025, gen_fib())


