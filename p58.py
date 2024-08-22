#Write a program which takes temperature as input and also input its type. Convert it to the other format.

T = float(input("Enter temperature: "))
ch = int(input("Enter 1 if temperature is in Celsius or 2 if in Fahrenheit: "))

if ch == 1:
    F = (9/5)*T +32
    print("Temperature in Fahrenheit:", F)
elif ch == 2:
    C = (5/9)*(T-32)
    print("Temperature in Celsius:", C)
else:
    print("Invalid type")