with open("forras.txt") as f: 
    adatok = f.read().splitlines()

data = []

sublist = []
for a in adatok:
    if a != "F":
        sublist.append(a)
    else:
        data.append(sublist)
        sublist = []



def counting(string, lista):
    value =  sum([1 for l in lista if l == string])
    return value


def ertek(darabszam):

    pay = 0
    if darabszam >= 1:
        pay += 500
    if darabszam >= 2:
        pay += 450

    if darabszam >= 3:
        pay += (darabszam - 3) * 400
    return pay



print("2. feladat")
print(f"A fizetések száma: {len(data)} ")

print("3. feladat")
print(f"Az első vásárló {len(data[0])} darab árucikket vásárolt. ")

print("4. feladat")

sorszam = int(input("Adja meg egy vásárlás sorszámát! "))
arucikk = input("Adja meg egy árucikk nevét! ")
darabszam = int(input("Adja meg a vásárolt darabszámot! "))

elofordulas = []
count = 0
for d in data:
    count += 1
    if arucikk in d:
        elofordulas.append(count)

print("5. feladat")
print(f"Az első vásárlás sorszáma: {elofordulas[0]}")
print(f"Az utolsó vásárlás sorszáma: {elofordulas[len(elofordulas)-1]}")
print(f"32 vásárlás során vettek belőle. {len(elofordulas)}")

print("6. feladat")


print(f"{darabszam} darab vételekor fizetendő: {ertek(darabszam)}")

print("7. feladat")


for d in set(data[sorszam-1]):
    print(f"{counting(d, data[sorszam-1])} {d}")

valuelist = []

for d in data:
    temp = 0

    for x in set(d):
        if counting(x, d) != 1:
            temp += ertek(counting(x, d))
        else:
            temp += 500
            
    valuelist.append(temp)
        

with open("osszeg.txt", "w") as f:
    for v in valuelist:
        f.write(str(v) + "\n")



