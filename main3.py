# HTTP Request test
# http://samuelofficial.id/db/nabati_hmi_test_lanius/get_line_data.php
import requests
from requests_jwt import JWTAuth

import threading

# always seem to need this
import sys
import subprocess
# For PostgreSQL database
# import psycopg2

# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# for serial communication
import serial
import time
import threading
from datetime import datetime, timedelta

# For json parsing
import json

# This is our window from QtCreator
import mainwindow
import rework
import numpad
import popup
import login

# Windows
mainwin = ''
reworkwin = ''
numpadwin = ''
popupwin = ''
loginwin=''

# variables
style_succeed = (
    "color: rgb(0, 79, 239);\nbackground-color: rgb(255, 255, 255);\nborder-color: rgb(0, 76, 229);\nfont: 75 10pt \"Arial\";")

style_waiting = (
    "color: rgb(0, 0, 255);\nbackground-color: rgb(255, 255, 255);\nborder-color: rgb(0, 0, 255);\nfont: 75 10pt \"Arial\";")

style_failed = (
    "color: rgb(255, 15, 15);\nbackground-color: rgb(255, 255, 255);\nborder-color: rgb(255, 15, 15);\nfont: 75 10pt \"Arial\";")
style_off = ("color: rgb(255, 0, 0);\n" + "font: 75 17pt \"Arial\";\n" + "background-color: rgb(214, 214, 214);")
val_line_active = 1
val_of_line = 0
ready_setup = 0
current_time = 0
total_val = ''
data_ready = False
numpad_f = 0
all_data=''
init_cb=False
JwToken=''
firstname=''
lastname=''

# components
line_val = ''
rework_val = ''
val_line23 = ''
val_line24 = ''
val_line25 = ''
val_line26 = ''
time_lbl = ''
numpad_val = ''
total_lbl = ''
table_widget = ''
line_cb = ''
lbl_line = ''
verticalLayoutWidget = ''
verticalLayout = ''
scrollArea = ''

# Python threads
clockThread = ''
# ip: 192.168.3.2:8081/
# MAC :
# eth0 =  b8:27:eb:c3:8d:2f
# wlan0 =  b8:27:eb:96:d8:7a
# Virtul keyboard
# https://stackoverflow.com/questions/49306865/matchbox-keyboard-on-input-for-qlineedit-pyqt5

class clockThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        getLineData()


def getLineData():
    global current_time, time_lbl, ready_setup
    while 1:
        if ready_setup == 1:
            # Get current time
            current_time = time.localtime(time.time())
            time_now = [0] * 3
            time_now[0] = str(current_time.tm_hour)
            time_now[1] = str(current_time.tm_min)
            time_now[2] = str(current_time.tm_sec)
            current_time = ''
            for i in range(3):
                if len(time_now[i]) == 1:
                    time_now[i] = '0' + time_now[i]
            current_time = time_now[0] + ':' + time_now[1] + ':' + time_now[2]
            time_lbl.setText(current_time)
            time.sleep(1)

class MonitorLineDataThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, parent):
        QThread.__init__(self, parent)
        self.signal.connect(parent.getData)
        self.parent=parent
        print("Init Thread")

    # run method gets called when we start the thread
    def run(self):
        global line_data, data_ready
        while 1:
            data_ready = False
            try:
                headers = {'Authorization': 'Bearer ' + JwToken, 'content-type': 'application/json'}
                line_data = requests.get("http://192.168.3.2:8081/api/v1/rencana-produksi", headers=headers)
                data_ready = True
                print("Data")
                if(str(line_data.status_code)=='200' or str(line_data.status_code)=='201'):
                    self.signal.emit(line_data.text)
                # self.parent.updateF=0
            except:
                print("Error in connection!")
            time.sleep(1)

class LoadLineDataThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        # self.signal.connect(parent.getData)
        print("Init Thread")

    # run method gets called when we start the thread
    def run(self):
        global line_data, data_ready, JwToken
        data_ready = False
        while not data_ready:
            try:
                print(JwToken)
                headers = {'Authorization': 'token {}'.format(JwToken)}
                # headers={'Authorization': 'access_token '+ JwToken}
                auth = JWTAuth(str(JwToken))
                headers = {'Authorization': 'Bearer ' + JwToken, 'content-type': 'application/json'}
                line_data = requests.get("http://192.168.3.2:8081/api/v1/rencana-produksi", headers=headers)
                data_ready = True
                print(line_data.text)
                print(line_data.status_code)
                if(str(line_data.status_code)=='200' or str(line_data.status_code)=='201'):
                    self.signal.emit(line_data.text)
                else:
                    print('Failed to retrieve data')
            except:
                print("Error in connection while Load data!")
            time.sleep(1)

class Popup(QMainWindow, popup.Ui_Form):
    def load_finished(self, result):
        global mainwin
        self.result=result
        print("Load Finished")
        mainwin=MainWindow(None)
        mainwin.show()
        mainwin.getData(self.result)
        self.close()

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file
        # Move to the center of window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # Always on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.popup_text.setText("Retrieve data ...")
        self.popup_text.setStyleSheet(style_waiting)

        # Threading
        self.load_thread = LoadLineDataThread()  # This is the thread object
        # Connect the signal from the thread to the finished method
        self.load_thread.signal.connect(self.load_finished)
        self.load_thread.start()
        print("Init Popup")

class Numpad(QMainWindow, numpad.Ui_Form):
    def pb_1_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('1')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '1')

    def pb_2_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('2')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '2')

    def pb_3_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('3')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '3')

    def pb_4_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('4')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '4')

    def pb_5_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('5')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '5')

    def pb_6_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('6')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '6')

    def pb_7_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('7')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '7')

    def pb_8_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('8')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '8')

    def pb_9_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('9')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '9')

    def pb_0_click(self):
        if (self.lbl_val.text() == '0'):
            self.lbl_val.setText('0')
        else:
            self.lbl_val.setText(self.lbl_val.text() + '0')

    def pb_enter_click(self):
        # self.parent.rework_val.setText(self.lbl_val.text())
        self.parent.change_val.emit(int(self.lbl_val.text()))
        self.parent.setEnabled(True)
        self.close()

    def pb_del_click(self):
        val = self.lbl_val.text()
        if len(val) == 1:
            self.lbl_val.setText('0')
        else:
            val = val[0:len(val) - 1]
            self.lbl_val.setText(val)

    def pb_exit_click(self):
        self.parent.setEnabled(True)
        self.close()

    def pb_clear_click(self):
        self.lbl_val.setText('0')

    def __init__(self, parent):
        global numpad_val, lbl_line
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)  # gets defined in the UI file
        self.parent = parent
        print("NUMPADD")
        # Move to the center of window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # Always on top
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(QtCore.Qt.WindowFullScreen)
        # self.setWindowState(self, QtCore.Qt.WindowFullScreen)
        # Button number
        self.pb_1.clicked.connect(self.pb_1_click)
        self.pb_2.clicked.connect(self.pb_2_click)
        self.pb_3.clicked.connect(self.pb_3_click)
        self.pb_4.clicked.connect(self.pb_4_click)
        self.pb_5.clicked.connect(self.pb_5_click)
        self.pb_6.clicked.connect(self.pb_6_click)
        self.pb_7.clicked.connect(self.pb_7_click)
        self.pb_8.clicked.connect(self.pb_8_click)
        self.pb_9.clicked.connect(self.pb_9_click)
        self.pb_0.clicked.connect(self.pb_0_click)
        # pb enter
        self.pb_enter.clicked.connect(self.pb_enter_click)
        # pb delete
        self.pb_backspace.clicked.connect(self.pb_del_click)
        # Clear button
        self.pb_clear.clicked.connect(self.pb_clear_click)
        # pb exit
        self.pb_exit.clicked.connect(self.pb_exit_click)
        #
        self.lbl_val.setText(str(self.parent.val))
        self.lbl_line.setText(str(self.parent.line))

