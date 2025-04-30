n = int(input("Enter int number bigger than 0: "))

# a)
for i in range(1, n+1):
    if(i % 3 == 0):
        print(i)
        
# b)
for i in range(1, n+1):
    if i % 10 == 0:
        print(i)
    
# c)
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

# d)
for i in range(1, n+1):
    if i % 5 == 0 or i % 3 == 0:
        print(i)