#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one.
#Use subject name as key & marks as value.

marks = {}

x = int(input("Enter physics marks : "))
marks.update({"phy": x})
x = int(input("Enter mathematics marks : "))
marks.update({"math": x})
x = int(input("Enter chemistry marks : "))
marks.update({"chem": x})

print(marks)