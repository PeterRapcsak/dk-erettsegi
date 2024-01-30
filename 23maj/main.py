from datetime import date
from operator import itemgetter

with open("forras.txt") as f:
    a = f.read().split()

data = []
for x in range(0, len(a), 6):
    data.append([int(a[x]), int(a[x+1]), int(a[x+2]), int(a[x+3]), a[x+4], a[x+5]])

print("2. feladat")
print(f"Az adatsorok száma: {len(data)}")

print(f"Az először rögzített tábor témája: {data[0][5]}\nAz utoljára rögzített tábor témája: {data[len(data)-1][5]}")

print("3. feladat")
zeneitabor = [[d[0], d[1]] for d in data if d[5] == "zenei"]
if not zeneitabor:
    print("Nem volt zenei tábor.")
else:
    for z in zeneitabor:
        print(f"Zenei tábor kezdődik {z[0]}. hó {z[1]}. napján.")

print("4. feladat\nLegnépszerűbbek:")

nepszeru = max([len(d[4]) for d in data])

for d in data:
    if len(d[4]) == nepszeru:
        print(f"{d[0]} {d[1]} {d[5]}")
    
def sorszam(honap, nap):
    d1 = date(2000, 6, 16)
    d2 = date(2000, honap, nap)
    return int(str(d2-d1)[0:2])

def tart(h1, n1, h2, n2, h3, n3):
    d1 = date(2000, h1, n1)
    d2 = date(2000, h2, n2)
    d3 = date(2000, h3, n3)

    if d1 <= d2 <= d3:
        return True

print('6. feladat')
ho = int(input('Hó: '))
nap = int(input('Nap: '))

napok = sum([1 for d in data if tart(d[0], d[1], ho, nap, d[2], d[3])])

print(f"Ekkor éppen {napok} tábor tart. ")

print('7. feladat')
diak = input("Adja meg egy tanuló betűjelét: ")
ment = [d for d in data if diak in d[4]]
ment = sorted(ment, key=itemgetter(0,1))

with open("egytanulo.txt", "w") as f:
    for m in ment:
        f.write(f"{m[0]}.{m[1]}-{m[2]}.{m[3]}. {m[5]}\n")

if len(ment) == len(data):
    print('Elmehet mindegyik táborba. ')
else: 
    print('Nem mehet el mindegyik táborba. ')











