# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window2(object):
    def setupUi(self, Window2):
        Window2.setObjectName("Window2")
        Window2.resize(551, 425)
        Window2.setMinimumSize(QtCore.QSize(551, 400))
        Window2.setMaximumSize(QtCore.QSize(551, 540))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 60, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 99, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 79, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 30, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 40, 119))
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
        brush = QtGui.QBrush(QtGui.QColor(179, 60, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 157, 217))
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
        brush = QtGui.QBrush(QtGui.QColor(179, 60, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 99, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 79, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 30, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 40, 119))
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
        brush = QtGui.QBrush(QtGui.QColor(179, 60, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 157, 217))
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
        brush = QtGui.QBrush(QtGui.QColor(89, 30, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 60, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 99, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 79, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 30, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 40, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 30, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 30, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 60, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 60, 179))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 60, 179))
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
        Window2.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(Window2)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_7 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_7.setEnabled(True)
        self.splitter_7.setGeometry(QtCore.QRect(20, 20, 139, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_7.sizePolicy().hasHeightForWidth())
        self.splitter_7.setSizePolicy(sizePolicy)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setOpaqueResize(False)
        self.splitter_7.setChildrenCollapsible(False)
        self.splitter_7.setObjectName("splitter_7")
        self.labelMale = QtWidgets.QLabel(self.splitter_7)
        self.labelMale.setMinimumSize(QtCore.QSize(0, 27))
        self.labelMale.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        self.labelMale.setFont(font)
        self.labelMale.setObjectName("labelMale")
        self.listboxMale = QtWidgets.QListWidget(self.splitter_7)
        self.listboxMale.setMinimumSize(QtCore.QSize(0, 272))
        self.listboxMale.setMaximumSize(QtCore.QSize(16777215, 272))
        self.listboxMale.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listboxMale.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listboxMale.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listboxMale.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listboxMale.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listboxMale.setObjectName("listboxMale")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_8.sizePolicy().hasHeightForWidth())
        self.splitter_8.setSizePolicy(sizePolicy)
        self.splitter_8.setMinimumSize(QtCore.QSize(0, 26))
        self.splitter_8.setMaximumSize(QtCore.QSize(139, 16777215))
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setOpaqueResize(False)
        self.splitter_8.setChildrenCollapsible(False)
        self.splitter_8.setObjectName("splitter_8")
        self.radiobuttonMaleA = QtWidgets.QRadioButton(self.splitter_8)
        self.radiobuttonMaleA.setMinimumSize(QtCore.QSize(67, 0))
        self.radiobuttonMaleA.setMaximumSize(QtCore.QSize(67, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radiobuttonMaleA.setFont(font)
        self.radiobuttonMaleA.setChecked(True)
        self.radiobuttonMaleA.setObjectName("radiobuttonMaleA")
        self.radiobuttonMaleB = QtWidgets.QRadioButton(self.splitter_8)
        self.radiobuttonMaleB.setMinimumSize(QtCore.QSize(67, 0))
        self.radiobuttonMaleB.setMaximumSize(QtCore.QSize(67, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radiobuttonMaleB.setFont(font)
        self.radiobuttonMaleB.setObjectName("radiobuttonMaleB")
        self.buttonSaveMale = QtWidgets.QPushButton(self.splitter_7)
        self.buttonSaveMale.setMinimumSize(QtCore.QSize(0, 51))
        self.buttonSaveMale.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonSaveMale.setFont(font)
        self.buttonSaveMale.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.buttonSaveMale.setObjectName("buttonSaveMale")
        self.splitter_9 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_9.setGeometry(QtCore.QRect(180, 20, 139, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_9.sizePolicy().hasHeightForWidth())
        self.splitter_9.setSizePolicy(sizePolicy)
        self.splitter_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setOpaqueResize(False)
        self.splitter_9.setChildrenCollapsible(False)
        self.splitter_9.setObjectName("splitter_9")
        self.labelFemale = QtWidgets.QLabel(self.splitter_9)
        self.labelFemale.setMinimumSize(QtCore.QSize(0, 27))
        self.labelFemale.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        self.labelFemale.setFont(font)
        self.labelFemale.setObjectName("labelFemale")
        self.listboxFemale = QtWidgets.QListWidget(self.splitter_9)
        self.listboxFemale.setMinimumSize(QtCore.QSize(0, 272))
        self.listboxFemale.setMaximumSize(QtCore.QSize(16777215, 272))
        self.listboxFemale.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listboxFemale.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.listboxFemale.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listboxFemale.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listboxFemale.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listboxFemale.setObjectName("listboxFemale")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_11.sizePolicy().hasHeightForWidth())
        self.splitter_11.setSizePolicy(sizePolicy)
        self.splitter_11.setMinimumSize(QtCore.QSize(0, 26))
        self.splitter_11.setMaximumSize(QtCore.QSize(139, 16777215))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setOpaqueResize(False)
        self.splitter_11.setChildrenCollapsible(False)
        self.splitter_11.setObjectName("splitter_11")
        self.radiobuttonFemaleA = QtWidgets.QRadioButton(self.splitter_11)
        self.radiobuttonFemaleA.setMinimumSize(QtCore.QSize(67, 0))
        self.radiobuttonFemaleA.setMaximumSize(QtCore.QSize(67, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radiobuttonFemaleA.setFont(font)
        self.radiobuttonFemaleA.setChecked(True)
        self.radiobuttonFemaleA.setObjectName("radiobuttonFemaleA")
        self.radiobuttonFemaleB = QtWidgets.QRadioButton(self.splitter_11)
        self.radiobuttonFemaleB.setMinimumSize(QtCore.QSize(67, 0))
        self.radiobuttonFemaleB.setMaximumSize(QtCore.QSize(67, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radiobuttonFemaleB.setFont(font)
        self.radiobuttonFemaleB.setObjectName("radiobuttonFemaleB")
        self.buttonSaveFemale = QtWidgets.QPushButton(self.splitter_9)
        self.buttonSaveFemale.setMinimumSize(QtCore.QSize(0, 51))
        self.buttonSaveFemale.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonSaveFemale.setFont(font)
        self.buttonSaveFemale.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.buttonSaveFemale.setObjectName("buttonSaveFemale")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(340, 50, 191, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.buttonSaveA = QtWidgets.QPushButton(self.splitter)
        self.buttonSaveA.setMinimumSize(QtCore.QSize(0, 56))
        self.buttonSaveA.setMaximumSize(QtCore.QSize(16777215, 56))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonSaveA.setFont(font)
        self.buttonSaveA.setStyleSheet("background-color: #4CC34C")
        self.buttonSaveA.setObjectName("buttonSaveA")
        self.buttonClearA = QtWidgets.QPushButton(self.splitter)
        self.buttonClearA.setMinimumSize(QtCore.QSize(0, 56))
        self.buttonClearA.setMaximumSize(QtCore.QSize(16777215, 56))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonClearA.setFont(font)
        self.buttonClearA.setStyleSheet("background-color: #4CC34C")
        self.buttonClearA.setObjectName("buttonClearA")
        self.buttonReadA = QtWidgets.QPushButton(self.splitter)
        self.buttonReadA.setMinimumSize(QtCore.QSize(0, 56))
        self.buttonReadA.setMaximumSize(QtCore.QSize(16777215, 56))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonReadA.setFont(font)
        self.buttonReadA.setStyleSheet("background-color: #4CC34C")
        self.buttonReadA.setObjectName("buttonReadA")
        self.buttonSaveB = QtWidgets.QPushButton(self.splitter)
        self.buttonSaveB.setMinimumSize(QtCore.QSize(0, 56))
        self.buttonSaveB.setMaximumSize(QtCore.QSize(16777215, 56))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonSaveB.setFont(font)
        self.buttonSaveB.setStyleSheet("background-color: rgb(76, 195, 187);")
        self.buttonSaveB.setObjectName("buttonSaveB")
        self.buttonClearB = QtWidgets.QPushButton(self.splitter)
        self.buttonClearB.setMinimumSize(QtCore.QSize(0, 56))
        self.buttonClearB.setMaximumSize(QtCore.QSize(16777215, 56))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonClearB.setFont(font)
        self.buttonClearB.setStyleSheet("background-color: rgb(76, 195, 187);")
        self.buttonClearB.setObjectName("buttonClearB")
        self.buttonReadB = QtWidgets.QPushButton(self.splitter)
        self.buttonReadB.setMinimumSize(QtCore.QSize(0, 56))
        self.buttonReadB.setMaximumSize(QtCore.QSize(16777215, 56))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonReadB.setFont(font)
        self.buttonReadB.setStyleSheet("background-color: rgb(76, 195, 187);")
        self.buttonReadB.setObjectName("buttonReadB")
        Window2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "2-ге вікно"))
        self.labelMale.setText(_translate("Window2", "<html><head/><body><p><span style=\" font-size:12pt;\">Чоловічі імена</span></p></body></html>"))
        self.radiobuttonMaleA.setText(_translate("Window2", "A"))
        self.radiobuttonMaleB.setText(_translate("Window2", "B"))
        self.buttonSaveMale.setText(_translate("Window2", "Зберегти в множину \n"
"\"чоловічі імена\""))
        self.labelFemale.setText(_translate("Window2", "<html><head/><body><p><span style=\" font-size:12pt;\">Жіночі імена</span></p></body></html>"))
        self.radiobuttonFemaleA.setText(_translate("Window2", "A"))
        self.radiobuttonFemaleB.setText(_translate("Window2", "B"))
        self.buttonSaveFemale.setText(_translate("Window2", "Зберегти в множину\n"
"\"жіночі імена\""))
        self.buttonSaveA.setText(_translate("Window2", "Зберегти А"))
        self.buttonClearA.setText(_translate("Window2", "Очистити А"))
        self.buttonReadA.setText(_translate("Window2", "Зчитати А"))
        self.buttonSaveB.setText(_translate("Window2", "Зберегти B"))
        self.buttonClearB.setText(_translate("Window2", "Очистити B"))
        self.buttonReadB.setText(_translate("Window2", "Зчитати B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window2 = QtWidgets.QMainWindow()
    ui = Ui_Window2()
    ui.setupUi(Window2)
    Window2.show()
    sys.exit(app.exec_())