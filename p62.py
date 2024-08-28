#Write a pay program using try and except so that your program handles non-numeric input gradually by printing a message and exiting the program.

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = hours*rate
    print("Pay:", pay)
except ValueError:
    print("Error, please enter numeric input")