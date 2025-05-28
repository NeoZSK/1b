def pow_naive(k, a):
    res = 1
    while(a>0):
        res *= k
        a -= 1
    return res

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


def horner_naive(T, n, x):
    res = 0
    for (idx, elem) in enumerate(T, start=1):
        res += elem * pow_naive(x, n-idx)
    return res
 
def horner(T, n, x):
    res = 0
    for (idx, elem) in enumerate(T, start=1):
        res += elem * pow_quick(x, n-idx)
    return res     

def horner_iterative(T, n, x):
    res = 0
    for elem in T:
        res *= x
        res += elem
    return res

def run(func):
    t = [1,1,1,1,1,1]
    res = func(t, len(t), 5)
    print(f"{func.__name__}: {res}")

# run(horner_naive)
# run(horner)
# run(horner_iterative)

from time import time
    
def measure_time(func):
    T = list([1]*10000)
    n = len(T)
    x = 2
    
    t1 = time()
    res = func(T,n,x)
    print(f"{func.__name__:20s}: {(time() - t1):.3f}")



print("\n--- times ---")

measure_time(horner_naive)
measure_time(horner)
measure_time(horner_iterative)
