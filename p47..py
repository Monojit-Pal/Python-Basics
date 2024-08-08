#Write a program to prompt the user for hours and wages per hour and compute gross pay.

hours = int(input("Enter number of hours: "))
wages = float(input("Enter wages per hour: "))
grosspay = round(hours*wages, 2)
print("Gross Pay:", grosspay)