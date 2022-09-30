countries = {"Україна": (603548,42000000), "Німеччина": (357578, 83000000), "Італія": (301000,57000000), "Австралія": (7688287,25250000), "США": (9826675,325720000)}
a = countries.values()
a = list(a)
d = list(countries.items())
print(d)
for i in range(len(d)):
    d[i] = list(d[i])
for i in range(len(a)):
    for j in range(1):
        s = round(a[i][j+1] / a[i][j], 1)
        count = s
        d[i][1] = count
d.sort(key=lambda i : i[1])
for i in d:
    print(i[0], ':', i[1] ," human/km2")


