#Prints only the initials of your name
name = input("Enter your name: ")
parts = name.split()
for n in parts:
    print(n[0].upper(),end="")