# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mivista.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(481, 482)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../DjangoProjects/ReadingRoom/media/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color:#252525;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.run_button = QtGui.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(350, 140, 101, 101))
        self.run_button.setStyleSheet(_fromUtf8("background-color:#3677A9;\n"
"font-size:30px;\n"
"color:#e2e2e2;\n"
"font-family:courier;\n"
"border-radius:4px;\n"
"text-align:center;"))
        self.run_button.setObjectName(_fromUtf8("run_button"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 431, 51))
        self.label_2.setStyleSheet(_fromUtf8("color:#3677A9;\n"
"font-size:30px;\n"
"font-family:courier;\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 70, 361, 20))
        self.label_3.setStyleSheet(_fromUtf8("color:#3677A9;\n"
"font-size:20px;\n"
"font-family:courier;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.entrada = QtGui.QLineEdit(self.centralwidget)
        self.entrada.setGeometry(QtCore.QRect(30, 140, 291, 101))
        self.entrada.setStyleSheet(_fromUtf8("border:none;\n"
"background-color: #e2e2e2;\n"
"border-radius:5px;\n"
"font-size:60px;\n"
"color:#252525;\n"
"font-family:courier\n"
""))
        self.entrada.setText(_fromUtf8(""))
        self.entrada.setObjectName(_fromUtf8("entrada"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 361, 20))
        self.label_4.setStyleSheet(_fromUtf8("color:#3677A9;\n"
"font-size:20px;\n"
"font-family:courier;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.respuesta = QtGui.QTextEdit(self.centralwidget)
        self.respuesta.setGeometry(QtCore.QRect(30, 340, 421, 111))
        self.respuesta.setStyleSheet(_fromUtf8("background-color:#353535;\n"
"border:none;\n"
"border-radius:4px;\n"
"color:#e2e2e2;\n"
"font-size:18px;\n"
"font-family:courier"))
        self.respuesta.setObjectName(_fromUtf8("respuesta"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Genetic Arithmetic", None))
        self.run_button.setText(_translate("MainWindow", "Run ", None))
        self.label_2.setText(_translate("MainWindow", "Genetic Arithmetic", None))
        self.label_3.setText(_translate("MainWindow", "La genética de la aritmética", None))
        self.label_4.setText(_translate("MainWindow", "Información", None))

