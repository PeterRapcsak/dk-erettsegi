with open("forras.txt") as f:
    a = f.read().splitlines()

data = []

for x in range(0, len(a), 5): 
    data.append([a[x], a[x+1], a[x+2], int(a[x+3]), int(a[x+4])])


print("2. feladat")
vetitesidatum = sum([1 for d in data if d[0] != "NI"])
print(f"A listában {vetitesidatum} db vetítési dátummal rendelkező epizód van.")


print("3. feladat")
latott = sum([d[4] for d in data])
print(f"A listában lévő epizódok {round(latott / len(data)*100, 2)}%-át látta. ")

print("4. feladat")
nezett = sum([d[3] for d in data])

nap = nezett // (60*60*24)
ora = nezett // (60*60)
perc = nezett % 60

print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött. ")


print("5. feladat")
datum = input("Adjon meg egy dátumot! Dátum= ")
ev = int(datum[0:4])
ho = int(datum[5:7])
nap = int(datum[8:10])

nemlatott = []
for d in data:
    if d[0] != "NI":
        if int(d[0][0:4]) <= ev:
            if int(d[0][5:7]) <= ho:
                if int(d[0][8:10]) <= nap:
                    if d[4] == 0:
                        nemlatott.append(d)

for n in nemlatott:
    print(f"{n[2]}\t{n[1]}")

def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1
    return napok[(ev+ ev//4 - ev//100 + ev//400+honapok[ho-1]+nap)%7]

print("7. feladat")
bekert = input("Adja meg a hét egy napját (például cs)! Nap= ")

vetitesek = set([d[1] for d in data if d[0] != "NI" and hetnapja(int(d[0][0:4]), int(d[0][5:7]), int(d[0][8:10])) == bekert])
for v in vetitesek:
    print(v)

sorozatok = set([d[1] for d in data])

with open("summa.txt", "w") as f:
    for s in sorozatok:

        ido = sum([d[3] for d in data if d[1] == s])
        szam = sum([1 for d in data if d[1] == s])

        f.write(f"{s} {ido} {szam}\n")





