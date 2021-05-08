import sys
import random as rn
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Window_1 import Ui_MainWindow
from Window_2 import Ui_Window2

class Lab3(QMainWindow, Ui_MainWindow):
    def __init__(self):

        # Main window

        super(Lab3, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.showSumMatrix.clicked.connect(self.win2show)
        self.ui.showSecondMatrix.clicked.connect(self.showgraph)
        #self.ui.buttonCall4.clicked.connect(self.bellmanford)
        self.ui.showSecondMatrix.clicked.connect(self.showgraph)

        # Second(Matrix) window

        self.win2 = QMainWindow()
        self.win2.ui = Ui_Window2()
        self.win2.ui.setupUi(self.win2)
        self.win2.edges = {}
        self.win2.nodes = []
        self.win2.weightedges = dict()
        self.win2.ui.buttonSetNodeCount.clicked.connect(self.setnodes)
        self.win2.ui.buttonSetEdgeCount.clicked.connect(self.setedges)
        self.win2.ui.buttonGenerateMatrix.clicked.connect(self.setmanualmatrix)

    def win2show(self):
        self.win2.show()

    def setnodes(self):
        try:
            self.win2.nodes = [node for node in range(int(self.win2.ui.lineNodeCount.text()))]
            if self.win2.nodes == []:
                int("s")
            print(self.win2.nodes)
            self.win2.ui.tableMatrix.setColumnCount(len(self.win2.nodes))
            self.win2.ui.tableMatrix.setRowCount(len(self.win2.nodes))
            self.win2.nodesstr = [str(node) for node in self.win2.nodes]
            self.win2.ui.tableMatrix.setHorizontalHeaderLabels(self.win2.nodesstr)
            self.win2.ui.tableMatrix.setVerticalHeaderLabels(self.win2.nodesstr)
            self.win2.dekart = set()
            print(self.win2.dekart)
            for elem1 in self.win2.nodes:
                for elem2 in self.win2.nodes:
                    self.win2.ui.tableMatrix.setItem(elem1, elem2, QTableWidgetItem("0"))
        except ValueError:
            self.win2.ui.lineNodeCount.setText("Натуральне число!")


    def setedges(self):
        if self.win2.nodes == []:
            self.win2.ui.lineEdgeCount.setText("Вершин нема!")
            return
        try:
            self.win2.edgescount = int(self.win2.ui.lineEdgeCount.text())
        except TypeError:
            self.win2.ui.lineEdgeCount.setText("Натуральне число!")
            return
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
            self.win2.ui.lineEdgeCount.setText("Забагато!")
            return
        for elem1 in self.win2.nodes:
            for elem2 in self.win2.nodes:
                if not elem1 == elem2 and (elem2, elem1) not in self.win2.dekart:
                    self.win2.dekart.add((elem1, elem2))
                self.win2.ui.tableMatrix.setItem(elem1, elem2, QTableWidgetItem("0"))
        self.win2.edges = rn.sample(self.win2.dekart, self.win2.edgescount)
        print(self.win2.edges)
        '''self.win2.weightedges = dict()
        for edge in self.win2.edges:
            weight = rn.randrange(1, 10)
            self.win2.weightedges.update({(edge[0], edge[1]): weight, (edge[1], edge[0]): weight})'''

        print(self.win2.weightedges)
        for keey in self.win2.weightedges.keys():
            self.win2.ui.tableMatrix.setItem(keey[0], keey[1], QTableWidgetItem(str(self.win2.weightedges[keey])))
            self.win2.ui.tableMatrix.setItem(keey[1], keey[0], QTableWidgetItem(str(self.win2.weightedges[keey])))

    def setmanualmatrix(self):
        if self.win2.nodes == []:
            return
        self.win2.weightedges = dict()
        for i in range(2):
            for i in self.win2.nodes:
                for j in self.win2.nodes:
                    if self.win2.ui.tableMatrix.item(i, j).text() != "0" and i != j:
                        self.win2.weightedges.update({(i, j): int(self.win2.ui.tableMatrix.item(i, j).text())})
                        self.win2.ui.tableMatrix.setItem(j, i, QTableWidgetItem(self.win2.ui.tableMatrix.item(i, j).text()))
                    elif i == j:
                        self.win2.ui.tableMatrix.setItem(i, j, QTableWidgetItem("0"))
        print(self.win2.weightedges)

    def showgraph(self):
        if self.win2.nodes == [] or self.win2.weightedges == dict():
            return
        G = nx.Graph()
        G.add_nodes_from(self.win2.nodes)
        G.add_edges_from(self.win2.weightedges.keys())
        nx.draw_shell(G, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels=self.win2.weightedges, label_pos=0.1)
        plt.show()

    def bellmanford(self):
        try:
            src = int(self.ui.lineSrc.text())
            if src not in self.win2.nodes:
                self.ui.lineSrc.setText("Не існуе!")
                return
        except ValueError:
            self.ui.lineSrc.setText("Треба число!")
            return
        try:
            dest = int(self.ui.lineDest.text())
            if dest not in self.win2.nodes:
                self.ui.lineDest.setText("Не існуе!")
                return
        except ValueError:
            self.ui.lineDest.setText("Треба число!")
            return

        dist = [float("Inf")] * len(self.win2.nodes)
        prev = [None] * len(self.win2.nodes)
        dist[src] = 0
        for i in range(len(self.win2.nodes) - 1):
            for key in self.win2.weightedges.keys():
                if dist[key[0]] + self.win2.weightedges[key] < dist[key[1]]:
                    dist[key[1]] = dist[key[0]] + self.win2.weightedges[key]
                    prev[key[1]] = key[0]
                if dist[key[1]] + self.win2.weightedges[key] < dist[key[0]]:
                    dist[key[0]] = dist[key[1]] + self.win2.weightedges[key]
                    prev[key[0]] = key[1]
        print(dist)
        self.ui.labelPath.setText("Довжина найкоротшого шляху:{}".format(dist[dest]))
        for i in range(len(self.win2.nodes)):
            print("{} -> {}".format(i, dist[i]))
        print(prev)
        curr = dest
        path = []
        while curr is not None:
            path.append(curr)
            curr = prev[curr]
        print(path)
        pathedges = []
        for i in range(len(path) - 1):
            pathedges.append((path[i], path[i + 1]))
        print(pathedges)
        colored_nodes = [src, dest]

        G = nx.Graph()
        G.add_nodes_from(self.win2.nodes)
        G.add_edges_from(self.win2.weightedges.keys())
        nx.draw_shell(G, with_labels=True)
        nx.draw_networkx_nodes(G, pos=nx.shell_layout(G), nodelist=colored_nodes, node_color="Yellow" )
        nx.draw_networkx_edge_labels(G, pos=nx.shell_layout(G), edge_labels=self.win2.weightedges, label_pos=0.1)
        nx.draw_networkx_edges(G, pos=nx.shell_layout(G), edgelist=pathedges, edge_color="yellow")
        plt.show()

if __name__ == "__main__":  # Show the window if this file is launched directly, not imported
    app = QApplication(sys.argv)
    lab3 = Lab3()
    lab3.show()
    sys.exit(app.exec())