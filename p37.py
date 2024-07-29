#Create a new file "practice.txt" using python and add data

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Python.\nI like programming in Python.")

f.close()