#Write a program that prompts for a list of numbers as above and at the end points out both
#the maximum and minimum of the numbers and average.

total = 0
count = 0
numbers = []

while True:
    user_input = input("Enter a number or 'done' to finish: ")
    if user_input == 'done':
        break

    try:
        num = int(user_input)
        numbers.append(num)
        total += num
        count += 1
    except ValueError:
        print("Invalid Input")

average = total/count if count > 0 else 0

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", average)