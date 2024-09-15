# Write a program that passes a list to a function that squares each element in the list.
# Print the list values at different stages to show the changes made to one list is
# automatically reflected in the other list.

def square_elements(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

numbers = list(map(int, input("Enter list of numbers: ").split()))
print(numbers)
square_elements(numbers)
print(numbers)