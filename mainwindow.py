# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\dataD\Qt\HMI-Lakban-Qt5\new_design2\mainWindow\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 451, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 30, 101, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setStyleSheet("color: rgb(10, 10, 10);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.cb_set_date = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_set_date.setGeometry(QtCore.QRect(120, 30, 321, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_set_date.sizePolicy().hasHeightForWidth())
        self.cb_set_date.setSizePolicy(sizePolicy)
        self.cb_set_date.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cb_set_date.setFont(font)
        self.cb_set_date.setStyleSheet("color: rgb(15, 15, 15);\n"
"background-color: rgb(254, 254, 254);")
        self.cb_set_date.setObjectName("cb_set_date")
        self.cb_set_date.addItem("")
        self.cb_set_date.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 431, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 427, 367))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalWidget = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalWidget.setGeometry(QtCore.QRect(20, 20, 271, 31))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_date = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_date.setFont(font)
        self.lbl_date.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_date.setObjectName("lbl_date")
        self.horizontalLayout.addWidget(self.lbl_date)
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lbl_time = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_time.setFont(font)
        self.lbl_time.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 18pt \"Arial\";")
        self.lbl_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_time.setObjectName("lbl_time")
        self.horizontalLayout.addWidget(self.lbl_time)
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setGeometry(QtCore.QRect(460, 120, 20, 471))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(480, 110, 311, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 150, 101, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(10, 10, 10);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 101, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(10, 10, 10);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.pb_set_total = QtWidgets.QPushButton(self.groupBox)
        self.pb_set_total.setGeometry(QtCore.QRect(240, 310, 61, 61))
        self.pb_set_total.setMinimumSize(QtCore.QSize(50, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pb_set_total.setFont(font)
        self.pb_set_total.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"background-color: rgb(0, 0, 131);")
        self.pb_set_total.setObjectName("pb_set_total")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 230, 101, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(10, 10, 10);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lbl_total = QtWidgets.QLabel(self.groupBox)
        self.lbl_total.setGeometry(QtCore.QRect(120, 310, 121, 61))
        self.lbl_total.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_total.setFont(font)
        self.lbl_total.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"color: rgb(15, 15, 15);")
        self.lbl_total.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_total.setObjectName("lbl_total")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 310, 101, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(10, 10, 10);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255,0);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pb_update = QtWidgets.QPushButton(self.groupBox)
        self.pb_update.setGeometry(QtCore.QRect(120, 380, 181, 61))
        self.pb_update.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pb_update.setFont(font)
        self.pb_update.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";\n"
"background-color: rgb(0, 0, 131);")
        self.pb_update.setObjectName("pb_update")
        self.lbl_po = QtWidgets.QLabel(self.groupBox)
        self.lbl_po.setGeometry(QtCore.QRect(120, 70, 181, 61))
        self.lbl_po.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_po.setFont(font)
        self.lbl_po.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"color: rgb(15, 15, 15);")
        self.lbl_po.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_po.setObjectName("lbl_po")
        self.cb_shift = QtWidgets.QLabel(self.groupBox)
        self.cb_shift.setGeometry(QtCore.QRect(120, 150, 181, 61))
        self.cb_shift.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cb_shift.setFont(font)
        self.cb_shift.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"color: rgb(15, 15, 15);")
        self.cb_shift.setAlignment(QtCore.Qt.AlignCenter)
        self.cb_shift.setObjectName("cb_shift")
        self.cb_line = QtWidgets.QLabel(self.groupBox)
        self.cb_line.setGeometry(QtCore.QRect(120, 230, 181, 61))
        self.cb_line.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cb_line.setFont(font)
        self.cb_line.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"color: rgb(15, 15, 15);")
        self.cb_line.setAlignment(QtCore.Qt.AlignCenter)
        self.cb_line.setObjectName("cb_line")
        self.txt_loading = QtWidgets.QLabel(self.groupBox)
        self.txt_loading.setGeometry(QtCore.QRect(220, 450, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_loading.setFont(font)
        self.txt_loading.setObjectName("txt_loading")
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_8.raise_()
        self.lbl_total.raise_()
        self.label_10.raise_()
        self.pb_update.raise_()
        self.lbl_po.raise_()
        self.pb_set_total.raise_()
        self.cb_shift.raise_()
        self.cb_line.raise_()
        self.txt_loading.raise_()
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(330, 20, 215, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 14pt \"Arial\";\n"
"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 255);")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.txt_username = QtWidgets.QLabel(self.groupBox_3)
        self.txt_username.setGeometry(QtCore.QRect(570, 20, 215, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_username.setFont(font)
        self.txt_username.setStyleSheet("border: 1px solid blue;")
        self.txt_username.setObjectName("txt_username")
        self.pb_logout = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_logout.setGeometry(QtCore.QRect(670, 60, 115, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pb_logout.setFont(font)
        self.pb_logout.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 0, 0);")
        self.pb_logout.setObjectName("pb_logout")
        self.txt_loading_logout = QtWidgets.QLabel(self.groupBox_3)
        self.txt_loading_logout.setGeometry(QtCore.QRect(580, 65, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_loading_logout.setFont(font)
        self.txt_loading_logout.setObjectName("txt_loading_logout")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Current total in PO"))
        self.label_13.setText(_translate("MainWindow", "Date :"))
        self.cb_set_date.setItemText(0, _translate("MainWindow", "11 November 2018"))
        self.cb_set_date.setItemText(1, _translate("MainWindow", "12 November 2018"))
        self.lbl_date.setText(_translate("MainWindow", "12/11/2019"))
        self.label.setText(_translate("MainWindow", "|"))
        self.lbl_time.setText(_translate("MainWindow", "09:45:55"))
        self.groupBox.setTitle(_translate("MainWindow", "Update total value of PO"))
        self.label_11.setText(_translate("MainWindow", "Shift :"))
        self.label_12.setText(_translate("MainWindow", "PO :"))
        self.pb_set_total.setText(_translate("MainWindow", "SET"))
        self.label_8.setText(_translate("MainWindow", "Line :"))
        self.lbl_total.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Total :"))
        self.pb_update.setText(_translate("MainWindow", "UPDATE"))
        self.lbl_po.setText(_translate("MainWindow", "0"))
        self.cb_shift.setText(_translate("MainWindow", "-"))
        self.cb_line.setText(_translate("MainWindow", "-"))
        self.txt_loading.setText(_translate("MainWindow", "Loading..."))
        self.label_9.setText(_translate("MainWindow", "HMI Lakban"))
        self.txt_username.setText(_translate("MainWindow", "Admin"))
        self.pb_logout.setText(_translate("MainWindow", "Logout"))
        self.txt_loading_logout.setText(_translate("MainWindow", "Loading..."))

