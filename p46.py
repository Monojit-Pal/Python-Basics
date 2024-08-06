#Write a program to convert Celsius to Fahrenheit and vice versa.

C = float(input("Enter temperature in Celsius: "))
F = (C * 9/5) + 32
print("Temperature in Fahrenheit:", round(F, 2))
F = float(input("Enter temperature in Fahrenheit: "))
C = (F - 32) * 5/9
print("Temperature in Celsius:", round(C, 2))