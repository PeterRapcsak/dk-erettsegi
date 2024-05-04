from datetime import date
from operator import itemgetter

with open("forras.txt") as f:
    a = f.read().split()

data = []

for x in range(0, len(a), 6):
    data.append([int(a[x]), int(a[x+1]), int(a[x+2]), int(a[x+3]), a[x+4], a[x+5]])

print("2. feladat ")
print(f"Az adatsorok száma: {len(data)} ")

print(f"Az először rögzített tábor témája: {data[0][5]}")
print(f"Az utoljára rögzített tábor témája: {data[-1][5]} ")

print("3. feladat ")
zeneitabor = [d for d in data if d[5] == "zenei"]

if zeneitabor: 
    for z in zeneitabor:
        print(f"Zenei tábor kezdődik {z[0]}. hó {z[1]}. napján. ")
else: 
    print("Nem volt zenei tábor.")

print("4. feladat ")
szam = max([len(d[4]) for d in data])
legnepszerubbek = [d for d in data if len(d[4]) == szam]

for l in legnepszerubbek:
    print(f"{l[0]} {l[1]} {l[5]}")

def sorszam(ho, nap):
    d1 = date(2000, ho, nap)
    d2 = date(2000, 6, 16)

    day = d1 - d2

    return day.days

print("6. feladat ")
ho = int(input("Hó: "))
nap = int(input("Nap: "))

def tart(h1, n1, h2, n2, h3, n3):
    d1 = date(2000, h1, n1)
    d2 = date(2000, h2, n2)
    d3 = date(2000, h3, n3)

    if d1 <= d2 <= d3:
        return True

tartotaborok = [d for d in data if tart(d[0], d[1], ho, nap, d[2], d[3])]

print(f"Ekkor éppen {len(tartotaborok)} tábor tart. ")

print("7. feladat ")
nev = input("Adja meg egy tanuló betűjelét: ")
toprint = []

jelentkezett = [d for d in data if nev in d[4]]

var = sorted(jelentkezett, key=itemgetter(0,1))

for v in var:
    toprint.append(f"{v[0]}.{v[1]}-{v[2]}.{v[3]}. {v[5]}\n")

with open("egytanulo.txt ", "w") as f:
    f.writelines(toprint)
