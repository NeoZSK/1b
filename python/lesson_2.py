# --- variables naming --- 
something = None
some_long_name = None
SOME_CONST = None

Never_Ever_Do_This = None # (ugly!)

# in OOP
class SomeClassname:
    _private_variable = None 
# Note: When using acronyms in CapWords, 
# capitalize all the letters of the acronym. 
# Thus HTTPServerError is better than HttpServerError.

# existing:
__embeded_names__= None
__name__ == "__main__" # when is a starting file









# --- importing modules --- 
import math 
import keyword as kw

from keyword import kwlist







# --- keywords --- 
# print(kw.kwlist)
print(kwlist)









# --- Continuation of statements --- 
if (1 == 1) and (1 == 1) and (1 == 1) and (1 == 1) and (1 == 1) and (1 == 1) \
    and (1 == 1) and (2 == 2):
    print("Continuation of statements")
    
    







# --- Python Enhancement Proposals ---
""" PEP8 
https://peps.python.org/pep-0008/

(that's a multiline comment, btw)
"""
    
    







# --- Defining functions ---
def repeat_text(text, times):
    res = text * times
    return res

repeat_text("asdf", 5)









# --- Flow control ---
a = 1
b = 2
if (a == b):
    print("equal")
elif (a > b):
    print("a > b")    
else:
    print("b > a")
    
""" note
`==` VS `is`

Use `==` when comparing values
Use `is` in OOP in specific cases (is THE SAME object?) - sometimes a little tricky
"""









# --- Loops ---
sequence = range(0,5)
print(sequence)
print(list(sequence))

for i in range(1,5):
    print(i)


# iterate over list
some_list = [55, 22, 44, "abs"]
for item in some_list:
    print(f"item: {item}")
    
# index
for idx, item in enumerate(some_list):
    print(f"item at idx {idx}: {item}")










# --- (Not so obvious) Operators ---
x, y = 5, 2

# Division
print (x / y)

# Floor division (dzielenie całkowite)
print (x // y)

# Modulus
print (x % y)

# Exponentiation
print (x ** y)










# --- Basic types ---

# bool     
flag = True

# int      
x = 42

# float    
y = 3.14

# str      
s = "Hello, World!"

# list     
lst = [1, 2, 3, "apple"]

# tuple    
tpl = (10, 20, "banana")
(_, _, b) = tpl
print(b)

# dict     
dct = {"name": "Alice", "age": 25}
print(dct["name"])

# set (unique values)
st = {1, 2, 3, 4, 2}
print(st)











# --- String ---
message1 = 'This is a string in Python'
message2 = "This is also a string"
print(message1)
print(message2)

# zewnętrzny jest silniejszy! 
message = "It's a string"
message = 'It"s a string'
message = 'It\'s also a valid \'string '
print(message1)
print(message2)



# multiline string
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

print(help_message)