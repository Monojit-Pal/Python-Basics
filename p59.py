#Write a program which takes input of a number and check whether if it is positive or negatiive

n = int(input("Enter number: "))
if n > 0:
    print("Number is positive")
elif n < 0:
    print("Number is negative")
else:
    print("Neither positive nor negative")