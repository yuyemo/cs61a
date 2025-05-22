def digit_distance(n):
    if n<10:
        return 0
    else:
        last1,last2,all_but_last=n%10,n%100//10,n//10
        return abs(last1-last2)+digit_distance(all_but_last)
print(digit_distance(31415926535))
