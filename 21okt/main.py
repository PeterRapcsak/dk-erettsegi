print("1. feladat")
nehezseg = input("Adja meg a bemeneti fájl nevét! ")
sor = int(input("Adja meg egy sor számát! "))
oszlop = int(input("Adja meg egy oszlop számát! "))

with open(nehezseg) as f:
    a = f.read().split()

jatek = []
for x in range(0, 81, 9):
    jatek.append([int(a[x]), int(a[x+1]), int(a[x+2]), int(a[x+3]), int(a[x+4]), int(a[x+5]), int(a[x+6]), int(a[x+7]), int(a[x+8])])

lepesek = []
for x in range(81, 93, 3):
    lepesek.append([a[x], a[x+1], a[x+2]])

print("3. feladat")
if jatek[sor][oszlop] == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {jatek[sor][oszlop]}")

def resztabla(sor, oszlop):
    return (sor-1)//3 * 3 + (oszlop-1)//3 + 1

def checkcube(num, sl1, sl2):
    return 0

def checkrow(num, sl1, sl2):
    return 0

def checkcolumn(num, sl1, sl2):
    return 0





print(f"A hely a(z) {resztabla(sor, oszlop)} résztáblázathoz tartozik.")

print("4. feladat")

nullasok = 0
for j in jatek:
    for x in j:
        if x == 0:
            nullasok += 1
szazalek = nullasok / (81) * 100

print(f"Az üres helyek aránya: {round(szazalek,2)}%")

print("5. feladat")
for l in lepesek:
    print(f"A kiválasztott sor: {l[1]} oszlop: {l[2]} a szám: {l[0]} ")
    
    print(f"")
    print(f"\n")


