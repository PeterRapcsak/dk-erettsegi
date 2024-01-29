with open("kep.txt") as f:
    adatok = f.read().splitlines()

data = []
adatok2 = []

for a in adatok:
    adatok2.append(a.split())


for a in adatok2:
    sor = []
    for x in range(0, len(a), 3):
        sor.append([a[x], a[x + 1], a[x + 2]])
    data.append(sor)

print(data)

print("2. feladat:")
print("Kérem egy képpont adatait! ")


def hatar(sor, elteres):


elozo = false
for i in range(0, len(data)):
    akt = hatar(i, 10)
    if elozo != akt:
        if akt:
            print(f"elso sora: {i}")
        else:
            print(f"utolso sora: {i}")
            break
    elozo = akt    




hatarok = []
for i in range(0, len(data)):
    hatarok.append(hatar(i, 10))

for h in range(0, len(hatarok)):
    if hatarok[h] == True:
        print(f"elso sora: {h}")
        break

hatarok = sorted(hatarok, reverse=true)

for h in range(0, len(hatarok)):
    if hatarok[h] == True:
        print(f"utolso sora: {339 - h}")
        break



    

    


