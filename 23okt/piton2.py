with open("forras.txt") as f:
    kezdetiadatok = f.read().split()
data = [[int(kezdetiadatok[x]), kezdetiadatok[x+1], int(kezdetiadatok[x+2])] for x in range(0, len(kezdetiadatok), 3)]
print(f"2. feladat:\nA rendelések száma: {len(data)}")
napszam = int(input("Kérem, adjon meg egy napot: "))
rendelesszam = sum([1 for x in data if x[0] == napszam])
print(f"3. feladat:\nA rendelések száma az adott napon: {rendelesszam}")
rendelési_napok = set([d[0] for d in data if d[1] == 'NR'])
if (30 - len(rendelési_napok)) > 0:
    print(f'4. feladat:\n{30 - len(rendelési_napok)} nap nem volt a reklámban nem érintett városból rendelés')
else:
    print('4. feladat:\nMinden nap volt rendelés a reklámban nem érintett városból')
legtobbrendeles = max([d[2] for d in data])
legtobbnap = [d[0] for d in data if d[2] == legtobbrendeles]
print(f"5. feladat:\nA legnagyobb darabszám: {legtobbrendeles}, a rendelés napja: {legtobbnap[0]} ")
def osszes(varos, szam):
    return sum([d[2] for d in data if (d[1] == varos) and (d[0] == szam)])
print(f"7. feladat:\nA rendelt termékek darabszáma a 21. napon PL: {osszes('PL', 21)} TV: {osszes('TV', 21)} NR: {osszes('NR', 21)}\n8. feladat:\nNapok\t1..10\t11..20\t21..30")
tipusok, toprint = ["PL", "TV", "NR"], ["Napok\t1..10\t11..20\t21..30\n"]
for t in tipusok:
    szam10, szam20, szam30 = sum([1 for d in data if (d[1] == t) and (d[0] <= 10)]), sum([1 for d in data if (d[1] == t) and (11 <= d[0] <= 20)]), sum([1 for d in data if (d[1] == t) and (21 <= d[0] <= 30)])
    toprint.append(f"{t}\t{szam10}\t{szam20}\t{szam30}\n")
    print(f"{t}\t{szam10}\t{szam20}\t{szam30}")
with open("kampany.txt", "w") as f:
    f.write("".join(toprint))