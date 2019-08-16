# HTTP Request test
# http://samuelofficial.id/db/nabati_hmi_test_lanius/get_line_data.php
import requests

import threading

# always seem to need this
import sys
 
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

# Windows
mainwin=''
reworkwin=''
numpadwin=''
popupwin=''

# variables
style_succeed=("color: rgb(0, 79, 239);\nbackground-color: rgb(255, 255, 255);\nborder-color: rgb(0, 76, 229);\nfont: 75 10pt \"Arial\";")
style_waiting=("color: rgb(243, 243, 15);\nbackground-color: rgb(255, 255, 255);\nborder-color: rgb(243, 243, 15);\nfont: 75 10pt \"Arial\";")
style_failed=("color: rgb(255, 15, 15);\nbackground-color: rgb(255, 255, 255);\nborder-color: rgb(255, 15, 15);\nfont: 75 10pt \"Arial\";")
style_off=("color: rgb(255, 0, 0);\n"+"font: 75 17pt \"Arial\";\n"+"background-color: rgb(214, 214, 214);")
val_line_active=1
val_of_line=0
ready_setup=0
current_time=0
total_val=''
data_ready=False
numpad_f=0

# components
line_val=''
rework_val=''
val_line23=''
val_line24=''
val_line25=''
val_line26=''
time_lbl=''
numpad_val=''
total_lbl=''
table_widget=''
line_cb=''
lbl_line=''
verticalLayoutWidget=''
verticalLayout=''
scrollArea=''

# Python threads
clockThread=''

class clockThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        getLineData()

def getLineData():
    global current_time,time_lbl, ready_setup
    while 1:
        if ready_setup ==1:
            # Get current time
            current_time=time.localtime(time.time())
            time_now=[0]*3
            time_now[0]=str(current_time.tm_hour)
            time_now[1]=str(current_time.tm_min)
            time_now[2]=str(current_time.tm_sec)
            current_time=''
            for i in range(3):
                if len(time_now[i])==1:
                    time_now[i]='0'+time_now[i]
            current_time=time_now[0]+':'+time_now[1]+':'+time_now[2]
            time_lbl.setText(current_time)
            time.sleep(1)

class MonitorLineDataThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    def __init__(self):
        QThread.__init__(self)
    # run method gets called when we start the thread
    def run(self):
        global line_data, data_ready
        while 1:
            data_ready=False
            try:
                line_data = requests.get('http://samuelofficial.id/db/nabati_hmi_test_lanius/get_line_data.php', auth=('', ''))
                data_ready=True
                # Update line data
                update_table(line_data.text)
                # Update line list in cb
                update_cb_line_name()
            except:
                print("Error in connection!")
            time.sleep(1)
        self.signal.emit(line_data)

class LoadLineDataThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)

    # run method gets called when we start the thread
    def run(self):
        global line_data, data_ready
        data_ready=False
        while not data_ready:
            try:
                line_data = requests.get('http://samuelofficial.id/db/nabati_hmi_test_lanius/get_line_data.php', auth=('', ''))
                data_ready=True
            except:
                print("Error in connection!")
            time.sleep(1)
        self.signal.emit(line_data)

class Popup(QMainWindow, popup.Ui_Form):
    def load_finished(self, result):
        global mainwin
        # print(result)
        mainwin.show()
        self.close()

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
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


class Numpad(QMainWindow, numpad.Ui_Form):
    def pb_1_click(self):
        if(self.lbl_val.text()=='0'):
            self.lbl_val.setText('1')
        else:
            self.lbl_val.setText(self.lbl_val.text()+'1')
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
        val=self.lbl_val.text()
        if len(val)==1:
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
        self.setupUi(self) # gets defined in the UI file
        self.parent=parent
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
        self.lbl_val.setText(self.parent.val)
        self.lbl_line.setText(self.parent.line)


