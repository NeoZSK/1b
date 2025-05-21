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
