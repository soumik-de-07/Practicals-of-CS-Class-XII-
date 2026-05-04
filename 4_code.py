import pickle

file = open("student.dat", "wb")

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))

    data = [roll, name]   

    pickle.dump(data, file)

file.close()

import pickle

file = open("student.dat", "rb")

found = False
search_roll = int(input("Enter roll number to search: "))

try:
    while True:
        data = pickle.load(file)

        if data[0] == search_roll:
            print("Name:", data[1])
            found = True
            break

except EOFError:
    pass

if not found:
    print("Record not found")

file.close()