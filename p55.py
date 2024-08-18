#Write a program which takes two integers as input. Print whether the two numbers are equal, less than, or greater than the other.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Numbers are equal")
elif a > b:
    print(a, "is greater than", b)
else:
    print(a, "is less than", b)