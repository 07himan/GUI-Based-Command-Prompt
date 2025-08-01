# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from notNeeded.filemang import fileManWindow
from network_merge_pyqt5_logic import NetworkQtWindow
from systeminfo_merged import SystemInfoApp
from filemang_merge_pyqt5_logic import FileManQtWindow 

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 761, 491))
        self.label.setText("")
                
        self.movie = QtGui.QMovie("animated2.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 70, 201, 51))
        self.label_2.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 150, 240, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #670D2F;   \n"
"    color: white;\n"
"    font: bold 16px;\n"
"    border-radius: 10px;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A53860; \n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("FILE.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 230, 240, 60))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #344C64;\n"
"    color: white;\n"
"    font: bold 16px;\n"
"    border-radius: 10px;\n"
"    padding: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #57A6A1;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("network.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 310, 240, 60))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #1D267D;\n"
"    color: white;\n"
"    font: bold 16px;\n"
"    border-radius: 10px;\n"
"    padding: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5C469C;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("SINFO.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.open_file_management)
        self.pushButton_2.clicked.connect(self.open_network)
        self.pushButton_3.clicked.connect(self.open_system_info)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Custom Shell"))
        self.pushButton.setText(_translate("MainWindow", "    File Management"))
        self.pushButton_2.setText(_translate("MainWindow", "    Network"))
        self.pushButton_3.setText(_translate("MainWindow", "    System Info"))
        
    def open_file_management(self):
        self.file_window = FileManQtWindow()
        self.file_window.show()

    def open_network(self):
        self.network_window = NetworkQtWindow()
        self.network_window.show()

    def open_system_info(self):
        self.system_info_window = SystemInfoApp()
        self.system_info_window.show()

        
import notNeeded.bg_rc as bg_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
