#Search for a number x in this tuple using for loop
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter x : "))

idx = 0
for el in nums:
    if el == x:
        print("found at index", idx)
        break
    idx += 1

if idx == len(nums):
    print("not found")