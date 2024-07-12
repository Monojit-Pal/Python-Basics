#WAP to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1 > num2:
    if num1 > num3:
        print(num1, "is the greatest")
    else:
        print(num3, "is the greatest")
else:
    if num2 > num3:
        print(num2, "is the greatest")
    else:
        print(num3, "is the greatest")