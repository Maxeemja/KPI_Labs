import locale
import sys
import pickle
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Window_1 import Ui_MainWindow
from Window_2 import Ui_Window2
from Window_3 import Ui_Window3
from Window_4 import Ui_Window4

# Налаштування локалей для нормального сортування українських імен

locale.setlocale(locale.LC_ALL, "uk_UA.UTF-8")




class Lab2(QMainWindow, Ui_MainWindow):
    def __init__(self):

        # Перше вікно

        super(Lab2, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.var()

        # Win1 кнопки:

        self.ui.buttonCall2.clicked.connect(self.win2show)
        self.ui.buttonCall3.clicked.connect(self.win3show)
        self.ui.buttonCall4.clicked.connect(self.win4show)

        # 2-ге вікно:

        self.win2 = QMainWindow()
        self.win2.ui = Ui_Window2()
        self.win2.ui.setupUi(self.win2)
        self.win2.setMale = {"Іван", "Петро", "Остап", "Максим", "Олександр", "Богдан", "Свят", "Стас", "Дмитро", "Влад", "Олег", "Олексій", "Матвій", "Євген", "Єгор"}
        self.win2.setFemale = {"Ірина", "Марія", "Діана", "Анастасія", "Іванна", "Богдана", "Влада", "Вікторія", "Анна", "Христина", "Софія", "Оксана", "Наталя", "Олена", "Зоя"}
        self.fill_listbox(self.win2.setMale, self.win2.ui.listboxMale, self.win2.ui.browserAction)
        self.fill_listbox(self.win2.setFemale, self.win2.ui.listboxFemale, self.win2.ui.browserAction)
        self.win2.setA = set()
        self.win2.setB = set()

        # Win2 кнопки:

        self.win2.ui.buttonSaveMale.clicked.connect(self.add_male)
        self.win2.ui.buttonSaveFemale.clicked.connect(self.add_female)
        self.win2.ui.buttonSaveA.clicked.connect(self.save_a)
        self.win2.ui.buttonReadA.clicked.connect(self.read_a)
        self.win2.ui.buttonClearA.clicked.connect(self.clear_a)
        self.win2.ui.buttonSaveB.clicked.connect(self.save_b)
        self.win2.ui.buttonReadB.clicked.connect(self.read_b)
        self.win2.ui.buttonClearB.clicked.connect(self.clear_b)

        # 3-тє вікно

        self.win3 = QMainWindow()
        self.win3.ui = Ui_Window3()
        self.win3.ui.setupUi(self.win3)
        self.win3.relationS = set()
        self.win3.relationR = set()

        # Win3 кнопки

        self.win3.ui.buttonFillSetA.clicked.connect(self.fill_listbox_a)
        self.win3.ui.buttonFillSetB.clicked.connect(self.fill_listbox_b)
        self.win3.ui.buttonGetRelationS.clicked.connect(self.form_relation_s)
        self.win3.ui.buttonGetRelationR.clicked.connect(self.form_relation_r)

        # 4-те вікно

        self.win4 = QMainWindow()
        self.win4.ui = Ui_Window4()
        self.win4.ui.setupUi(self.win4)

        # Win4 кнопки

        self.win4.ui.buttonGetIntersectionRS.clicked.connect(self.get_intersection_r_s)
        self.win4.ui.buttonGetUnionRS.clicked.connect(self.get_union_r_s)
        self.win4.ui.buttonGetDifferenceRS.clicked.connect(self.get_difference_r_s)
        self.win4.ui.buttonGetDifferenceUR.clicked.connect(self.get_difference_u_r)
        self.win4.ui.buttonGetReverseS.clicked.connect(self.get_reversed_s)

    # Функції показу побічних вікон:

    def win2show(self):
        self.win2.show()
        self.ui.browserAction.append("-Відкрито вікно №2")

    def win3show(self):
        self.win3.show()
        self.ui.browserAction.append("-Відкрито вікно №3")

    def win4show(self):
        self.win4.show()
        self.ui.browserAction.append("-Відкрито вікно №4")

    # Функція для визначення варіанту:

    def var(self):
        G = 2
        N = 10
        M = "ІО"
        self.ui.labelInfo2.setText("Моя група: {0}-0{1}".format(M, G))
        self.ui.labelInfo3.setText("Мій номер у групі: {0}".format(N))
        if M == "ІО": N += 1
        self.ui.labelVarGet.setText("Мій варіант: {0}".format((N + G % 60) % 30 + 1))

    # функції для операцій над R та S

    def get_intersection_r_s(self):
        self.win4.intersection_r_s = self.win3.relationR & self.win3.relationS
        self.fill_table(self.win4.ui.tableIntersectionRS, self.win4.intersection_r_s)
        self.win4.ui.browserAction.append("-Сформовано матрицю результата операції перетину R та S")

    def get_union_r_s(self):
        self.win4.union_r_s = self.win3.relationR | self.win3.relationS
        self.fill_table(self.win4.ui.tableUnionRS, self.win4.union_r_s)
        self.win4.ui.browserAction.append("-Сформовано матрицю результата операції об'єднання R та S")

    def get_difference_r_s(self):
        self.win4.difference_r_s = self.win3.relationR - self.win3.relationS
        self.fill_table(self.win4.ui.tableDifferenceRS, self.win4.difference_r_s)
        self.win4.ui.browserAction.append("-Сформовано матрицю результата операції різниці R та S")

    def get_difference_u_r(self):
        self.fill_table(self.win4.ui.tableDifferenceUR, self.win3.relationR, zeros="1", crosses="0")
        self.win4.ui.browserAction.append("-Сформовано матрицю результата операції різниці U та R")

    def get_reversed_s(self):
        self.win4.reversed_s = set([(elem[1], elem[0]) for elem in self.win3.relationS])
        self.fill_table(self.win4.ui.tableReverseS, self.win4.reversed_s, order="reverse")
        self.win4.ui.browserAction.append("-Сформовано матрицю результата операції обернення S")

    # Win3 функції для заповнення лістбоксів

    def fill_listbox_a(self):
        self.win3.ui.listboxSetA.clear()
        self.fill_listbox(self.win2.setA, self.win3.ui.listboxSetA, self.win3.ui.browserAction)
        self.win3.ui.browserAction.append("-Множина А відображена у відповідному лістбоксі")

    def fill_listbox_b(self):
        self.win3.ui.listboxSetB.clear()
        self.fill_listbox(self.win2.setB, self.win3.ui.listboxSetB, self.win3.ui.browserAction)
        self.win3.ui.browserAction.append("-Множина B відображена у відповідному лістбоксі")

    # Win3 функції формування відношень R та S:

    def form_relation_s(self): # Forms relation S and fills the table with it
        if self.win2.setA != set() and self.win2.setB != set():
            self.win3.relationS = set()
            selection_teshcha = list(self.win2.setA)
            selection_man = list(self.win2.setB)
            while selection_teshcha != list():
                teshcha = random.choice(selection_teshcha)
                selection_teshcha.remove(teshcha)
                if teshcha in self.win2.setFemale:
                    chance = 90
                    if teshcha in selection_man: selection_man.remove(teshcha)
                    selection_local_man = list(selection_man)
                    while random.randrange(0, 101) in range(chance+1) and selection_local_man != list():
                        man = random.choice(selection_local_man)
                        if man != teshcha and (man, teshcha) not in self.win3.relationS and man not in self.win2.setFemale:
                            self.win3.relationS.add((teshcha, man))
                            selection_man.remove(man)
                            selection_local_man.remove(man)
                            chance -= 30
                            if man in selection_teshcha:
                                selection_teshcha.remove(man)
                        else:
                            selection_local_man.remove(man)

            self.win3.ui.browserAction.append("-Відношення S сформовано та відображено у вигляді матриці")
            self.fill_table(self.win3.ui.tableRelationS, self.win3.relationS)
        else:
            self.win3.ui.browserAction.append("-Неможливо сформувати відношення, причини: множина А пуста, множина B пуста")

    def form_relation_r(self):  # Forms relation R and fills the table with it
        if self.win2.setA != set() and self.win2.setB != set() and self.win3.relationS != set():
            self.win3.relationR = set()
            selection_wife = list(self.win2.setA)
            selection_husband = list(self.win2.setB)
            while selection_wife != list():
                wife = random.choice(selection_wife)
                selection_wife.remove(wife)
                if wife in self.win2.setFemale:
                    chance = 90
                    selection_local_husband = list(selection_husband)
                    while selection_local_husband != list() and random.randrange(0, 101) in range(chance+1):
                        husband = random.choice(selection_local_husband)
                        if husband != wife and (husband, wife) not in self.win3.relationR and husband in self.win2.setMale\
                                and (husband, wife) not in self.win3.relationS and (wife, husband) not in self.win3.relationS:
                            self.win3.relationR.add((wife, husband))
                            selection_husband.remove(husband)
                            selection_local_husband.remove(husband)
                            chance = 0
                        else:
                            selection_local_husband.remove(husband)
            self.fill_table(self.win3.ui.tableRelationR, self.win3.relationR)
            self.win3.ui.browserAction.append("-Відношення R сформовано та відображено у вигляді матриці")
        else:
            self.win3.ui.browserAction.append("-Неможливо сформувати відношення, причини: множина А пуста, множина B пуста, відношення aSb не сформовано")

    # Win2 Функції додавання чоловічих та жіночих імен до множини A або B, функції для зберігання, зчитування або очищення множин A або B:

    def add_male(self):
        items1 = self.win2.ui.listboxMale.selectedItems()

        if self.win2.ui.radiobuttonMaleA.isChecked():
            self.set_clear(self.win2.setA, self.win2.setMale)
            self.win2.setAMale = set()
            for i in range(len(items1)):
                self.win2.setAMale.add(str(self.win2.ui.listboxMale.selectedItems()[i].text()))
            self.win2.setA.update(self.win2.setAMale)
            self.win2.ui.browserAction.append("-В множину A додано:\n{0}.\nМножина A на даний момент:\n{1}".format(self.win2.setAMale, self.win2.setA))

        if self.win2.ui.radiobuttonMaleB.isChecked():
            self.set_clear(self.win2.setB, self.win2.setMale)
            self.win2.setBMale = set()
            for i in range(len(items1)):
                self.win2.setBMale.add(str(self.win2.ui.listboxMale.selectedItems()[i].text()))
            self.win2.setB.update(self.win2.setBMale)
            self.win2.ui.browserAction.append("-В множину В додано:\n{0}.\nМножина B на даний момент:\n{1}".format(self.win2.setBMale, self.win2.setB))

    def add_female(self):
        items2 = self.win2.ui.listboxFemale.selectedItems()

        if self.win2.ui.radiobuttonFemaleA.isChecked():
            self.set_clear(self.win2.setA, self.win2.setFemale)
            self.win2.setAFemale = set()
            for i in range(len(items2)):
                self.win2.setAFemale.add(str(items2[i].text()))
            self.win2.setA.update(self.win2.setAFemale)
            self.win2.ui.browserAction.append("-В множину A додано:\n{0}.\nМножина A на даний момент:\n{1}".format(self.win2.setAFemale, self.win2.setA))

        if self.win2.ui.radiobuttonFemaleB.isChecked():
            self.set_clear(self.win2.setB, self.win2.setFemale)
            self.win2.setBFemale = set()
            for i in range(len(items2)):
                self.win2.setBFemale.add(str(items2[i].text()))
            self.win2.setB.update(self.win2.setBFemale)
            self.win2.ui.browserAction.append("-В множину В додано:\n{0}.\nМножина B на даний момент:\n{1}".format(self.win2.setBFemale, self.win2.setB))

    def set_clear(self, someset, uniset):
        try:
            for elem in uniset:
                if elem in someset:
                    someset.remove(elem)
        except NameError:
            pass

    def save_a(self):
        with open("setA", "wb") as a:
            pickle.dump(self.win2.setA, a)
        self.win2.ui.browserAction.append("-Множина А збережена в файл")

    def read_a(self):
        try:
            with open("setA", "rb") as a:
                self.win2.setA = pickle.load(a)
            self.win2.ui.browserAction.append("-Множина А, завантажена з файлу:\n{}".format(self.win2.setA))
        except FileNotFoundError:
            self.win2.ui.browserAction.append("-Неможливо завантажити множину з неіснуючого файлу")

    def clear_a(self):
        self.win2.setA.clear()
        with open("setA", "wb") as a:
            setA = set()
            pickle.dump(setA, a)
        self.win2.ui.browserAction.append("-Множина A очищена та зтерта з файлу")

    def save_b(self):
        with open("setB", "wb") as b:
            pickle.dump(self.win2.setB, b)
        self.win2.ui.browserAction.append("-Множина B збережена в файл")

    def read_b(self):
        try:
            with open("setB", "rb") as b:
                self.win2.setB = pickle.load(b)
            self.win2.ui.browserAction.append("-Множина B, завантажена з файлу:\n{}".format(self.win2.setB))
        except FileNotFoundError:
            self.win2.ui.browserAction.append("-Неможливо завантажити множину з неіснуючого файлу")

    def clear_b(self):
        self.win2.setB.clear()
        with open("setB", "wb") as b:
            setB = set()
            pickle.dump(setB, b)
        self.win2.ui.browserAction.append("-Множина B очищена та зтерта з файлу")

    # Функції-заповнювачі

    def fill_listbox(self, someset, somelistbox, report): # Tool function that fills listboxes
        try:
            for elem in someset:
                somelistbox.addItem(elem)
        except NameError:
            report.append("-Множина, якою потрібно заповнити список не знайдена")

    def fill_table(self, table, relation, zeros="0", crosses="X", order="straight"): # Tool function that fills tables with given relations
        if order == "straight":
            listA = sorted(list(self.win2.setA), key=locale.strxfrm)
            listB = sorted(list(self.win2.setB), key=locale.strxfrm)
        elif order == "reverse":
            listA = sorted(list(self.win2.setB), key=locale.strxfrm)
            listB = sorted(list(self.win2.setA), key=locale.strxfrm)
        table.setColumnCount(len(listB))
        table.setRowCount(len(listA))
        table.setHorizontalHeaderLabels(listB)
        table.setVerticalHeaderLabels(listA)
        for i in range(len(listB) + 1):
            for j in range(len(listA) + 1):
                table.setItem(j, i, QTableWidgetItem(zeros))
        print(relation)
        for elem in relation:
            table.setItem(listA.index(elem[0]), listB.index(elem[1]), QTableWidgetItem(crosses))


if __name__ == "__main__":  # Show the window if this file is launched directly, not imported
    app = QApplication(sys.argv)
    lab2 = Lab2()
    lab2.show()
    sys.exit(app.exec())

