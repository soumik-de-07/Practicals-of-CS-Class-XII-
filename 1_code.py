f = open("data.txt", "r")
for w in f.read().split():
    print(w, end = "#")
f.close()