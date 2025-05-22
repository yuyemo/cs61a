def interleaved_sum(n,odd_func,even_func):
    def middle_o(i):
        if i>=n:
            return odd_func(i)
        return odd_func(i)+middle_e(i+1)
    def middle_e(m):
        if m>=n:
            return even_func(m)
        return even_func(m)+middle_o(m+1)
    return middle_o(1)
print(interleaved_sum(5,lambda x: x,lambda x: x * x))
     