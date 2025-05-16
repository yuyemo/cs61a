def close_list(s,k):
    t=[]
    for x in range(len(s)):
        if abs(s[x]-x)<=k:
            t.append(s[x])
    return t
