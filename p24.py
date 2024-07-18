#Print the multiplication table of a number n

n = int(input("Enter n : "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1