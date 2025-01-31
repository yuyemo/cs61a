def divisible_by_k(n,k):
    i=0
    num=0
    while i<=n:
        i+=1
        if i%k==0:
            print(i)
            num+=1
    return num
x,y=int(input('n=')),int(input('m='))
print('num=' + str(divisible_by_k(x, y)))
