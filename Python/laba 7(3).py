import os , pickle , shelve

os.makedirs("C:/lab5/")
list5laba = [('Україна', (603548, 42000000)), ('Німеччина', (357578, 83000000)), ('Італія', (301000, 57000000)), ('Австралія', (7688287, 25250000)), ('США', (9826675, 325720000))]
with open("C:/lab5/lab5.txt", "wb") as lab5:
    pickle.dump(list5laba, lab5)

with open("C:/lab5/lab5.txt", "r") as text:
    s = text.read()
    s += "  Я виконую 7-му лабу"
with open("C:/lab5/lab5(m0dified).txt", "w") as text:
    text.write(s)
#####################################################
os.makedirs("C:/lab6/")
text1 = shelve.open("C:/lab6/lab6.txt")
text1["name"] = "Одеська область"
text1["population"] = "2377230"
text1["sqarea"] = "33314"
text1["popdensity"] = "round(population / sqarea, 1)"
text1["maincities"] = "Одеса, Білгород-Дністровський, Чорноморськ"
text1.close()