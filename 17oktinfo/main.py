with open('naplo.txt', 'r', encoding='utf-8') as file:
    naplo = file.read().splitlines()

igazolt_hianyzas = 0
igazolatlan_hianyzas = 0
count = 0

for sor in naplo:
    if sor.startswith('#'):
        continue
    for karakter in sor[7:]:
        
        if karakter == 'X':
            igazolt_hianyzas += 1
        elif karakter == 'I':
            igazolatlan_hianyzas += 1

    count += 1

print(f'2. feladat\nA naplóban {count} bejegyzés van.')

print(f'3. feladat\nAz igazolt hiányzások száma {igazolt_hianyzas}, az igazolatlanoké {igazolatlan_hianyzas} óra.')

def hetnapja(honap, nap):
    napnev = ("vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat")
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap-1] + nap) % 7
    return napnev[napsorszam]

# 5. feladat: Kérjen be egy dátumot (hónap, nap), és írassa ki, hogy az a hét melyik napjára esett!
honap = int(input('5. feladat\nA hónap sorszáma='))
nap = int(input('A nap sorszáma='))
nap_neve = hetnapja(honap, nap)
print(f'Azon a napon {nap_neve} volt.')

# 6. feladat: Kérje be a hét egy tanítási napjának nevét és egy aznapi tanítási óra óraszámát
tanitasi_nap_neve = input('6. feladat\nA nap neve=')
oraszam = int(input('Az óra sorszáma='))
hianyzasok = 0

for sor in naplo:
    if sor.startswith('#'):
        continue
    if sor[7 + oraszam - 1] == 'X' or sor[7 + oraszam - 1] == 'I':
        if hetnapja(int(sor[2:4]), int(sor[5:7])) == tanitasi_nap_neve:
            hianyzasok += 1

print(f'Ekkor összesen {hianyzasok} óra hiányzás történt.')

# 7. feladat: Írassa ki a képernyőre a legtöbb órát hiányzó tanuló nevét!
tanulok_hianyzasok = {}
max_hianyzas = 0

for sor in naplo:
    if sor.startswith('#'):
        tanulo_neve = sor[2:]
        tanulok_hianyzasok[tanulo_neve] = sor[7:].count('X') + sor[7:].count('I')
        if tanulok_hianyzasok[tanulo_neve] > max_hianyzas:
            max_hianyzas = tanulok_hianyzasok[tanulo_neve]

legtobb_hianyzas_tanulok = [tanulo for tanulo, hianyzas in tanulok_hianyzasok.items() if hianyzas == max_hianyzas]
legtobb_hianyzas_nevek = ' '.join(legtobb_hianyzas_tanulok)

print(f'7. feladat\nA legtöbb órát hiányzó tanulók: {legtobb_hianyzas_nevek}')
