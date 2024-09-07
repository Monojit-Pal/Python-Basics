#Reverse a string
s1 = input("Enter a string: ")
s2 = ""
for i in range(1,len(s1)+1):
    s2 += s1[-i]
print(s2)