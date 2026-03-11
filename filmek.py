a = open("filmek.txt", "r", encoding="utf-8")
adatok = a.readlines()
a.close()
from statistics import mean

dia = []
legregebbi = 2000
ev = 0
volt = False

class diafilmek:
    def __init__(self, cim, ev, kockak, szinese):
        self.cim = cim
        self.ev = ev
        self.kockak = kockak
        self.szinese = szinese

for i in range (len(adatok)):
    db = adatok[i].strip().split(";")
    p = diafilmek(db[0], int(db[1]), int(db[2]), int(db[3]))
    dia.append(p)

for i in range(len(dia)):
    if dia[i].ev < legregebbi:
        legregebbi = dia[i].ev
        ev = i



for i in range(len(dia)):
    atlag = mean([dia[i].kockak for i in range(len(dia))])

print(f"3. feladat: Diafilmek száma: {len(dia)}")
print(f"3.2 feladat: Legrégebbi diafilm címe: {dia[ev].cim}, kiadása: {dia[ev].ev}")
harom = int(input("Kérem adjon meg egy évszámot: "))
for i in range(len(dia)):
    if dia[i].ev == harom:
        volt = True
        break
if volt == True:
    print(f"{harom} évben megjelent diafilmek: ")
    for i in range(len(dia)):
        if dia[i].ev == harom:
            print(dia[i].cim)
else:
    print("3.3 feladat: Nincs ilyen évszámú diafilm.")

print("3.4 feladat: Diafilmek átlagos kockaszáma: ", round(atlag, 2))

