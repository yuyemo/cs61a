def swipe(n):
    if n<10:
        print(n)
    else:
        def divide(k):
            last,all_but_last=k%10,k//10
            print(last)
            return swipe(all_but_last)
        divide(n)
        print(n%10)
    return True
swipe(1234)