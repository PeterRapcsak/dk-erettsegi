with open("forras.txt") as f:
    a = f.read().splitlines()

data = []
for x in range(0, len(a), 5):
    data.append([a[x], a[x+1], a[x+2], int(a[x+3]), int(a[x+4])])

print("2. feladat")
datumvan = sum([1 for d in data if d[0] != "NI"])
print(f"A listában {datumvan} db vetítési dátummal rendelkező epizód van")


print("3. feladat")
látta = sum([1 for d in data if d[4] == 1])
print(f"A listában lévő epizódok {round(látta/len(data)*100, 2)}%-át látta. ")

print("4. feladat")

percek = sum([d[3] for d in data if d[4] == 1])

nap = percek // (24 * 60)
óra = percek % (24 * 60) // 60
perc = percek % 60
print(f"Sorozatnézéssel {nap} napot {óra} órát és {perc} percet töltött. ")

print("5. feladat")
látta = sum([1 for d in data if d[4] == 1])
print(f"A listában lévő epizódok {round(látta/len(data)*100, 2)}%-át látta. ")



