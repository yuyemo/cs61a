def sum_digits(y):
    i=0
    sum=0
    while y>0:
        n=y%10
        sum=sum+n
        y=y//10
    return sum
x=int(input('y='))
print('sum_digit='+str(sum_digits(x)))