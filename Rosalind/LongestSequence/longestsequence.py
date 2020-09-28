f = open("data.txt")
raw = f.readlines()
f.close()
k = raw[0].rstrip()
rest = raw[1:]
s=""
for each in rest:
    s += each.rstrip()

print(s)