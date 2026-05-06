import pickle

f = open("student.dat", "wb")

for i in range(int(input("Enter number: "))):
    r = int(input("Roll: "))
    n = input("Name: ")
    pickle.dump([r, n], f)

f.close()


f = open("student.dat", "rb")

x = int(input("Search roll: "))
found = 0

try:
    while True:
        d = pickle.load(f)
        if d[0] == x:
            print("Name:", d[1])
            found = 1
            break
except:
    pass

if found == 0:
    print("Not found")

f.close()