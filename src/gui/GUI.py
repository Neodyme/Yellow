# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Mon Jan  5 17:36:37 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(652, 689)
        self.tabWidget = QtGui.QTabWidget(GUI)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 631, 671))
        self.tabWidget.setObjectName("tabWidget")
        self.AnalyzeTraffic = QtGui.QWidget()
        self.AnalyzeTraffic.setObjectName("AnalyzeTraffic")
        self.scrollArea = QtGui.QScrollArea(self.AnalyzeTraffic)
        self.scrollArea.setGeometry(QtCore.QRect(-10, -10, 631, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 621, 641))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtGui.QLabel(self.AnalyzeTraffic)
        self.label.setGeometry(QtCore.QRect(0, 530, 81, 16))
        self.label.setObjectName("label")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.AnalyzeTraffic)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 550, 621, 91))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.AnalyzeTraffic, "")
        self.PacketsModifications = QtGui.QWidget()
        self.PacketsModifications.setObjectName("PacketsModifications")
        self.tabWidget.addTab(self.PacketsModifications, "")

        self.retranslateUi(GUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        GUI.setWindowTitle(QtGui.QApplication.translate("GUI", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("GUI", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("GUI", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("GUI", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("GUI", "Protocol", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("GUI", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GUI", "Packet Content", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnalyzeTraffic), QtGui.QApplication.translate("GUI", "Analyze Traffic", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PacketsModifications), QtGui.QApplication.translate("GUI", "Packets Modifications", None, QtGui.QApplication.UnicodeUTF8))

