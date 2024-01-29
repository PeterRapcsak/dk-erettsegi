import datetime
import math

with open("jel.txt") as f:
    lista = f.read().split()

jel = []

for x in range(0, len(lista), 5):
    jel.append([int(lista[x]), int(lista[x+1]), int(lista[x+2]),int(lista[x+3]), int(lista[x+4]),])


print("2. feladat")

sorszam = int(input("Adja meg a jel sorszámát! ")) -1 

print(f"x={jel[sorszam][3]} y={jel[sorszam][4]}")

def eltelt(n1, n2):
    d1 = datetime.timedelta(hours = jel[n1][0], minutes= jel[n1][1], seconds=jel[n1][2])
    d2 = datetime.timedelta(hours = jel[n2][0], minutes= jel[n2][1], seconds=jel[n2][2])

    time = d2 - d1

    return time

print("4. feladat")
print("Időtartam " + str(eltelt(0, len(jel)-1)))


print("5. feladat")

balx = min([x[3] for x in jel])
baly = min([x[4] for x in jel])
jobbx = max([x[3] for x in jel])
jobby = max([x[4] for x in jel])

print(f"Bal alsó: {balx} {baly}, jobb felső: {jobbx} {jobby}")


print("6. feladat")

def elmozdulas(a, b):
    elmozdulasNum = math.sqrt((a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1]))
    return elmozdulasNum

elmozdulasok = [[j[3], j[4]] for j in jel]

osszesites = 0

for e in range(0, len(elmozdulasok)):
    if e == len(elmozdulasok)-1:
        break

    osszesites += elmozdulas(elmozdulasok[e], elmozdulasok[e+1])

print(f"Elmozdulás: {round(osszesites, 3)} egység")