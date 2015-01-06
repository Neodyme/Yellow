#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
import sys

import GUI

class Gui(QtGui.QWidget, GUI.Ui_GUI):
	def __init__(self, parent=None):
		super(Gui, self).__init__(parent)
		self.setupUi(self)
		self.init()

	def init(self):
		self.packetList = list()
		self.tableWidget.currentItemChanged.connect(self.affPacket)
		self.packetList.append(['1', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test', 'Info Test Line', 'Packet Content 1'])
		self.packetList.append(['2', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test 2', 'Info Test Line 2', 'Packet Content 2'])
		self.packetList.append(['3', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test 3', 'Info Test Line 3', 'Packet Content 3'])
		self.packetList.append(['4', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test 4', 'Info Test Line 4', 'Packet Content 4'])
		self.packetList.append(['5', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test 5', 'Info Test Line 5', 'Packet Content 5'])
		self.packetList.append(['6', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test 6', 'Info Test Line 6', 'Packet Content 6'])
		self.packetList.append(['7', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test 7', 'Info Test Line 7', 'Packet Content 7'])
		self.packetList.append(['8', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test 8', 'Info Test Line 8', 'Packet Content 8'])
		self.packetList.append(['9', '01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test 9', 'Info Test Line 9', 'Packet Content 9'])
		self.packetNumber = len(self.packetList)
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		self.addReceivedPacket(['01-01-2015', '127.0.0.1', '127.0.0.1', 'Protocol Test uytuyhkj', 'Info Test Line HGIUG', 'Packet Content KJHGFCHGVJ'])
		for i in range(self.packetNumber):
			self.addPacketLine(self.packetList[i][0], self.packetList[i][1], self.packetList[i][2], self.packetList[i][3], self.packetList[i][4], self.packetList[i][5])
		pass

	def addReceivedPacket(self, packet):
		self.packetNumber += 1
		packet.insert(0, str(self.packetNumber))
		self.packetList.append(packet)
		# ajoute le paquet dans self.packetList, dans la dernière cellule non visible, et remplir les précédentes pour le résumé pour le stocker -> A voir avec Fred en fonction de comment il recoit et m'envoie les infos
		pass

	def addPacketLine(self, number, time, source, destination, protocol, info):
		timeItem = QtGui.QTableWidgetItem()
		sourceItem = QtGui.QTableWidgetItem()
		destinationItem = QtGui.QTableWidgetItem()
		protocolItem = QtGui.QTableWidgetItem()
		infoItem = QtGui.QTableWidgetItem()
		self.tableWidget.insertRow(int(number) - 1)

		timeItem.setText(time)
		sourceItem.setText(source)
		destinationItem.setText(destination)
		protocolItem.setText(protocol)
		infoItem.setText(info)
		self.tableWidget.setItem(int(number) - 1, 0, timeItem)
		self.tableWidget.setItem(int(number) - 1, 1, sourceItem)
		self.tableWidget.setItem(int(number) - 1, 2, destinationItem)
		self.tableWidget.setItem(int(number) - 1, 3, protocolItem)
		self.tableWidget.setItem(int(number) - 1, 4, infoItem)
		pass

	# current/previous QTableWidgetItem
	def affPacket(self, current, previous):
		for i in range(self.packetNumber):
			if current.text() == self.packetList[i][5]:
				self.plainTextEdit.setPlainText(self.packetList[i][6])
		pass

class MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)		
		self.createMenu()
		self.init_Ui()

	def init_Ui(self):
		self.resize(1080,720)
		# self.showMaximized()
		self.setWindowTitle('WireShark Remake')

		self.window = QtGui.QWidget()
		self.setCentralWidget(self.window)
		self.window.showMaximized()


		self.tabProb = QtGui.QTabWidget(self.window)
		self.tabProb.setTabPosition(QtGui.QTabWidget.West)

		self.tabList = list()
		self.createNewTab()
		self.createNewTab()
		self.createNewTab()
		self.createNewTab()
		self.createNewTab()
		self.createNewTab()

		self.mainLayout = QtGui.QVBoxLayout()
		self.mainLayout.setMenuBar(self.menuBar)
		self.mainLayout.addWidget(self.tabProb)

		self.window.setLayout(self.mainLayout)

	def createNewTab(self):
		self.tabList.append(Gui(self.tabProb))
		self.tabProb.addTab(self.tabList[len(self.tabList) - 1], 'Prob' + str(len(self.tabList)))


	def createMenu(self):
		self.menuBar = QtGui.QMenuBar()
 
		self.fileMenu = QtGui.QMenu("&File", self)
		self.exitAction = self.fileMenu.addAction("&Exit")
		self.menuBar.addMenu(self.fileMenu)
 
		self.exitAction.triggered.connect(self.close)

	def contextMenuEvent(self, event):
		pass
		# QContextMenuEvent

def main(argv):
	app = QtGui.QApplication(argv)

	mwindow = MainWindow()

	mwindow.show()

	# ici intanciation des sockets (ou avant peu importe)
	# puis la reception de packets qui appelleront alors addReceivedPacket
	# puis le clique sur la ligne créée du packet appellera affPacket avec en parametre le numero du packet recus, et l'affichera dans la zone indiqué
	return app.exec_()

if __name__=='__main__':
    if len(sys.argv) >= 1:
        main(sys.argv)
    else:
        print('Usage: python GUI')