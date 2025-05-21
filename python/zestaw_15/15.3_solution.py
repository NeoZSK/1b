# T - tablica o długości n
#  0 <= k <= l < n
def min_idx(T, k, l):
    min_idx = k
    for i in range(k, l+1):
        if(T[i] < T[min_idx]):
            min_idx = i
    return min_idx


some_list = [0,5,4,3,2,-10,5,6,7,1]
m = min_idx(some_list, 3, 8)
print(f"min_idx: {m}, value: {some_list[m]}")