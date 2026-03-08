# Task 1
# A
file = open("student_info.txt", "w")
file.write("C12\n")
file.write("C23\n")
file.write("C44\n")
file.close()

# B
file = open("student_info.txt", "a")
file.write("C55\n")
file.write("C66\n")
file.write("C77\n")
file.write("C88\n")
file.close()

# C
file = open("student_info.txt", "r")



for line in file:
    print(line.strip()) 

file.close()


#task 2
file = open("students.csv", "r")

lines = file.readlines()

for line in lines:  
    i=line.strip().split(",")
    name=i[0]
    sec=i[1]
    age=i[2]

    

    print(f"{name}  is in section {sec} , her age is {age} age")

file.close()
