#Write a program which repeatedly reads numbers until  the user enters "done". Once "done" is enetered, print out the total,
#countand average of the numbers. If the user enters anything other than a number, detect their mistake using try and except
#and print an error message and skip to the next number.

total = 0
count = 0

while True:
    user_input = input("Enter a number or 'done' to finish: ")
    if user_input == 'done':
        break

    try:
        num = int(user_input)
        total += num
        count += 1
    except ValueError:
        print("Invalid Input")

average = total/count if count > 0 else 0

print("Total:", total)
print("Count:", count)
print("Average:", average)