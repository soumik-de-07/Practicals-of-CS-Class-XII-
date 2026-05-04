t = open("data.txt", "r").read()

v = c = u = l = 0

for ch in t:
    if ch in "aeiouAEIOU":
        v += 1
    elif " " in ch:
        pass
    else:
        c += 1
    if ch.isupper():
        u += 1
    elif " " in ch:
        pass
    else:
        l += 1

print("Vowels:", v)
print("Consonants:", c)
print("Uppercase:", u)
print("Lowercase:", l)