# Login window
class Login(QMainWindow, login.Ui_Form):
    def focusInEvent(self, event):
        print("focus in event")
        try:
            subprocess.Popen(["matchbox-keyboard"])
        except FileNotFoundError:
            pass

    def focusOutEvent(self, event):
        print("focus Out event")
        try:
            subprocess.Popen(["killall","matchbox-keyboard"])
        except:
            print("Error")

    def login(self):
        global popupwin, JwToken, firstname, lastname
        # Loading text
        self.txt_loading.setVisible(True)
        username=self.input_username.text()
        password=self.input_pass.text()
        print(username)
        print(password)
        # Get token with username & password
        #Create authentication header
        headers = {'Authorization': 'JwToken' + ' ', 'content-type': 'application/json'}
        try:
            r = requests.post("http://192.168.3.2:8081/api/v1/auth/login", headers=headers, json={"username": username, "password": password, "roleId":1})
            if(str(r.status_code)=="200" or str(r.status_code)=="201"):
                print("Login success")
                print(r.text)
                print(r.status_code)
                data=json.loads(r.text)
                # {"accessToken":"..-","user":{"id":2,"firstname":"Admin","lastname":"test","username":"admin","password":"$2b$10$tnnh6FzQE2BSH9PijLqOIuZBVLW2dq1yz6ZC.pyDKplKhfyLZR/MW","roleId":1}}
                firstname=data['user']['firstname']
                lastname=data['user']['lastname']
                JwToken=data['accessToken']
                # If success load the data
                self.close()
                popupwin = Popup()
                popupwin.show()
            else:
                print(r.status_code)
            self.txt_loading.setVisible(False)
        except Exception as e:
            self.txt_loading.setVisible(False)
            print("Error : "+ str(e))

    def focus(self):
        print("Focus")

    def __init__(self):
        # QMainWindow.__init__(self, parent)
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file
        # Center point
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.pb_login.clicked.connect(self.login)
        self.txt_loading.setVisible(False)
        self.input_username.focusInEvent =self.focusInEvent
        # self.input_username.focusOutEvent =self.focusOutEvent
        # self.input_pass.focusInEvent =self.focusInEvent
        self.input_pass.focusOutEvent =self.focusOutEvent

# create class for our Raspberry Pi GUI
class Rework(QMainWindow, rework.Ui_Form):
    change_val = pyqtSignal(int)

    def pb_set_rework_clicked(self):
        self.setEnabled(False)
        numpad_f = 2
        self.val = self.rework_val.text()
        Numpad(self).show()

    def update_rework_val(self, total, rencanaProduksiId):
        head = {"Authorization":"Token token="}
        url = 'http://192.168.3.2:8081/api/v1/lakban/rework'
        payload = {'total' : total, 'rencanaProduksiId' : rencanaProduksiId }
        try:
            r = requests.patch(url, payload)
            if(str(r.status_code)=="200" or str(r.status_code)=="201"):
                print("Update success")
                # aaa.lbl_total.setText(self.lbl_total.text())
                self.parent.updateF=1
            else:
                print(r.status_code)
            self.txt_loading.setVisible(False)
        except Exception as e:
            print("Error : "+ str(e))
            self.txt_loading.setVisible(False)


    def submit_rework(self):
        self.txt_loading.setVisible(True)
        self.parent.setEnabled(True)
        selisih = int(self.parent.lbl_total.text()) - int(self.rework_val.text())
        self.parent.lbl_total.setText(str(selisih))
        self.parent.parent.setEnabled(True)
        print("selisih:"+ str(selisih))
        self.close()
        self.update_rework_val(int(self.rework_val.text()), int(self.parent.rencanaProduksiId))
        # print(self.parent.rencanaProduksiId)

    def exit_pb_clicked(self):
        self.parent.parent.setEnabled(True)
        self.close()

    def change_val_(self, val):
        self.rework_val.setText(str(val))

    def __init__(self, parent):
        global line_val, rework_val
        # QMainWindow.__init__(self, parent)
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)  # gets defined in the UI file
        # Move to the center of window
        # Move to the center of window
        print("Reworkkk")
        self.parent = parent
        self.line_val.setText(str(self.parent.line))
        self.line = self.line_val.text()

        self.txt_loading.setVisible(False)

        # Center point
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # # Always on top
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # # Buttons
        self.pb_set_rework.clicked.connect(self.pb_set_rework_clicked)
        self.exit_pb.clicked.connect(self.exit_pb_clicked)
        self.pb_submit.clicked.connect(self.submit_rework)
        # line_val=self.line_val
        # rework_val=self.rework_val
        self.rework_val.setText('0')
        self.change_val.connect(self.change_val_)


