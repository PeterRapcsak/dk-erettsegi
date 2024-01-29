with open("melyseg.txt") as f:
    data = f.read().splitlines()

print("1. feladat ")
print(f"A fájl adatainak száma: {len(data)}")

print("2. feladat ")
szam = int(input("Adjon meg egy távolságértéket! ")) - 1
print(f"Ezen a helyen a felszín {data[szam]} méter mélyen van.")

print("3. feladat ")
nullak = sum([1 for d in data if int(d) == 0])
szazalek = nullak / len(data) *100
print(f"Az érintetlen terület aránya {round(szazalek, 2)}%. ")

godrok = []
for d in data:
    if int(d) == 0:
        godrok.append("\n")
    else:
        godrok.append(d + " ")

with open("godrok.txt", "w") as f2:
    f2.writelines(godrok)

print("5. feladat ")

with open("godrok.txt") as f3:
    godor = f3.read().splitlines()


print(f"A gödrök száma: {len(godor)} ")

print("6. feladat ")

print("a)")
if data[szam] == 0:
    print(f"Az adott helyen nincs gödör")
else: 
    kezd = 0
    veg = 0


    print(f"A gödör kezdete: {kezd} méter, a gödör vége: {veg} méter. ")
