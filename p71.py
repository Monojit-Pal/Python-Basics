# Write a program that prompts the user to enter a string and returns in alphabetical order,
# a letter and its frequency of occurrence in the string.

l = list(input("Enter a string: ").lower())
l.sort()
s = "".join(l)
checked = ""
for ch in s:
    if ch not in checked:
        print(ch, ":", s.count(ch))
        checked += ch
