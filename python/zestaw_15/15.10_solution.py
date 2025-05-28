def swap(T, i, j):
    (T[i], T[j]) = (T[j], T[i])

# Funkcja sortuje tablicę liczb rosnąco
# T - tablica liczb
# n - długość tablicy
def sort_min(T, n):
    for i in range(n):
        for j in range(i+1, n):
            if(T[j] < T[i]):
                swap(T, i, j)
    return T


print(sort_min([6,3,7,1,7], 4))