# Create a list of strngs. Write a python which creates another list from the list
# taking the first character from each word.

words = list(input("Enter a list of words: ").split())
new_list = [x[0] for x in words]
print(new_list)