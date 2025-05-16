def max_products(s):
    if len(s)==1:
        return s[0]
    if len(s)<=0:
        return 1
    result=max(max_products(s[:-2])*s[-1],max_products(s[:-3])*s[-2])
    return result
