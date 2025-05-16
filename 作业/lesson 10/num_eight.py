def num_eight(n):
    m=0
    def add_i(i,m):
        if i<10:
            if i==8:
                m+=1
            return m
        else:
            last,all_last=i%10,i//10
            if last==8:
                m+=1
            return add_i(all_last,m)
    return add_i(n,m)
print(num_eight(83434848))    
    

