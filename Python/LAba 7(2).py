with open("C:\\lab7\\Hrytsiuk\\10.txt" , "r") as text:
    s = text.read().replace("\n"," ").replace(","," , ").replace("!"," ! ").replace("?"," ? ").split(".")
    x = ""
    for i in range(len(s) - 1):
        if len(s[i].split()) % 2 != 0 :
            x += (s[i] + "." + "\n")
with open("C:\\lab7\\Hrytsiuk\\101.txt", "w" , encoding="utf-8") as output:  #запис першого файлу
    output.write(x)
with open("C:\\lab7\\Hrytsiuk\\10.txt", "r") as text1:
    s1 = text1.read().replace("\n"," ").replace("."," . ").replace(","," , ").replace("!"," ! ").replace("?"," ? ").split()
    Dict = ["а","е","є","и","і","ї","о","у","ю","я"]    #список усіх голосних
    result = ""
    for j in range(len(s1)):
        counter = 0
        m = list(s1[j])
        for f in range(len(m)):
            if m[f].lower() in Dict:
                counter += 1
        if counter >= 3:
            result += (s1[j] + " ; ")
with open("C:\\lab7\\Hrytsiuk\\102.txt", "w", encoding="utf-8") as output1:    #запис другого файлу
    output1.write(result)



