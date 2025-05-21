def Power(k, a):    
    result = 1
    for bit in reversed(a):
        if bit == 1:
            result *= k        
        k *= k 
    return result

print(Power(3,[1,1,0,1]))