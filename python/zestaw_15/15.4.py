# def swap(T, k, l):
#     (T[k], T[l]) = (T[l], T[k])
#     return T


def swap2(T, k, l):
    T[k] += T[l]
    T[l] = T[k] - T[l]
    T[k] -= T[l]  
    return T
    

    
    
    # Howto ze zmienną pomocniczą?
    # Howto bez?

print(swap2([0,1,2,3,4], 2, 4))





# [a, b] = input("put two values: ").split(" ")

# print(a)
# print(b)

# a += b
# b = a - b
# a -= b