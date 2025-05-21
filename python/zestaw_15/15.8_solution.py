from time import time

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


# def evaluate_naive(T, n, x):
#     res = 0
#     for (idx, elem) in enumerate(T, start=1):
#         res += elem * pow_naive(x, n-idx)
#         # print(f"{elem} * {x}^{n-idx}")
#     return res
 
# t = [4,5,6,7]
# res = evaluate_naive(t, len(t), 3)
# print(f"evaluate_naive: {res}")


def evaluate(T, n, x):
    res = 0
    for (idx, elem) in enumerate(T, start=1):
        res += elem * pow_quick(x, n-idx)
        # print(f"{elem} * {x}^{n-idx}")
    return res
        
     
t = [4,5,6,7]
res = evaluate(t, len(t), 3)
print(f"evaluate: {res}")




def evaluate_iterative(T, n, x):
    res = 0
    for elem in T:
        res *= x
        res += elem
    return res
             
t = [4,5,6,7]
res = evaluate_iterative(t, len(t), 3)
print(f"evaluate_iterative: {res}")  


# a = list(range(5000, 0, -1))
# b = len(a)
# c = 2

# print("\n--- times ---")

# t1 = time()
# evaluate_naive(a,b,c)
# print(f"evaluate_naive: {(time() - t1):.3f}")

# t1 = time()
# evaluate(a,b,c)
# print(f"evaluate: {(time() - t1):.3f}")

# t1 = time()
# evaluate_iterative(a,b,c)
# print(f"evaluate_iterative: {(time() - t1):.3f}")


