def is_even(x):
    return x%2==0

def make_keeper(n):
    def g(f):
        i=1
        while i<=n:
            if f(i)==True:
                print(i)
            i+=1
    return g
make_keeper(5)(lambda x:True)