# create class for our Raspberry Pi GUI
class Rework(QMainWindow, rework.Ui_Form):
    change_val = pyqtSignal(int)
    def pb_set_rework_clicked(self):
        self.setEnabled(False)
        numpad_f=2
        self.val=self.rework_val.text()
        Numpad(self).show()

    def submit_rework(self):
        self.parent.setEnabled(True)
        selisih=int(self.parent.lbl_total.text())-int(self.rework_val.text())
        self.parent.lbl_total.setText(str(selisih))
        self.parent.parent.setEnabled(True)
        self.close()

    def exit_pb_clicked(self):
        self.parent.parent.setEnabled(True)
        self.close()

    def change_val_(self, val):
        self.rework_val.setText(str(val))

    def __init__(self, parent):
        global line_val,rework_val
        # QMainWindow.__init__(self, parent)
        super(self.__class__, self).__init__(parent)
        self.setupUi(self) # gets defined in the UI file
        # Move to the center of window
        # Move to the center of window
        print("Reworkkk")
        self.parent = parent
        self.line_val.setText(str(self.parent.line))
        self.line=self.line_val.text()
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
    s=list(set(new_data) & set(current_data))
    added_data = list(i for i in new_data if not (i in s))
    if len(new_data)==len(current_data):
        if len(s)==len(new_data):
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
data_line='[{"line":"Line 5", "total":"500"}, {"line":"Line 6", "total":"550"}]'

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
    rowPosition=0
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
    data=json.loads(data)
    for i in range(len(data)):
        # pass
        line=data[i]['line']
        total=data[i]['total']

        rowPosition = table_widget.rowCount()
        table_widget.insertRow(rowPosition)

        table_widget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(line))
        table_widget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(total))

data_line='[{"12 August 2019":[{"po":"PO 5", "shift":"1", "line":"Line 1", "total":"777"}], "11 August 2019":[{"po":"PO 1", "shift":"1", "line":"Line 1", "total":"500"}, {"po":"PO 2", "shift":"2", "line":"Line 2", "total":"550"}]}]'
class ExampleWidget2(QGroupBox):
    change_val=pyqtSignal(int)
    def __init__(self, numAddWidget, po, shift, total, line, parent, pb_set_total):
        QGroupBox.__init__(self)
        self.parent=parent
        self.parent.pb_update.clicked.connect(self.update)
        # self.change_val.connect(self.change_val__)
        # self.parent.pb_set_total.clicked.connect(self.set_total)
        self.pb_set_total=pb_set_total
        self.numAddWidget = numAddWidget
        self.po=po
        self.shift=shift
        self.total=total
        self.line=line
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
        self.parent.cb_shift.clear()
        self.parent.cb_line.clear()

    def edit(self):
        print(self.numAddWidget)
        self.parent.groupBox.setEnabled(True)
        self.parent.lbl_po.setText(self.po)
        self.parent.lbl_total.setText(self.lbl_total.text())
        self.parent.cb_shift.addItem(self.shift)
        self.parent.cb_line.addItem(self.line)
        MainWindow(self).change_val__(self)

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
        item = self.teachersselect.model().item(self.numAddItem-1, 0)
        item.setCheckState(Qt.Unchecked)

