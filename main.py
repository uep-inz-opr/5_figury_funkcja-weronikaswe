import string
import math


def pole(dane_figury):
    if len(dane_figury) == 1:
        kolo = math.pi*math.pow(float(dane_figury[0]),2)
        return kolo
    elif len(dane_figury) == 2:
        prostokat = float(dane_figury[0])*float(dane_figury[1])
        return prostokat
    elif len(dane_figury) == 3:
        p = (float(dane_figury[0])+float(dane_figury[1])+float(dane_figury[2]))/2
        trojkat = math.sqrt(p*(p-float(dane_figury[0]))*(float(dane_figury[1])*float(dane_figury[2])))
        return trojkat
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
        quit()


liczba_figur = input()

sumka = 0

for i in range(int(liczba_figur)):
  dane_figury = input()
  dane_figury = dane_figury.split(' ')
  sumka += pole(dane_figury)

print(round(sumka, 2))


