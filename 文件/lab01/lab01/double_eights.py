def double_eights(n):
    i=0
    while n>0:
       if n%10==8:
           i+=1
       else:
           i=0
       if i==2:
        return True
       n=n//10
    return False
x=int(input('n='))
print(double_eights(x))