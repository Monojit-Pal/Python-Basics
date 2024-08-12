import math as m

def separate(n):
    i = m.floor(n)
    f = n - i
    return i, f

n = float(input("Enter a floating point number: "))
integer, floating = separate(n)
print("Integer part:", integer, "Floating part:", floating)