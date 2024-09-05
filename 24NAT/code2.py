from operator import itemgetter

with open("eloadasok.txt", encoding="UTF8") as f:
    a = f.read().splitlines()

b = []
for item in a:
    b.append(item.split("\t"))

data = []

for x in b:
    data.append([x[0], int(x[1]), int(x[2]), int(x[3]), int(x[4]), x[5], x[6]])

sorrend = sorted(data, key= itemgetter(2,3))

napok = [5,6,7,8]

for n in napok:
    print(f"november {n}.:")
    napi = [s for s in sorrend if s[2] == n]
    for x in napi:
        print(f"{x[3]}. {x[0]}: {x[5]}")

for n in napok:
    idotartam = sum([d[4] for d in data if d[2] == n])
    ora = idotartam//60
    perc = idotartam%60
    print(f"{n-4}. nap: {ora}:{perc}")

leghosszabbeloadas = max([d[4] for d in data if d[2] == 6])
megoldas = [d for d in data if d[4] == leghosszabbeloadas]
for m in megoldas:
    print(f"{m[0]} {m[4]}")


