def make_multiplier(x):

    def mulpiplier(n):
        return x*n
    
    return mulpiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))