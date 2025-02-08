def match_k(k):
    def input_n(n):
        t=pow(10,k)
        i=n%t
        while n>0:
            if n%t!=i:
                return False
            n//=t
        return True
    return input_n
print(match_k(4)(123123123))