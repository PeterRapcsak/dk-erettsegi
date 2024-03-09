from operator import itemgetter


with open("eloadasok.txt") as f:
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

kezdes = 480
for n in napok:
    idotartam = sum([d[4]+20 for d in data if d[2] == n])
    vegzes = kezdes + idotartam
    
    if vegzes > 720:
        vegzes += 60

    ora = vegzes//60
    perc = vegzes%60
    if perc < 10:
        perc = "0"+str(perc)
    print(f"november {n}.: {ora}:{perc}")

hetedike = [s for s in sorrend if s[2] == 7]
for h in hetedike:
    kezdes += h[4] + 20
    if kezdes >= 720:
        break

ora = kezdes//60
perc = kezdes%60
if perc < 10:
    perc = "0"+str(perc)
print(f"A harmadik napon az ebédszünet {ora}:{perc}-kor kezdődik")




