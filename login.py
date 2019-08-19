# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\dataD\Qt\HMI-Lakban-Qt5\new_design2\mainWindow\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(170, 170, 451, 311))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 101, 61))
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
        self.label_11.setStyleSheet("color: rgb(10,10,10);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 101, 61))
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
        self.label_12.setStyleSheet("color: rgb(10,10,10);\n"
"font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.pb_login = QtWidgets.QPushButton(self.groupBox)
        self.pb_login.setGeometry(QtCore.QRect(250, 200, 181, 61))
        self.pb_login.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_login.setFont(font)
        self.pb_login.setStyleSheet("background-color: rgb(0, 0, 131);\n"
"color: rgb(255, 255, 255);")
        self.pb_login.setObjectName("pb_login")
        self.input_username = QtWidgets.QLineEdit(self.groupBox)
        self.input_username.setGeometry(QtCore.QRect(120, 60, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_username.setFont(font)
        self.input_username.setObjectName("input_username")
        self.input_pass = QtWidgets.QLineEdit(self.groupBox)
        self.input_pass.setGeometry(QtCore.QRect(120, 130, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_pass.setFont(font)
        self.input_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_pass.setObjectName("input_pass")
        self.txt_loading = QtWidgets.QLabel(self.groupBox)
        self.txt_loading.setGeometry(QtCore.QRect(160, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_loading.setFont(font)
        self.txt_loading.setObjectName("txt_loading")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(550, 30, 221, 51))
        self.label_9.setStyleSheet("font: 75 18pt \"Arial\";\n"
"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 255);")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setStyleSheet("border: 2px solid blue;\n"
"background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.groupBox.raise_()
        self.label_9.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_11.setText(_translate("Form", "password"))
        self.label_12.setText(_translate("Form", "username"))
        self.pb_login.setText(_translate("Form", "LOGIN"))
        self.txt_loading.setText(_translate("Form", "Loading..."))
        self.label_9.setText(_translate("Form", "HMI Lakban"))

