def horner_iter(T, n, x):
    res = 0
    for elem in T:
        res *= x
        res += elem
    return res


def horner_rec(T, n, x):
    if(n == 1):
        return T[0]
    elif(n > 1):
        return horner_rec(T, n-1, x) * x + T[n-1]
        
        
res = horner_rec([2,2,2], 3, 2)
res2 = horner_iter([2,2,2], 3, 2)

print(res)
print(res2)

