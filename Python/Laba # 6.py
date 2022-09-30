X = input("Введіть назву області чи міста: ").capitalize()
class KyivRegion:
    name = "Київська область"
    population = 1781040
    sqarea = 28120
    popdensity = round(population / sqarea,1)
    maincities = ["Київ", "Бровари", "Бориспіль"]
    def infoRegion(): # завів функцію , яка буде роздруковувати дані по області
       return  print(str(KyivRegion.sqarea) + " км2", str(KyivRegion.population) + " чоловік",
              str(KyivRegion.popdensity) + " чоловік/км2", "Найбільші міста: ", *KyivRegion.maincities, sep="\n")
class LvivRegion:
    name = "Львівська область"
    population = 2512084
    sqarea = 21831
    popdensity = round(population / sqarea,1)
    maincities = ["Львів", "Дрогобич", "Червоноград"]
    def infoRegion():
       return  print(str(LvivRegion.sqarea) + " км2", str(LvivRegion.population) + " чоловік",
              str(LvivRegion.popdensity) + " чоловік/км2", "Найбільші міста: ", *LvivRegion.maincities, sep="\n")
class OdessaRegion:
    name = "Одеська область"
    population = 2377230
    sqarea = 33314
    popdensity = round(population / sqarea,1)
    maincities = ["Одеса", "Білгород-Дністровський", "Чорноморськ"]
    def infoRegion():
       return  print(str(OdessaRegion.sqarea) + " км2", str(OdessaRegion.population) + " чоловік",
              str(OdessaRegion.popdensity) + " чоловік/км2", "Найбільші міста: ", *OdessaRegion.maincities, sep="\n")
popdensityRate = [(KyivRegion.name,KyivRegion.popdensity),(LvivRegion.name,LvivRegion.popdensity),(OdessaRegion.name,OdessaRegion.popdensity)] #cтворив додатковий список для назв областей та густоти населення
popdensityRate.sort(key=lambda i : i[1],reverse= True) #відсортував за 2-им значенням (густотою)
if X == KyivRegion.name: KyivRegion.infoRegion()
elif X in KyivRegion.maincities: print(KyivRegion.name)
elif X == LvivRegion.name: LvivRegion.infoRegion()
elif X in LvivRegion.maincities: print(LvivRegion.name)
elif X == OdessaRegion.name: OdessaRegion.infoRegion()
elif X in OdessaRegion.maincities: print(OdessaRegion.name)
elif X == "Список областей":
    for i in popdensityRate:
        print(i[0], ':', i[1], " чоловік/км2")#красиво вивів список областей

else:
    print("Такої області/такого міста не знайдено :(")