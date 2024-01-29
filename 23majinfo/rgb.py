# kep = [
#        [[], [], [] ... []],
#        [[], [], [] ... []],
#        [[], [], [] ... []],
#        ...
#       ]

kep = []
with open('kep.txt') as forrasfajl:
    for sor in forrasfajl:
        adatsor = sor.strip().split(' ')

        kepsor = []
        keppont = []
        for ertek in adatsor:
            keppont.append(int(ertek))
            if len(keppont) == 3:
                kepsor.append(keppont)
                keppont = []
        kep.append(kepsor)
# print(kep)

print('2. feladat:')
print('Kérem egy képpont adatait!')
sor = int(input('Sor: '))
oszlop = int(input('Oszlop: '))
print(f'A képpont színe RGB({kep[sor-1][oszlop-1][0]}, {kep[sor-1][oszlop-1][1]}, {kep[sor-1][oszlop-1][2]})')

print('3. feladat:')
szamlalo = 0
for kepsor in kep:
    for keppont in kepsor:
        if sum(keppont) > 600:
            szamlalo += 1
print(f'A világos képpontok száma: {szamlalo}')

print('4. feladat:')
legsotetebb_ertek = 255 * 3
legstotebbek = []
for kepsor in kep:
    for keppont in kepsor:
        if sum(keppont) < legsotetebb_ertek:
            legsotetebb_ertek = sum(keppont)
            legstotebbek = []
        if sum(keppont) == legsotetebb_ertek:
            legstotebbek.append(keppont)
print(f'A legsötétebb pont RGB összege: {legsotetebb_ertek}')
print('A legsötétebb pixelek színe:')
for keppont in legstotebbek:
    print(f'RGB({keppont[0]}, {keppont[1]}, {keppont[2]})')

print('5. feladat:')


def hatar(s, elteres):
    for idx in range(len(s)-1):
        if abs(s[idx][2] - s[idx+1][2]) > elteres:
            return True
    return False


print('6. feladat:')
felho_sorok = []
for index, kepsor in enumerate(kep):
    if hatar(kepsor, 10):
        felho_sorok.append(index+1)
print(f'A felhő legfelső sora: {felho_sorok[0]}')
print(f'A felhő legalsó sora: {felho_sorok[-1]}')


















