def path(m,n):
    if m==1 and n==1:
        return 1
    elif m<=0 or n<=0:
        return 0
    else:
        return path(m-1,n)+path(m,n-1)