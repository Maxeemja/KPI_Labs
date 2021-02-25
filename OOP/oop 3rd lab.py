#відсортувати слова за зростанням кількості голосних у них
Dict = ["а", "е", "є", "и", "і", "ї", "о", "у", "ю", "я"] #усі голосні літери
txt = input().replace(".", " ").replace(",", " ").replace("?", " ").replace("!", " ").split(" ")

pre = {} #словник
for i in txt:
    w = list(i.lower()) #розбиваю слова на символи
    counter = 0
    for j in w: #перебір слів посимвольно
        if j in Dict:
            counter += 1
    pre[i] = counter
final = []

sorted_x = sorted(pre.items(), key=lambda v: v[1])# сортування за значеннями(к-ть голосних)
# sorted_x - список , який складається з кортежів (слово, к-ть голосних) , відсортований за другим елементом
for j in sorted_x:
    final.append(j[0]) #переношу слова(перші значення кортежів) у фінальний список
print(*final)
