#Frequency of all characters in a string
s = input("Enter a string: ")
checked = ""

for ch in s:
    if ch not in checked:
        frequency = s.count(ch)
        print(f"{ch} : {frequency}")
        checked += ch