file = open("students.csv", "r")
 
lines = file.readlines()

for line in lines:  
    i=line.strip().split(",")
    name=i[0]
    sec=i[1]
    age=i[2]

    

    print(f"{name}  is in section {sec} , her age is {age} age")

file.close()