# Update total value in QTableWidget
def update_value(line, tot_val):
    global table_widget
    table_widget.item(get_index(line), 1).setText(tot_val)


# def get all line name for table widget
def get_line_name_from_tw():
    global table_widget
    data = []
    for row in range(table_widget.rowCount()):
        data.append([])
        for column in range(table_widget.columnCount()):
            item = table_widget.item(row, column)
            # We suppose data are strings
            data[row].append(item.text())
    return data


def update_cb_line_name():
    global line_cb
    # new data from web
    new_data = [i[0] for i in get_line_name_from_tw()]
    # current data in cb
    current_data = [line_cb.itemText(i) for i in range(line_cb.count())]
    # get added data
    s = list(set(new_data) & set(current_data))
    added_data = list(i for i in new_data if not (i in s))
    if len(new_data) == len(current_data):
        if len(s) == len(new_data):
            # no update, data is same
            pass
        else:
            # update cb
            insert_line_name_to_cb(sorted(new_data))
    else:
        # update cb
        insert_line_name_to_cb(sorted(new_data))
    # print(new_data)

# Insert line name to combo box
def insert_line_name_to_cb(data):
    global line_cb
    line_cb.clear()
    # print(data)
    for i in data:
        line_cb.addItem(i)

# Get index in table widget
def get_index(line_name):
    global table_widget
    data = get_line_name_from_tw()
    for i in data:
        try:
            if line_name in str(i):
                return data.index(i)
        except:
            pass
    return -1

# Line JSON data
data_line = '[{"line":"Line 5", "total":"500"}, {"line":"Line 6", "total":"550"}]'

# Clear line data table
def clear_line_data_table():
    global table_widget
    table_widget.setRowCount(0)
    table_widget.setColumnCount(table_widget.columnCount())

# Update data line table
def update_table(data):
    global table_widget
    # Clear all data
    clear_line_data_table()
    # Insert new data
    data = json.loads(data)
    rowPosition = 0
    table_widget.setRowCount(len(data))
    for i in range(len(data)):
        # pass
        line = data[i]['line']
        total = data[i]['total']

        table_widget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(line))
        table_widget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(total))

        rowPosition += 1

# Insert data line table
def insert_table(data):
    global table_widget
    data = json.loads(data)
    for i in range(len(data)):
        # pass
        line = data[i]['line']
        total = data[i]['total']

        rowPosition = table_widget.rowCount()
        table_widget.insertRow(rowPosition)

        table_widget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(line))
        table_widget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(total))

data_line = '[{"13 August 2019":[{"po":"PO 5", "shift":"1", "line":"Line 1", "total":"777"}], "14 August 2019":[{"po":"PO 1", "shift":"1", "line":"Line 1", "total":"500"}, {"po":"PO 2", "shift":"2", "line":"Line 2", "total":"550"}]}]'

