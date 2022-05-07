import string
import math


def pole(dane_figury):
    if len(dane_figury) == 1:
        kolo = math.pi*math.pow((dane_figury[0]),2)
        return kolo
    elif len(dane_figury) == 2:
        prostokat = (dane_figury[0])*(dane_figury[1])
        return prostokat
    elif len(dane_figury) == 3:
        p = ((dane_figury[0])+(dane_figury[1])+(dane_figury[2]))/2
        trojkat = math.sqrt(p*(p-(dane_figury[0]))*(p-(dane_figury[1])*(p-(dane_figury[2]))))
        return trojkat
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
        quit()


liczba_figur = input()

sumka = 0

for i in range(int(liczba_figur)):
  dane_figury = input()
  dane_figury = dane_figury.split(' ')
  dane_float = [float(x) for x in dane_figury]
  sumka += pole(dane_float)

print(round(sumka, 2))


