def hailstone(n):
    print(n)
    if n%2==0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return hailstone(n/2)+1

def odd(n):
    if n==1:
        return 1
    else:
        return hailstone(n*3+1)+1
print(hailstone(10))
