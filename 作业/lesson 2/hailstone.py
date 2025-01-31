def hailstone(n):
    if(n==1):
        return 1
    q=n
    i=1
    while q!=1:
        if q%2==0:
            q=q//2
        else :
            q=q*3+1
        i=i+1
    return i