# T - tablica floatów
# k - index min 
# l - index max 
# 0 <= k <= l < len(T)
# 
# Zwraca index najmniejszego elementu
# z zakresu indexów k-l
def min_i(T, k, l):
    min_val_idx = k
    for i in range(k, l+1):
        if(T[i] < T[min_val_idx]):
            min_val_idx = i
        
        print(f"curr idx: {i}: {T[i]}")
        print(f"min idx:  {min_val_idx}: {T[min_val_idx]}")
        print()
    return min_val_idx

a= [90,10,20,30,-10 ,40,50]
min_idx = min_i(a, 2, 5)
print(f"min_idx: {min_idx}")

print("mix_idx: {min_idx}")