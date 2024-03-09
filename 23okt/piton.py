with open("forras.txt") as f:
    kezdetiadatok = f.read().split()

data = []
for x in range(0, len(kezdetiadatok), 3):
    data.append([int(kezdetiadatok[x]), kezdetiadatok[x+1], int(kezdetiadatok[x+2])])

print("2. feladat: ")
print(f"A rendelések száma: {len(data)}")

print("3. feladat: ")
napszam = int(input("Kérem, adjon meg egy napot: "))
rendelesszam = sum([1 for x in data if x[0] == napszam])
print(f"A rendelések száma az adott napon: {rendelesszam}")

print("4. feladat: ")
rendelési_napok = set([d[0] for d in data if d[1] == 'NR'])
hianyzo_napok = 30 - len(rendelési_napok)

if hianyzo_napok:
    print(f'{hianyzo_napok} nap nem volt a reklámban nem érintett városból rendelés')
else:
    print('Minden nap volt rendelés a reklámban nem érintett városból')

print("5. feladat: ")
legtobbrendeles = max([d[2] for d in data])
legtobbnap = [d[0] for d in data if d[2] == legtobbrendeles]
print(f"A legnagyobb darabszám: {legtobbrendeles}, a rendelés napja: {legtobbnap[0]} ")

def osszes(varos, szam):
    return sum([d[2] for d in data if (d[1] == varos) and (d[0] == szam)])

print("7. feladat: ")
pl = osszes("PL", 21)
tv = osszes("TV", 21)
nr = osszes("NR", 21)
print(f"A rendelt termékek darabszáma a 21. napon PL: {pl} TV: {tv} NR: {nr}")

print("8. feladat: ")
print("Napok\t1..10\t11..20\t21..30")
tipusok = ["PL", "TV", "NR"]
toprint = ["Napok\t1..10\t11..20\t21..30\n"]
for t in tipusok:
    szam10 = sum([1 for d in data if (d[1] == t) and (d[0] <= 10)])
    szam20 = sum([1 for d in data if (d[1] == t) and (11 <= d[0] <= 20)])
    szam30 = sum([1 for d in data if (d[1] == t) and (21 <= d[0] <= 30)])

    toprint.append(f"{t}\t{szam10}\t{szam20}\t{szam30}\n")
    print(f"{t}\t{szam10}\t{szam20}\t{szam30}")

with open("kampany.txt", "w") as f:
    for t in toprint:
        f.write(t)