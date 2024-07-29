#Write a recursive function to print all elements in a list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_list(list, idx):
    if idx == len(list):
        return
    print(list[idx], end = " ")
    print_list(list, idx+1)

print_list(list, 0)