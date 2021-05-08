import sys
import random as rn
import networkx as nx
import matplotlib.pyplot as plt
import copy
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Window_1 import Ui_MainWindow
from Window_2 import Ui_Window2

class Lab4(QMainWindow, Ui_MainWindow):
    def __init__(self):

        # Main window

        super(Lab4, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonCall2.clicked.connect(self.win2show)
        self.ui.buttonCall3.clicked.connect(self.showgraph)
        self.ui.buttonCall4.clicked.connect(self.colorgraph)

        # Second(Matrix) window

        self.win2 = QMainWindow()
        self.win2.ui = Ui_Window2()
        self.win2.ui.setupUi(self.win2)
        self.win2.nodes = []
        self.win2.tupedges = []
        self.win2.nodedges = dict()
        self.win2.ui.buttonSetEdgeCount.clicked.connect(self.setedges)
        self.win2.ui.buttonSetNodeCount.clicked.connect(self.setnodes)
        self.win2.ui.buttonGenerateMatrix.clicked.connect(self.setmanualmatrix)

    def win2show(self):
        self.win2.show()
        self.ui.browserAction.append("-Відображено вікно задання матриці суміжності")

    def setnodes(self):
        try:
            self.win2.nodes = [node for node in range(1, int(self.win2.ui.lineNodeCount.text())+1)]
            if self.win2.nodes == []:
                int("s")
            print(self.win2.nodes)
            self.win2.ui.tableMatrix.setColumnCount(len(self.win2.nodes))
            self.win2.ui.tableMatrix.setRowCount(len(self.win2.nodes))
            self.win2.nodesstr = [str(node) for node in self.win2.nodes]
            self.win2.ui.tableMatrix.setHorizontalHeaderLabels(self.win2.nodesstr)
            self.win2.ui.tableMatrix.setVerticalHeaderLabels(self.win2.nodesstr)
            for elem1 in self.win2.nodes:
                for elem2 in self.win2.nodes:
                    self.win2.ui.tableMatrix.setItem(elem1-1, elem2-1, QTableWidgetItem("0"))
            self.ui.browserAction.append("-Кількість вершин задана")
        except ValueError:
            self.ui.browserAction.append("-Необхідно ввести натуральне число")

    def setedges(self):
        # Перевірки:
        if self.win2.nodes == []:
            self.ui.browserAction.append("-Спершу задайте кількість вершин")
            return
        try:
            self.win2.edgescount = int(self.win2.ui.lineEdgeCount.text())
        except TypeError:
            self.ui.browserAction.append("-Необхідно ввести натуральне число")
            return
        self.win2.dekart = set()
        fac = 1
        factwo = 1
        facthree = 1
        for i in range(1, len(self.win2.nodes)+1):
            fac *= i
        print(fac)
        for i in range(1, 3):
            factwo *= i
        for i in range(1, len(self.win2.nodes)-1):
            facthree *= i
        if self.win2.edgescount > fac/(factwo*facthree):
            self.ui.browserAction.append("-Забагато ребер для такої кількості вершин")
            return
        # Основна частина функції:
        self.win2.dekart = set()
        for elem1 in self.win2.nodes:
            for elem2 in self.win2.nodes:
                if not elem1 == elem2 and (elem2, elem1) not in self.win2.dekart:
                    self.win2.dekart.add((elem1, elem2))
                self.win2.ui.tableMatrix.setItem(elem1, elem2, QTableWidgetItem("0"))
        print(self.win2.dekart)
        self.win2.tupedges = list(rn.sample(self.win2.dekart, self.win2.edgescount))
        print(self.win2.tupedges)
        self.win2.nodedges = dict()
        for elem in self.win2.nodes:
            elemlist = list()
            for edge in self.win2.tupedges:
                if elem == edge[0]:
                    elemlist.append(edge[1])
                if elem == edge[1]:
                    elemlist.append(edge[0])
            self.win2.nodedges.update({elem: elemlist})
        print(self.win2.nodedges)

        for edge in self.win2.tupedges:
            self.win2.ui.tableMatrix.setItem(edge[0]-1, edge[1]-1, QTableWidgetItem(str(1)))
            self.win2.ui.tableMatrix.setItem(edge[1]-1, edge[0]-1, QTableWidgetItem(str(1)))
        self.ui.browserAction.append("-Згенерована матриця з заданою кілкістю ребер")

    def setmanualmatrix(self):
        if self.win2.nodes == []:
            return
        self.win2.tupedges = set()
        self.win2.nodedges = {node: set() for node in self.win2.nodes}
        for mm in range(2):
            for i in self.win2.nodes:
                for j in self.win2.nodes:
                    if self.win2.ui.tableMatrix.item(i-1, j-1).text() != "0" and i != j:
                        if (i,j) not in self.win2.tupedges:
                            self.win2.tupedges.add((j,i))
                        self.win2.nodedges[i].add(j)
                        self.win2.nodedges[j].add(i)
                        self.win2.ui.tableMatrix.setItem(j-1, i-1, QTableWidgetItem("1"))
                    elif i == j:
                        self.win2.ui.tableMatrix.setItem(i-1, j-1, QTableWidgetItem("0"))
        self.win2.tupedges = list(self.win2.tupedges)
        print(self.win2.tupedges)
        for elem in self.win2.nodedges.keys():
            self.win2.nodedges[elem] = list(self.win2.nodedges[elem])
        print(self.win2.nodedges)
        self.ui.browserAction.append("-Матрицю відредаговано")

    def showgraph(self):
        if self.win2.nodes == [] or self.win2.tupedges == []:
            self.ui.browserAction.append("-Матриця не задана")
            return
        plt.figure("Base graph")
        G = nx.Graph()
        G.add_nodes_from(self.win2.nodes)
        G.add_edges_from(self.win2.tupedges)
        nx.draw_shell(G, with_labels=True)
        plt.show()
        self.ui.browserAction.append("-Відображено початковий граф")

    def colorgraph(self):
        if self.win2.nodes == [] or self.win2.tupedges == [] or self.win2.nodedges == dict():
            self.ui.browserAction.append("-Матриця не задана")
            return
        final = {}
        colors = ["orange", "cyan", "lime", "indigo", "yellow", "red", "blue", "green", "pink", "beige"]

        dictpower1 = dict()
        dictpower2 = dict()
        for edge in self.win2.nodedges.keys():
            dictpower1[edge] = len(self.win2.nodedges[edge])
        for edge in dictpower1.keys():
            power = 0
            for elem in self.win2.nodedges[edge]:
                power += dictpower1[elem]
            dictpower2[edge] = [dictpower1[edge], power]
        print(dictpower2)
        sorted_power = sorted(dictpower2.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
        print(sorted_power)
        sorted_list = [(elem[0], elem[1][0]) for elem in sorted_power]
        print(sorted_list)
        i = 0

        def delete_color():
            for color in colors:
                if color not in stackcolor:
                    return color
            color = colors[i+1]
            colors.append(color)
            return color

        for elem in sorted_list:
            stackcolor = []
            for elem2 in self.win2.nodedges[elem[0]]:
                if elem2 in final:
                    stackcolor.append(final[elem2])
            color = delete_color()
            final[elem[0]] = color
        print(final)
        node_colormap = list(final.items())
        print(node_colormap)

        G = nx.Graph()
        G.add_nodes_from(self.win2.nodes)
        G.add_edges_from(self.win2.tupedges)
        nx.draw_shell(G, with_labels=True)
        for elem in node_colormap:
            nx.draw_networkx_nodes(G,  pos=nx.shell_layout(G), nodelist=[elem[0]], node_color=elem[1])
        plt.show()
        self.ui.browserAction.append("-Відображено розфарбований граф")



if __name__ == "__main__":  # Show the window if this file is launched directly, not imported
    app = QApplication(sys.argv)
    lab3 = Lab4()
    lab3.show()
    sys.exit(app.exec())
