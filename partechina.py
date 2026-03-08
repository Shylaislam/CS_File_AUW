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


#Task 2
#A
import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["student_name", "section", "age"])
    writer.writerow(["Ariha", 2, 15])
    writer.writerow(["Sara", 1, 16])
    writer.writerow(["Lima", 3, 15])

print("students.csv file created and data added successfully.")



import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["student_name"]
        section = row["section"]
        age = row["age"]

        print(f"{name} is in section {section}, her age is {age}")