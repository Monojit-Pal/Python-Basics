#Write a program to prompt the user for principal amount, annual interest, and years.
#Print the interest amount and sum total of principal and interest.

principal = float(input("Enter principal amounnt: "))
rate = float(input("Enter annual interest: "))
years = int(input("Enter years: "))
interest = (principal * rate * years) / 100
print("Interest Amount:", interest)
print("Sum total:", principal + interest)