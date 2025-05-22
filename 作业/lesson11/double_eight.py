def double_eight(k):
    if k<10:
        return False
    last_two,all_but_last=k%100,k//10
    if last_two==88:
        return True
    else:
        return double_eight(all_but_last)