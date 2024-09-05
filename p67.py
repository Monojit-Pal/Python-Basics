#Check for palindrome string
s = input("Enter a string: ")
check = True
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        check = False

if check:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")