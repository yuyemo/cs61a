def is_prime(n):
    if n==2:
        return True
    def check(k):
        if n%k==0:
            return False
        else:
            k+=1
            if k>=n:
                return True
            return check(k)
    return check(2)
print(is_prime(7))
