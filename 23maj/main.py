from datetime import date

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

    return str(d2-d1)[0:2]

