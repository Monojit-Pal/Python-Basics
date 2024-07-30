#WAP that replaces all occurrences of "Python" with "Java" in practice.txt file.
#Search if the word "learning" exists in the file or not.

with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("Found")
    else:
        print("Not Found")

new_data = data.replace("Python", "Java")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)