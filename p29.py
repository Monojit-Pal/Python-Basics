#WAP to find the sum of first n numbers using while

n = int(input("Enter n : "))
idx, sum = 0, 0
while idx <= n:
    sum += idx
    idx += 1
print("Sum :", sum)