# T - tablica o długości n
#  0 <= k <= l < n
def swap(T, k, l):
    temp = T[k]
    T[k] = T[l]
    T[l] = temp
    return T


print("swap1:")

T = [0,1,2,3,4]
print(T)
print(swap(T, 1, 4))
# Warning:
# print(T)










# T - tablica o długości n
#  0 <= k <= l < n
def swap2(T, k, l):
    T[k] += T[l]
    T[l] = T[k] - T[l]
    T[k] -= T[l]
    return T


print("\nswap2")
T = [0,1,2,3,4]
print(T)
print(swap(T, 1, 4))
# Warning:
# print(T)
