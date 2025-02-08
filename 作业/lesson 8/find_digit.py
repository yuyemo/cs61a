def find_digit(k):
    def input_digit(n):
        i=1
        while i<k:
            n=n//10
            i+=1
        return n%10
    return input_digit
x,y=int(input('x=')),int(input('y='))
print(find_digit(x)(y))