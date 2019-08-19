# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\dataD\Qt\HMI-Lakban-Qt5\new_design2\mainWindow\rework.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 376)
        Form.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 10, 191, 51))
        self.label.setStyleSheet("color: rgb(255, 170, 0);\n"
"font: 75 28pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 81, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 175, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.line_val = QtWidgets.QLabel(Form)
        self.line_val.setGeometry(QtCore.QRect(340, 100, 191, 41))
        self.line_val.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(236, 236, 236);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.line_val.setAlignment(QtCore.Qt.AlignCenter)
        self.line_val.setObjectName("line_val")
        self.pb_submit = QtWidgets.QPushButton(Form)
        self.pb_submit.setGeometry(QtCore.QRect(0, 280, 611, 101))
        self.pb_submit.setStyleSheet("font: 75 28pt \"Arial\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pb_submit.setObjectName("pb_submit")
        self.exit_pb = QtWidgets.QPushButton(Form)
        self.exit_pb.setGeometry(QtCore.QRect(540, 10, 50, 41))
        self.exit_pb.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(243, 0, 0);\n"
"font: 75 28pt \"Arial\";")
        self.exit_pb.setObjectName("exit_pb")
        self.horizontalWidget = QtWidgets.QWidget(Form)
        self.horizontalWidget.setGeometry(QtCore.QRect(300, 160, 244, 80))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rework_val = QtWidgets.QLabel(self.horizontalWidget)
        self.rework_val.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Arial\";")
        self.rework_val.setAlignment(QtCore.Qt.AlignCenter)
        self.rework_val.setObjectName("rework_val")
        self.horizontalLayout.addWidget(self.rework_val, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pb_set_rework = QtWidgets.QPushButton(self.horizontalWidget)
        self.pb_set_rework.setMinimumSize(QtCore.QSize(50, 41))
        self.pb_set_rework.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_set_rework.setFont(font)
        self.pb_set_rework.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pb_set_rework.setObjectName("pb_set_rework")
        self.horizontalLayout.addWidget(self.pb_set_rework)
        self.txt_loading = QtWidgets.QLabel(Form)
        self.txt_loading.setGeometry(QtCore.QRect(130, 320, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_loading.setFont(font)
        self.txt_loading.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.txt_loading.setObjectName("txt_loading")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "REWORK"))
        self.label_2.setText(_translate("Form", "Line :"))
        self.label_3.setText(_translate("Form", "Jumlah Rework :"))
        self.line_val.setText(_translate("Form", "Line 23"))
        self.pb_submit.setText(_translate("Form", "SUBMIT"))
        self.exit_pb.setText(_translate("Form", "x"))
        self.rework_val.setText(_translate("Form", "1000"))
        self.pb_set_rework.setText(_translate("Form", "SET"))
        self.txt_loading.setText(_translate("Form", "Loading..."))

