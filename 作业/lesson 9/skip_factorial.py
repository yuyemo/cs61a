def skip_factorial(n):
    if n<=0:
        return 1
    else:
        return n*skip_factorial(n-2)
print(skip_factorial(5))
print(skip_factorial(8))