aaa=''
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
        idx=get_index(line_cb.currentText())
        total_lbl.setText(table_widget.item(idx, 1).text())
        lbl_line.setText(table_widget.item(idx, 0).text())

    def setDate(self):
        date_=self.cb_set_date.currentText()
        print(date_)
        self.addWidget(self.cb_set_date.currentText())
        # Reset edit group
        self.lbl_total.setText("0")
        self.lbl_po.setText("0")
        self.cb_shift.clear()
        self.cb_line.clear()
        self.groupBox.setEnabled(False)

    def change_val__(self, parent):
        global aaa
        aaa=parent
        self.parent=parent
        print(self.parent.lbl_total.text())

    def change_val_(self, val):
        self.lbl_total.setText(str(val))

    def update(self):
        global aaa
        print(aaa.lbl_total.text())
        aaa.lbl_total.setText(self.lbl_total.text())
        # self.lbl_total.setText()
        # ExampleWidget2(self.numAddWidget, self.po, self.shift, self.total, self.line, self, self.pb_set_total).change_val_(self.lbl_total.text())

    def set_total(self):
        self.setEnabled(False)
        self.val = self.lbl_total.text()
        Numpad(self).show()

    def addWidget(self, current_date):
        global data_line;
        # Insert new data
        data = json.loads(data_line)
        self.data_po=data
        self.data_po=self.data_po[0][current_date]

        print(self.data_po)
        # Delete all data
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

        # Insert data based on the date that is selected
        for i in range(len(self.data_po)):
            self.numAddWidget = i+1
            self.po = self.data_po[i]['po']
            self.shift=self.data_po[i]['shift']
            self.total = self.data_po[i]['total']
            self.line = self.data_po[i]['line']
            self.widget = ExampleWidget2(self.numAddWidget, self.po, self.shift, self.total, self.line, self, self.pb_set_total)
            self.gridLayout.addWidget(self.widget)

    # def update(self):
    #     self.groupBox.setEnabled(False)
    def __init__(self, parent):
        global time_lbl, total_lbl, table_widget, data_line, line_cb
        global val_line23,val_line24,val_line25,val_line26,ready_setup, verticalLayoutWidget, scrollArea, verticalLayout
        super(self.__class__, self).__init__(parent)
        self.setupUi(self) # gets defined in the UI file
        self.pb_set_total.clicked.connect(self.set_total)
        self.parent=parent
        # label
        time_lbl=self.lbl_time
        # total_lbl=self.lbl_total
        # line cb
        # line_cb=self.cb_line
        # line_cb.currentIndexChanged.connect(self.line_cb_changed)

        # Insert table widget dinamically
        # insert_table(data_line)
        # Insert line name to cb
        # insert_line_name_to_cb()
        # Update value
        # update_value('Line 1', "Hello")

        # Disable Edit
        self.groupBox.setEnabled(False)

        # Update
        self.pb_update.clicked.connect(self.update)
        self.lbl_total.setText("0")
        self.lbl_po.setText("0")
        self.cb_shift.clear()
        self.cb_line.clear()

        # Update datetime
        now = datetime.now()
        now = now.strftime("%d %B %Y")
        yesterday = datetime.today() - timedelta(days=1)
        yesterday = yesterday.strftime("%d %B %Y")
        # total_lbl.setText(str(yesterday))
        self.cb_set_date.clear()
        # print(data)
        self.cb_set_date.addItem(now)
        self.cb_set_date.addItem(yesterday)
        self.cb_set_date.setCurrentIndex(0)
        self.cb_set_date.currentIndexChanged.connect(self.setDate)

        # Threading
        self.load_thread = MonitorLineDataThread()  # This is the thread object
        # Connect the signal from the thread to the finished method
        # self.load_thread.signal.connect(self.monitor_finished)
        self.load_thread.start()

        #  ========= Setup for custom listview =========
        self.numAddWidget = 0
        verticalLayoutWidget=self.verticalLayoutWidget
        self.layoutV = self.verticalLayout
        scrollArea=self.scrollArea
        self.area=self.scrollArea
        self.area.setWidgetResizable(True)
        # scrollArea.setWidgetResizable(True)

        self.layoutH = QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QGridLayout()
        self.layoutH.addLayout(self.gridLayout)
        self.area.setWidget(self.scrollAreaWidgetContents)

        # self.add_button = QPushButton("Add Widget")
        self.layoutV.addWidget(self.area)

        # self.layoutV.addWidget(self.add_button)
        # self.add_button.clicked.connect(self.addWidget)
        self.addWidget(self.cb_set_date.currentText())

        self.change_val.connect(self.change_val_)
        # Ready
        ready_setup=1
        
# I feel better having one of these
def main():
    global mainwin,reworkwin, numpadwin, popupwin
    # a new app instance
    app = QApplication(sys.argv)
    mainwin = MainWindow(None)
    # reworkwin = Rework()
    # numpadwin = Numpad()
    popupwin = Popup()
    popupwin.show()
    # mainwin.show()
    # reworkwin.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())    

# Create new thread for sending data every second
try:
    clockThread=clockThread()
except Exception as e:
    print ("Error: unable to start thread!")
    print (str(e))
# Start thread
clockThread.start()

# python bit to figure how who started This
if __name__ == "__main__":
    main()
