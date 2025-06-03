# b)


def a(k):
    if(k == 1):
        return 6
    
    if(k > 1):
        return 2*a(k-1)+7
    
    
print(a(7))