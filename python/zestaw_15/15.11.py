def insertion_sort(T, n):
    # Zaczynamy od indexu 1 
    # (w pythonie liczymy od 0)
    for i in range(1, n):
        k = T[i]
        j = i - 1
        # (i >= 0 bo w pythonie liczymy od 0) 
        while j >= 0 and T[j] > k:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = k
        
        
some_list = [5,4,3,1,7,4,7,9]
insertion_sort(some_list, len(some_list))
print(some_list)


# ---------------------------


# min_i >= 0, min_i < max_i < n
def insertion_sort_between(T, min_i, max_i):
    # Zaczynamy od indexu 1 
    # (w pythonie liczymy od 0)
    for i in range(min_i + 1, max_i + 1):
        k = T[i]
        j = i - 1
        # (i >= 0 bo w pythonie liczymy od 0) 
        while j >= min_i and T[j] > k:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = k
        
        
some_list = [5,4,3,1,7,4,1,2]
insertion_sort_between(some_list, 2, 5 )
print(some_list)