import random
import math

#1. feladat:
# Nézzük meg a lottószámok átlagát.
def atlagolas(szam:int):
    print("1. feladat")
    osszeg:int=0
    atlag:int=0
    for i in range(0, len(szam), 1):
            osszeg += szam[i]
            atlag += 1

    return osszeg / atlag

#2. feladat:
# Hány 50-nél nagyobb szám van közte? 
def nagyobb(szam:int):
        print("2. feladat")
        nagyobb:int=0
        for i in range(0, len(szam), 1):
                if szam[i] >= 50:
                       nagyobb += 1

        return nagyobb

#3. feladat:
# Melyik a legnagyobb szám? 
def max(szam:int):
        print("3. feladat")
        max:int=szam[0]
        for i in range(0, len(szam), 1):
                if max < szam[i]:
                       max = szam[i]

        return max

#5. feladat:
# Melyik a legkisebb szám? 
def min(szam:int):
        print("5. feladat")
        min:int=szam[0]
        for i in range(0, len(szam), 1):
                if min > szam[i]:
                       min = szam[i]

        return min

#6. feladat:
# A legkisebb és a legnagyobb szám közti különbség? 
def kulombseg(szam:int):
    print("6. feladat")
    max:int = szam[0]
    min:int = szam[0]
    for i in range(0, len(szam), 1):
        if min > szam[i]:
            min = szam[i]
        elif max < szam[i]:
            max = szam[i]

    return max-min   

#4. feladat:
# Hányadiknak generáltuk a a legnagyobb számot? 
def legnagyobbszam(szam:int):
        print("4. feladat")
        legnagyobb:int=szam(max(szam))
        print(f"A legnagyobb szám a {legnagyobb + 1}. pozícióján található.")




