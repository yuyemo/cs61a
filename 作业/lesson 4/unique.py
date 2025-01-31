def has_digit(n, k):
    assert k >= 0 and k < 10,"k必须是10以内的正整数"
    while n>0:
        if k==n%10:
            return True
        n//=10
    return False
def unique_digits(n):
    i=0
    q=0
    while q<10:
        if has_digit(n,q):
            i+=1
        q+=1
    return i
x=int(input('n='))
print(unique_digits(x))