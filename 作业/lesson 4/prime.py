from math import sqrt
def is_prime(n):
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True
x=int(input('n='))
print(is_prime(x))
