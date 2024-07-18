#Search for a number x in this tuple using loop
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter x : "))

p = -1
idx = 0
while idx < len(nums):
    if nums[idx] == x:
        p = idx
        break
    idx += 1

if p == -1:
    print("Not found")
else:
    print("found at position", p)