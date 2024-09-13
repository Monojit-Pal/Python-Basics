my_list = list(map(int, input("Enter list of numbers: ").split()))
even_list = [x for x in my_list if x % 2 == 0]
odd_list = [x for x in my_list if x % 2 == 1]
print("Even List:", even_list)
print("Odd List: ", odd_list)