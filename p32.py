#WAF to print the elements of a list in a single line

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(list)