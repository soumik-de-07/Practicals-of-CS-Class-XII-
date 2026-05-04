f1 = open("data.txt", "r")
f2 = open("new.txt", "w")

for line in f1:
    if 'a' and 'A' in line:
        f2.write(line)

f1.close()
f2.close()