class ExampleWidget2(QGroupBox):
    change_val = pyqtSignal(int)

    def __init__(self, numAddWidget, po, shift, total, line, parent, pb_set_total):
        QGroupBox.__init__(self)
        self.parent = parent
        self.parent.pb_update.clicked.connect(self.update)
        # self.change_val.connect(self.change_val__)
        # self.parent.pb_set_total.clicked.connect(self.set_total)
        self.pb_set_total = pb_set_total
        self.numAddWidget = numAddWidget
        self.po = po
        self.shift = shift
        self.total = total
        self.line = line
        self.rencanaProduksiId=self.parent.rencanaProduksiId
        self.numAddItem = 1
        self.setTitle("No {}".format(self.numAddWidget))
        self.initSubject()
        self.organize()
        self.setStyleSheet("font: 14 14pt \"Arial\";\n"
                           "background-color: rgb(255, 255, 255);")

    def set_total(self):
        self.parent.setEnabled(False)
        self.parent.val = self.lbl_total.text()
        Numpad(self.parent).show()

    def update(self):
        self.parent.groupBox.setEnabled(False)
        self.parent.lbl_po.setText("0")
        self.parent.lbl_total.setText("0")
        self.parent.cb_shift.setText("-")
        self.parent.cb_line.setText("-")

    def edit(self):
        print(self.numAddWidget)
        self.parent.groupBox.setEnabled(True)
        self.parent.lbl_po.setText(str(self.po))
        self.parent.lbl_total.setText(self.lbl_total.text())
        self.parent.cb_shift.setText(str(self.shift))
        self.parent.cb_line.setText(str(self.line))
        self.parent.change_val__(self)

    def change_val_(self, val):
        print(self.lbl_total.text())
        print(val)
        # self.lbl_total.setText(val)
        self.change_val.emit(1)

    def change_val__(self, val):
        print(self.lbl_total.text())

    def initSubject(self):
        # self.parent.pb_set_total.clicked.connect(self.set_total)
        # self.pb_set_total.clicked.connect(self.set_total)
        self.change_val.connect(self.change_val__)
        # PO
        self.lbl_po = QLabel("{}".format(self.po), self)
        # self.lblSelectItem = QLabel(self)
        # Separator
        self.lbl_sep = QLabel("|", self)
        # Total
        self.lbl_total = QLabel("{}".format(self.total), self)

        # self.teachersselect = CheckableComboBox(self)
        # self.teachersselect.addItem("-Select {}-".format(self.numAddItem))
        # item = self.teachersselect.model().item(0, 0)
        # item.setCheckState(Qt.Unchecked)

        self.reworkbtn = QPushButton("Rework", self)
        self.reworkbtn.clicked.connect(self.rework)
        self.editbtn = QPushButton("Edit", self)
        self.editbtn.clicked.connect(self.edit)
        self.reworkbtn.setStyleSheet("font: 14 14pt \"Arial\";\n"
                                     "color: rgb(255,255,255);\n"
                                     "background-color: rgb(255, 0, 0);")
        self.editbtn.setStyleSheet("font: 14 14pt \"Arial\";\n"
                                   "color: rgb(255,255,255);\n"
                                   "background-color: rgb(0, 0, 255);")

    def organize(self):
        grid = QGridLayout(self)
        self.setLayout(grid)
        grid.addWidget(self.lbl_po, 0, 0, 1, 1)
        grid.addWidget(self.lbl_sep, 0, 1, 1, 1)
        grid.addWidget(self.lbl_total, 0, 2, 1, 1)
        grid.addWidget(self.reworkbtn, 0, 3, 1, 1)
        grid.addWidget(self.editbtn, 0, 4, 1, 1)

    def rework(self):
        self.parent.setEnabled(False)
        Rework(self).show()

    def addTeacher(self):
        self.numAddItem += 1
        self.teachersselect.addItem("-Select {}-".format(self.numAddItem))
        item = self.teachersselect.model().item(self.numAddItem - 1, 0)
        item.setCheckState(Qt.Unchecked)
