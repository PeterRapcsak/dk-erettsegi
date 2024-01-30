with open("felajanlas.txt") as f:
    adatok = f.read().split()

agyas = adatok[0]
del adatok[0]

data = []

for a in range(0, len(adatok), 3):
    data.append([int(adatok[a]), int(adatok[a+1]), adatok[a+2]])


print("2. feladat")
print(f"A felajánlások száma: {len(data)}")

print("3. feladat")

num = 1
for d in data:
    d.append(num)
    num += 1

feladat2 = sorted([d[3]for d in data if (d[1] - d[0]) < 0])
toprint = ""
for f in feladat2:
    toprint += str(f) + " "

print(f"A bejárat mindkét oldalán ültetők: {toprint}")

print("4. feladat")
sorszam = int(input("Adja meg az ágyás sorszámát! "))

felajanlokszama = sum([1 for d in data if sorszam>=d[0] and sorszam<=d[1]])

print(f"A felajánlók száma: {felajanlokszama}")

szinek = [d[2] for d in data if sorszam>=d[0] and sorszam<=d[1]]

print(f"A virágágyás színe, ha csak az első ültet: {szinek[0]}")

szinek = set(szinek)

toprint = ""
for s in szinek:
    toprint += str(s) + " "

print(f"A virágágyás színei: {toprint}")



print("5. feladat")





print(f"Átszervezéssel megoldható a beültetés. ")
print(f"Minden ágyás beültetésére van jelentkező. ")
print(f"A beültetés nem oldható meg. ")