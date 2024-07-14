#WAP to count the number of students with the "A" grade in the following tuple
# ("C", "D", "A", "A", "B", "B", "A")
#Store the above values in a list & sort them from "A" to "D"

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

list = [*grade]
list.sort()
print(list)