with open("dobasok.txt") as f:
    doabsok = f.read().split()


with open("osvenyek.txt") as f:
    osvenyek = f.read().splitlines()

print("2. feladat")
print(f"A dobások száma: {len(doabsok)}")
print(f"Az ösvények száma: {len(osvenyek)}")


print("3. feladat")

leghosszabb = max([len(o) for o in osvenyek])

a = 1

for o in osvenyek:
    if len(o) == leghosszabb:
        leghosszabbSor = a
        break
    a += 1


print(f"Az egyik leghosszabb a(z) {a}. ösvény, hossza: {leghosszabb} ")

print("4. feladat")

sor = int(input("Adja meg egy ösvény sorszámát! ")) - 1
jatekosSzam = int(input("Adja meg a játékosok számát! "))

print("5. feladat")

M = sum([1 for s in osvenyek[sor] if s == "M"])
V = sum([1 for s in osvenyek[sor] if s == "V"])
E = sum([1 for s in osvenyek[sor] if s == "E"])

if M != 0:
    print(f"M: {M} darab ")
if V != 0:
    print(f"V: {V} darab ")
if E != 0:
    print(f"E: {V} darab ")

print("6. feladat")

kulonlegesKarakter = [o for o in osvenyek[sor] if o != "M"]

print(kulonlegesKarakter)


toprint = []

szamlalo = 0
szamindex = 0


for o in osvenyek[sor]:
    if szamindex > len(osvenyek[sor]) - 1:
        break
    if kulonlegesKarakter[szamindex] == o:
        toprint.append(szamlalo)
        szamindex += 1

    szamlalo += 1

print(toprint)



with open("kulonleges.txt") as f:
    f.write()

