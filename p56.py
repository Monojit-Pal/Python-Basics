#Write pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours

hours = int(input("Enter the number of hours worked: "))
rate = float(input("Enter hourly rate: "))

pay = hours*rate
if hours > 40:
    pay += (hours-40)*rate*0.5

print("Pay:", pay)