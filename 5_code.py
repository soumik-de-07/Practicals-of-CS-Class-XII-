import pickle

# create file
f = open("student.dat", "wb")
for i in range(int(input("Enter number: "))):
    r = int(input("Roll: "))
    n = input("Name: ")
    m = int(input("Marks: "))
    pickle.dump([r, n, m], f)
f.close()

# update record
f = open("student.dat", "rb")
rec = []
x = int(input("Enter roll to update: "))
found = 0

try:
    while True:
        d = pickle.load(f)
        if d[0] == x:
            d[2] = int(input("New marks: "))
            found = 1
        rec.append(d)
except:
    pass

f.close()

# rewrite file
f = open("student.dat", "wb")
for i in rec:
    pickle.dump(i, f)
f.close()

if found:
    print("Updated")
else:
    print("Not found")