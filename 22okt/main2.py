with open("felajanlas.txt") as f:
    a = f.read().split()

hossz = int(a.pop(0))

data = []

for x in range(0, len(a), 3):
    data.append([int(a[x]), int(a[x+1]), a[x+2]])

print("2. Feladat")
print(f"A felajánlások száma: {len(data)}")

print("3. Feladat")

sorszamok = []
for x in range(0, len(data)):
    if data[x][0] > data[x][1]:
        sorszamok.append(x+1)

toprint = ""
for s in sorszamok:
    toprint += str(s) + " "

print(f"A bejárat mindkét oldalán ültetők: {toprint}")

print("4. Feladat")

sorszam = int(input("Adja meg az ágyás sorszámát! "))

szerepel = []

for d in data:
    if d[0] < d[1]: 
        if d[0] <= sorszam <= d[1]:
            szerepel.append(d)
    else: 
        if (d[0] <= sorszam <= hossz) or (0 <= sorszam <= d[1]):
            szerepel.append(d)

print(f"A felajánlók száma: {len(szerepel)}")
print(f"A virágágyás színe, ha csak az első ültet: {szerepel[0][2]}")

toprint = ""
for s in set([s[2] for s in szerepel]):
    toprint += str(s) + " "

print(f"A virágágyás színei: {toprint}")

print("5. Feladat")

foglalt = []

for d in data:
    if d[0] < d[1]:
        for x in range(d[0], d[1]+1):
            foglalt.append(x)
    else: 
        for x in range(d[0], hossz+1):
            foglalt.append(x)

        for x in range(0, d[1]):
            foglalt.append(x)

vanSzabad = False

for x in range(0, hossz+1):
    if x not in foglalt:
        vanSzabad = True

if vanSzabad:
    if len(foglalt) >= hossz:
        print("Átszervezéssel megoldható a beültetés.")
    else:
        print("A beültetés nem oldható meg.")
else: 
    print("Minden ágyás beültetésére van jelentkező.")

szinek = []
count = 1

for x in range(0, hossz+1):
    for d in data:
        if d[0] < d[1]:
            if d[0] <= x <= d[1]:
                szinek.append([d[2], count])
                break
        else:
            if (d[0] <= x <= hossz) or (0 <= x <= d[1]):
                szinek.append([d[2], count])
                break
        count += 1
    count = 1


print(szinek)