aaa = ''

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    change_val = pyqtSignal(int)

    def pb_rework_press(self):
        global reworkwin, mainwin, line_val, line_cb
        if (line_cb.currentText() != ''):
            mainwin.setEnabled(False)
            line_val.setText(line_cb.currentText())
            reworkwin.show()
        else:
            print('Please select line!')

    def pb_submit_click(self):
        global total_lbl, line_cb, total_lbl
        update_value(str(line_cb.currentText()), total_lbl.text())

    def line_cb_changed(self):
        global total_lbl, line_cb, table_widget, lbl_line
        # set total value based on selected line
        idx = get_index(line_cb.currentText())
        total_lbl.setText(table_widget.item(idx, 1).text())
        lbl_line.setText(table_widget.item(idx, 0).text())

    def setDate(self):
        global all_data
        date_ = self.cb_set_date.currentText()
        print(date_)
        self.addWidget(self.cb_set_date.currentText(), all_data)
        # Reset edit group
        self.lbl_total.setText("0")
        self.lbl_po.setText("0")
        self.cb_shift.setText("-")
        self.cb_line.setText("-")
        self.groupBox.setEnabled(False)

    def change_val__(self, parent):
        global aaa
        aaa = parent
        self.parent = parent
        print(self.parent.lbl_total.text())

    def change_val_(self, val):
        self.lbl_total.setText(str(val))

    def update_total_finish_good(self, total, rencanaProduksiId):
        global aaa, alldata, JwToken
        try:
            # headers = {'Authorization': 'JwToken' + ' ', 'content-type': 'application/json'}
            r = requests.post("http://192.168.3.2:8081/api/v1/lakban/finishgood", data={'total': total, 'rencanaProduksiId': rencanaProduksiId})
            if(str(r.status_code)=="200" or str(r.status_code)=="201"):
                print("Update success")
                print(r.text)
                # aaa.lbl_total.setText(self.lbl_total.text())
                self.updateF=1
            else:
                print(r.status_code)
            self.txt_loading.setVisible(False)
        except Exception as e:
            print("Error : "+ str(e))
            self.txt_loading.setVisible(False)

    def update(self):
        global aaa
        self.txt_loading.setVisible(True)
        print('Update : '+ aaa.lbl_po.text())
        print('Rencana produksi ID : '+ str(aaa.rencanaProduksiId))
        print('Update : '+ aaa.lbl_total.text())
        self.update_total_finish_good(int(self.lbl_total.text()), int(aaa.rencanaProduksiId))
        # self.lbl_total.setText()
        # ExampleWidget2(self.numAddWidget, self.po, self.shift, self.total, self.line, self, self.pb_set_total).change_val_(self.lbl_total.text())

    def set_total(self):
        self.setEnabled(False)
        self.val = self.lbl_total.text()
        Numpad(self).show()

    def extract_time(self, alldata):
        try:
            return int(alldata['date'])
        except KeyError:
            return 0

    def addWidget(self, current_date, alldata):
        # Delete all data
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

        #====== sort of the date of data ======
        alldata2=[]
        if(len(alldata)>0):
            alldata = sorted(alldata, key=lambda k: k['date'], reverse=True)
            for data in alldata:
                alldata2.append(data)
            alldata=(alldata2)

        self.numAddWidget=0
        for i in range(len(alldata)):
            if(alldata[i]['date']==current_date):
                self.numAddWidget += 1
                self.po = alldata[i]['po_number']
                self.shift = alldata[i]['shiftId']
                self.total = alldata[i]['b_finishgood_qty_karton']
                self.line = alldata[i]['lineId']
                self.rencanaProduksiId=alldata[i]['id']
                self.widget = ExampleWidget2(self.numAddWidget, self.po, self.shift, self.total, self.line, self,
                                             self.pb_set_total)
                self.gridLayout.addWidget(self.widget)
            else:
                self.numAddWidget=0

        # Insert data based on the date that is selected
        # for i in range(len(self.data_po)):

    def updateCBDate(self, data):
        # new data from web
        new_data = sorted(set(data))
        print("new data : "+ str(set(new_data)))
        print(len(new_data))
        # current data in cb
        current_data = sorted(set([self.cb_set_date.itemText(i) for i in range(self.cb_set_date.count())]))
        print("current date: "+ str(current_data))
        print(len(current_data))
        # get added data
        s = list(set(new_data) & set(current_data))
        print("Diff: "+ str(s))
        added_data = list(i for i in new_data if not (i in s))
        if len(new_data) == len(current_data):
            if len(s) == len(new_data):
                # no update, data is same
                pass
            else:
                print("Update date 1")
                # update cb
                self.insertCBDate(sorted(new_data))
        else:
            print("Update date 2")
            # update cb
            self.insertCBDate(sorted(new_data))
        # print(new_data)

    def insertCBDate(self, data):
        self.cb_set_date.clear()
        for i in range(len(data)):
            self.cb_set_date.addItem(data[i])
        self.cb_set_date.setCurrentIndex(0)

    def getData(self, data):
        global all_data, init_cb
        try:
            self.all_data=data
            data=json.loads(data)
            data_date=[]
            for i in range(len(data)):
                # Get PO NUMBER
                data_date.append(data[i]['date'])
            print(str(data_date))
            self.updateCBDate(data_date)
        except:
            print("Error in JSON parse")
            return
        all_data=data
        if(init_cb==False or self.updateF>-1):
            init_cb=True
            self.updateF-=1
            self.addWidget(self.cb_set_date.currentText(), all_data)    

    def logout(self):
        global JwToken, loginwin
        JwToken=''
        self.close()
        loginwin=Login()
        loginwin.show()

    def __init__(self, parent):
        global firstname, lastname
        global time_lbl, total_lbl, table_widget, data_line, line_cb
        global val_line23, val_line24, val_line25, val_line26, ready_setup, verticalLayoutWidget, scrollArea, verticalLayout
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)  # gets defined in the UI file
        self.pb_set_total.clicked.connect(self.set_total)
        self.parent = parent
        self.all_data=''
        self.updateF=0

        # loading text
        self.txt_loading.setVisible(False)
        self.txt_loading_logout.setVisible(False)
        self.pb_logout.clicked.connect(self.logout)

        self.txt_username.setText(str(firstname)+ ' '+ str(lastname))

        # Move to the center of window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # label
        time_lbl = self.lbl_time

        # Disable Edit
        self.groupBox.setEnabled(False)

        # Update
        self.pb_update.clicked.connect(self.update)
        self.lbl_total.setText("0")
        self.lbl_po.setText("0")
        self.cb_line.setText("-")
        self.cb_shift.setText("-")
        self.cb_set_date.currentIndexChanged.connect(self.setDate)

        # Update datetime
        now = datetime.now()
        now = now.strftime("%d %B %Y")
        yesterday = datetime.today() - timedelta(days=1)
        yesterday = yesterday.strftime("%d %B %Y")

        # Threading
        self.load_thread = MonitorLineDataThread(self)  # This is the thread object
        self.load_thread.start()

        #  ========= Setup for custom listview =========
        self.numAddWidget = 0
        verticalLayoutWidget = self.verticalLayoutWidget
        self.layoutV = self.verticalLayout
        scrollArea = self.scrollArea
        self.area = self.scrollArea
        self.area.setWidgetResizable(True)

        self.layoutH = QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QGridLayout()
        self.layoutH.addLayout(self.gridLayout)
        self.area.setWidget(self.scrollAreaWidgetContents)

        self.layoutV.addWidget(self.area)

        self.change_val.connect(self.change_val_)
        # Ready
        ready_setup = 1
        print("Initt")

# I feel better having one of these
def main():
    global mainwin, reworkwin, numpadwin, popupwin
    # a new app instance
    app = QApplication(sys.argv)
    # popupwin = Popup()
    # popupwin.show()
    login=Login()
    login.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# Create new thread for sending data every second
try:
    clockThread = clockThread()
except Exception as e:
    print("Error: unable to start thread!")
    print(str(e))
# Start thread
clockThread.start()

# python bit to figure how who started This
if __name__ == "__main__":
    main()
