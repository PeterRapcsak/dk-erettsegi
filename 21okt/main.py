print("1. feladat")
nehezseg = input("Adja meg a bemeneti fájl nevét! ")
sor = int(input("Adja meg egy sor számát! ")) - 1
oszlop = int(input("Adja meg egy oszlop számát! ")) - 1

with open(nehezseg + ".txt") as f:
    a = f.read().split()

jatek = []
for x in range(0, 81, 9):
    jatek.append([int(a[x]), int(a[x+1]), int(a[x+2]), int(a[x+3]), int(a[x+4]), int(a[x+5]), int(a[x+6]), int(a[x+7]), int(a[x+8])])

lepesek = []
for x in range(81, 93, 3):
    lepesek.append([int(a[x]), int(a[x+1]), int(a[x+2])])

def getnum(r,c):
    return jatek[r][c]

def checkq(r, c):
    rowq = r // 3
    colq = c // 3
    
    subsq = rowq * 3 + colq + 1
    
    return subsq

def getsquare(r, c):
    rs = (r // 3) * 3
    cs = (c // 3) * 3
    
    subgrid = []
    for i in range(rs, rs + 3):
        for j in range(cs, cs + 3):
            subgrid.append(jatek[i][j])
    return subgrid


print("3. feladat")
print(f"Az adott helyen szereplő szám: {getnum(sor, oszlop)}")
print(f"A hely a(z) {checkq(sor, oszlop)} résztáblázathoz tartozik.")

print("4. feladat")
nullak = 0
for j in jatek:
    for x in j:
        if x == 0:
            nullak += 1
print(f"Az üres helyek aránya: {round(nullak / 81 * 100, 1)}% ")

def checkvalid(r,c,v):
    if jatek[r][c] != 0:
        return "A helyet már kitöltötték."
    if v in jatek[r]:
        return "Az adott sorban már szerepel a szám."
    if v in [j[c] for j in jatek]:
        return "Az adott oszlopban már szerepel a szám."
    if v in getsquare(r, c):
        return "Az adott résztáblázatban már szerepel a szám."
    return "A lépés megtehető."

print("5. feladat")
for l in lepesek:
    r = l[2] - 1
    c = l[1] - 1
    v = l[0]
    print(f"A kiválasztott sor: {r} oszlop: {c} a szám: {v} ")
    print(checkvalid(r, c, v))






