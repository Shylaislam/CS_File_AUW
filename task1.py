# Part A 
file = open("student info.txt", "w")

file.write("C12\n")
file.write("C23\n")
file.write("C44\n")

file.close()


# Part B
file = open("student info.txt", "a")

file.write("C16\n")
file.write("C13\n")
file.write("C14\n")
file.write("C15\n")

file.close()


# Part C
file = open("student info.txt", "r")

for line in file:
    print(line.rstrip())   

file.close()