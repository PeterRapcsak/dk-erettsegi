from operator import itemgetter


with open("eloadasok.txt", encoding="UTF-8") as f:
    a = f.read().splitlines()

b = []
for item in a:
    b.append(item.split("\t"))

data = []


for x in b:
    data.append([x[0], int(x[1]), int(x[2]), int(x[3]), int(x[4]), x[5], x[6]])

sorrend = sorted(data, key= itemgetter(2,4))
print(sorrend)