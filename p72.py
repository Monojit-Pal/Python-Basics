# Write a program to add two matrices

m1 = []
m2 = []
r = int(input("Enter the no. of rows: "))
c = int(input("Enter the no. of columns: "))
print("Enter the first matrix:")
for i in range(r):
    l = list(map(int, input().split()))
    m1.append(l)
print("Enter the second matrix:")
for i in range(r):
    l = list(map(int, input().split()))
    m2.append(l)
print("First Matrix")
for i in range(r):
    for j in range(c):
        print(m1[i][j], end = "  ")
    print()
print("Second Matrix")
for i in range(r):
    for j in range(c):
        print(m2[i][j], end = "  ")
    print()
print("Sum of the Matrices:")
for i in range(r):
    for j in range(c):
        print(m1[i][j] + m2[i][j], end = "  ")
    print()