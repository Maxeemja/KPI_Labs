import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
)
from mainWindow import Ui_MainWindow
from Win2 import Ui_Window2
from win3 import Ui_Window3


class Laba2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # головне вікно
        super(Laba2, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # кнопки першого вікна
        self.ui.pushButton.clicked.connect(self.win2open)
        self.ui.pushButton_3.clicked.connect(self.win3open)
        #  self.ui.pushButton_2.clicked.connect(self.win4open)

        # вікно №2

        self.win2 = QMainWindow()
        self.win2.ui = Ui_Window2()
        self.win2.ui.setupUi(self.win2)
        self.win2.setMale = {"Іван", "Петро", "Остап", "Максим", "Олександр", "Богдан", "Свят", "Стас", "Дмитро",
                             "Влад", "Олег", "Олексій", "Матвій", "Євген", "Єгор"}
        self.win2.setFemale = {"Ірина", "Марія", "Діана", "Анастасія", "Іванна", "Богдана", "Влада", "Вікторія", "Анна",
                               "Христина", "Софія", "Оксана", "Наталя", "Олена", "Зоя"}
        self.fill_listbox(self.win2.setMale, self.win2.ui.listboxMale)
        self.fill_listbox(self.win2.setFemale, self.win2.ui.listboxFemale)
        self.win2.setA = set()
        self.win2.setB = set()

        # Win2 Buttons:

        self.win2.ui.buttonSaveMale.clicked.connect(self.add_male)
        self.win2.ui.buttonSaveFemale.clicked.connect(self.add_female)
        self.win2.ui.buttonSaveA.clicked.connect(self.save_a)
        self.win2.ui.buttonReadA.clicked.connect(self.read_a)
        self.win2.ui.buttonClearA.clicked.connect(self.clear_a)
        self.win2.ui.buttonSaveB.clicked.connect(self.save_b)
        self.win2.ui.buttonReadB.clicked.connect(self.read_b)
        self.win2.ui.buttonClearB.clicked.connect(self.clear_b)

        # Third window

        self.win3 = QMainWindow()
        self.win3.ui = Ui_Window3()
        self.win3.ui.setupUi(self.win3)
        self.win3.relationS = set()
        self.win3.relationR = set()

        # Win3 Buttons

        self.win3.ui.buttonFillSetA.clicked.connect(self.fill_listbox_a)
        self.win3.ui.buttonFillSetB.clicked.connect(self.fill_listbox_b)
        self.win3.ui.buttonGetRelationS.clicked.connect(self.form_relation_s)
        self.win3.ui.buttonGetRelationR.clicked.connect(self.form_relation_r)

        # Fourth window

        self.win4 = QMainWindow()
        #   self.win4.ui = Ui_Window4()
        self.win4.ui.setupUi(self.win4)

        # Win4 Buttons

    #   self.win4.ui.buttonGetUnionRS.clicked.connect(self.get_union_r_s)
    #   self.win4.ui.buttonGetDifferenceRS.clicked.connect(self.get_difference_r_s)
    #   self.win4.ui.buttonGetDifferenceUR.clicked.connect(self.get_difference_u_r)
    #   self.win4.ui.buttonGetReverseS.clicked.connect(self.get_reversed_s)
    def win2open(self):
        self.win2.show()

    def win3open(self):
        self.win3.show()

    # def win4open(self):
    #     self.win4.show()


    def fill_listbox(self, someset, somelistbox):  # Tool function that fills listboxes
        try:
            for elem in someset:
                somelistbox.addItem(elem)
        except NameError:
            print("-Множина, якою потрібно заповнити список не знайдена")

    def fill_table(self, table, relation, zeros="0", ones="1",
                   order="straight"):  # Tool function that fills tables with given relations
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
            table.setItem(listA.index(elem[0]), listB.index(elem[1]), QTableWidgetItem(ones))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = Laba2()
    mainwin.show()
    sys.exit(app.exec())
