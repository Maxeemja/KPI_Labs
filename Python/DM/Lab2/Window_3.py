# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window3(object):
    def setupUi(self, Window3):
        Window3.setObjectName("Window3")
        Window3.resize(1440, 510)
        Window3.setMinimumSize(QtCore.QSize(0, 0))
        Window3.setMaximumSize(QtCore.QSize(12121212, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        Window3.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(Window3)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonGetRelationR = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetRelationR.setGeometry(QtCore.QRect(890, 390, 534, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonGetRelationR.setFont(font)
        self.buttonGetRelationR.setStyleSheet("background-color: rgb(244, 202, 22);")
        self.buttonGetRelationR.setObjectName("buttonGetRelationR")
        self.labelRelationR = QtWidgets.QLabel(self.centralwidget)
        self.labelRelationR.setGeometry(QtCore.QRect(890, 20, 191, 21))
        self.labelRelationR.setObjectName("labelRelationR")
        self.buttonGetRelationS = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetRelationS.setGeometry(QtCore.QRect(340, 390, 534, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonGetRelationS.setFont(font)
        self.buttonGetRelationS.setStyleSheet("background-color: rgb(244, 202, 22);")
        self.buttonGetRelationS.setObjectName("buttonGetRelationS")
        self.labelRelationS = QtWidgets.QLabel(self.centralwidget)
        self.labelRelationS.setGeometry(QtCore.QRect(340, 20, 191, 21))
        self.labelRelationS.setObjectName("labelRelationS")
        self.tableRelationS = QtWidgets.QTableWidget(self.centralwidget)
        self.tableRelationS.setGeometry(QtCore.QRect(340, 50, 534, 326))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableRelationS.setFont(font)
        self.tableRelationS.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.tableRelationS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableRelationS.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableRelationS.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableRelationS.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableRelationS.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableRelationS.setObjectName("tableRelationS")
        self.tableRelationS.setColumnCount(0)
        self.tableRelationS.setRowCount(0)
        self.tableRelationS.horizontalHeader().setCascadingSectionResizes(True)
        self.tableRelationS.horizontalHeader().setDefaultSectionSize(53)
        self.tableRelationS.horizontalHeader().setMinimumSectionSize(53)
        self.tableRelationS.horizontalHeader().setSortIndicatorShown(False)
        self.tableRelationS.horizontalHeader().setStretchLastSection(True)
        self.tableRelationS.verticalHeader().setCascadingSectionResizes(True)
        self.tableRelationS.verticalHeader().setDefaultSectionSize(40)
        self.tableRelationS.verticalHeader().setMinimumSectionSize(34)
        self.tableRelationS.verticalHeader().setStretchLastSection(True)
        self.listboxSetA = QtWidgets.QListWidget(self.centralwidget)
        self.listboxSetA.setGeometry(QtCore.QRect(20, 50, 141, 331))
        self.listboxSetA.setObjectName("listboxSetA")
        self.listboxSetB = QtWidgets.QListWidget(self.centralwidget)
        self.listboxSetB.setGeometry(QtCore.QRect(180, 50, 141, 331))
        self.listboxSetB.setObjectName("listboxSetB")
        self.buttonFillSetA = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFillSetA.setGeometry(QtCore.QRect(20, 390, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonFillSetA.setFont(font)
        self.buttonFillSetA.setStyleSheet("background-color: rgb(244, 202, 22);")
        self.buttonFillSetA.setObjectName("buttonFillSetA")
        self.buttonFillSetB = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFillSetB.setGeometry(QtCore.QRect(180, 390, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonFillSetB.setFont(font)
        self.buttonFillSetB.setStyleSheet("background-color: rgb(244, 202, 22);")
        self.buttonFillSetB.setObjectName("buttonFillSetB")
        self.labelSetA = QtWidgets.QLabel(self.centralwidget)
        self.labelSetA.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.labelSetA.setObjectName("labelSetA")
        self.labelSetB = QtWidgets.QLabel(self.centralwidget)
        self.labelSetB.setGeometry(QtCore.QRect(180, 20, 91, 21))
        self.labelSetB.setObjectName("labelSetB")
        self.browserAction = QtWidgets.QTextBrowser(self.centralwidget)
        self.browserAction.setGeometry(QtCore.QRect(20, 450, 1401, 41))
        self.browserAction.setMinimumSize(QtCore.QSize(1241, 0))
        self.browserAction.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.browserAction.setObjectName("browserAction")
        self.tableRelationR = QtWidgets.QTableWidget(self.centralwidget)
        self.tableRelationR.setGeometry(QtCore.QRect(890, 50, 534, 326))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableRelationR.setFont(font)
        self.tableRelationR.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.tableRelationR.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableRelationR.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableRelationR.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableRelationR.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableRelationR.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableRelationR.setObjectName("tableRelationR")
        self.tableRelationR.setColumnCount(0)
        self.tableRelationR.setRowCount(0)
        self.tableRelationR.horizontalHeader().setCascadingSectionResizes(True)
        self.tableRelationR.horizontalHeader().setDefaultSectionSize(53)
        self.tableRelationR.horizontalHeader().setMinimumSectionSize(53)
        self.tableRelationR.horizontalHeader().setSortIndicatorShown(False)
        self.tableRelationR.horizontalHeader().setStretchLastSection(True)
        self.tableRelationR.verticalHeader().setCascadingSectionResizes(True)
        self.tableRelationR.verticalHeader().setDefaultSectionSize(40)
        self.tableRelationR.verticalHeader().setMinimumSectionSize(34)
        self.tableRelationR.verticalHeader().setStretchLastSection(True)
        Window3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window3)
        QtCore.QMetaObject.connectSlotsByName(Window3)

    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        Window3.setWindowTitle(_translate("Window3", "?????????? ???3"))
        self.buttonGetRelationR.setText(_translate("Window3", "???????????????????? ???????????????????? aRb"))
        self.labelRelationR.setText(_translate("Window3", "<html><head/><body><p><span style=\" font-size:12pt;\">?????????????? ???????????????????? aRb:</span></p></body></html>"))
        self.buttonGetRelationS.setText(_translate("Window3", "???????????????????? ???????????????????? aSb"))
        self.labelRelationS.setText(_translate("Window3", "<html><head/><body><p><span style=\" font-size:12pt;\">?????????????? ???????????????????? aSb:</span></p></body></html>"))
        self.buttonFillSetA.setText(_translate("Window3", "??????????????????????\n"
"?????????????? ??"))
        self.buttonFillSetB.setText(_translate("Window3", "??????????????????????\n"
"?????????????? ??"))
        self.labelSetA.setText(_translate("Window3", "<html><head/><body><p><span style=\" font-size:12pt;\">?????????????? ??:</span></p></body></html>"))
        self.labelSetB.setText(_translate("Window3", "<html><head/><body><p><span style=\" font-size:12pt;\">?????????????? B:</span></p></body></html>"))
        self.browserAction.setHtml(_translate("Window3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window3 = QtWidgets.QMainWindow()
    ui = Ui_Window3()
    ui.setupUi(Window3)
    Window3.show()
    sys.exit(app.exec_())
