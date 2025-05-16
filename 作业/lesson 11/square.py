from math import sqrt
def square(s):
    t=[]
    for x in s:
        m=int(sqrt(x))
        if m**2==x:
            t.append(m)
    return t