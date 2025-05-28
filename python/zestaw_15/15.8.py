def pow_quick(k, a):
    res = 1
    while a > 0:
        if a % 2 == 1:
            res *= k
            a -= 1
        else:
            k = k*k
            a //= 2
    return res



def evaluate(T, n, x):
    result = 0
    for i in range(0, n):
        powed = pow_quick(x, n - (i + 1))
        result += T[i] * powed

    return result    
    
res = evaluate([5,4,0,4], 4, 50)
print(res)



def evaluate_iterative(T, n, x):
    res = 0
    for elem in T:
        res *= x
        res += elem
    return res