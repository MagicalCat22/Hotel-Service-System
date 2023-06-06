# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime,QTimer,Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1278, 712)
       
        self.lable_title = QtWidgets.QLabel(Form)
        self.lable_title.setGeometry(QtCore.QRect(400, 90, 1000, 100))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lable_title.setFont(font)
        self.lable_title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lable_title.setMouseTracking(False)
        self.lable_title.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lable_title.setAcceptDrops(False)
        self.lable_title.setObjectName("lable_title")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(610, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        self.pushButton1.setFont(font)
        self.pushButton1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton1.setAcceptDrops(False)
        self.pushButton1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton1.setObjectName("pushButton1")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(530, 460, 256, 121))
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(12)
        self.say_label = QtWidgets.QLabel(Form)
        self.say_label.setFont(font)
        self.say_label.setGeometry(QtCore.QRect(512, 370, 300, 31))
        self.say_label.setObjectName("say_label")
        self.input_label = QtWidgets.QLabel(Form)
        self.input_label.setGeometry(QtCore.QRect(800, 470, 441, 27))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.input_label.setFont(font)
        self.input_label.setObjectName("input_label")
        self.decode_label = QtWidgets.QLabel(Form)
        self.decode_label.setGeometry(QtCore.QRect(800, 550, 441, 27))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.decode_label.setFont(font)
        self.decode_label.setObjectName("decode_label")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(450, 230, 61, 41))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(480, 280, 400, 41))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(480, 320, 301, 41))
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.time_label = QtWidgets.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(950, 680, 500, 31))
        self.time_label.setObjectName("time_label")
        self.time_label.setFont(QFont('DFKai-SB', 16))

        self.Timer=QTimer()
        self.Timer.start()
        self.Timer.timeout.connect(self.timeupdate)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.pushButton1, self.textBrowser)
    def timeupdate(self):
        self.time_label.setText(QDateTime.currentDateTime().toString('yyyy年MM月dd日 hh:mm:ss'))
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lable_title.setText(_translate("Form", "AI旅館服務系統"))
        self.pushButton1.setText(_translate("Form", "開始"))
        self.input_label.setText(_translate("Form", "輸入"))
        self.decode_label.setText(_translate("Form", "解碼"))
        self.label.setText(_translate("Form", "模式"))
        self.label_2.setText(_translate("Form", "1.我要訂(數量)+(房間)+(日期)"))
        self.label_3.setText(_translate("Form", "2.我要(食物)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

