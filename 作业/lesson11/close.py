def close(s,k):
    i=0
    for x in range(len(s)):
        if abs(s[x]-x)<=k:
            i+=1
    return i
