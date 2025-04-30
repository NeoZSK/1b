import math


n = int(input("Get n value (n >= 1): "))
k = int(input("Get k value (n >= k >= 1): "))

res = math.factorial(n) / (math.factorial(n - k) * math.factorial(k))
print("Result: ", int(res))


