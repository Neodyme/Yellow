#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
import sys

import GUI

class Gui(QtGui.QWidget, GUI.Ui_GUI):
	def __init__(self, parent=None):
		super(Gui, self).__init__(parent)
		self.setupUi(self)
		self.init_Ui()
		self.init()

	def init_Ui(self):
		# currentCellChanged ( int currentRow, int currentColumn, int previousRow, int previousColumn )
		# self.tableWidget.currentItemChanged.connect(self.affPacket)
		self.tableWidget.currentCellChanged.connect(self.affPacket)

	def init(self):
		self.packetList = list()
		self.packetNumber = 0

		# TEST
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV PREV')])])
		self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', 'ICIIIIIIIIIIIII'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '666'), ('Checksum', '666'), ('Data', 'DATA UQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZV')])])
		# END OF TEST
		pass

	# refaire l'add avec les bonnes lists
	def addReceivedPacket(self, packet):
		self.packetNumber += 1
		packet[0]['ID'] = self.packetNumber
		self.packetList.append(packet)
		self.addPacketLine(packet[0])
		
		# TEST
		# "\r\n"
		# TCP REF = [dict([('ID', 1), ('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])]
		# UDP REF = [dict([('ID', 2), ('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])]
		# END OF TEST
		return

	def addPacketLine(self, header):
		idItem = QtGui.QTableWidgetItem()
		dateItem = QtGui.QTableWidgetItem()
		timeItem = QtGui.QTableWidgetItem()
		macSItem = QtGui.QTableWidgetItem()
		macDItem = QtGui.QTableWidgetItem()
		versionItem = QtGui.QTableWidgetItem()
		headerItem = QtGui.QTableWidgetItem()
		ttlItem = QtGui.QTableWidgetItem()
		protocolItem = QtGui.QTableWidgetItem()
		ipSItem = QtGui.QTableWidgetItem()
		ipDItem = QtGui.QTableWidgetItem()
		injectItem = QtGui.QTableWidgetItem()
		self.tableWidget.insertRow(header['ID'] - 1)

		idItem.setText(str(header['ID']))
		dateItem.setText(header['Date'])
		timeItem.setText(header['Time'])
		macSItem.setText(header['Mac Source'])
		macDItem.setText(header['Mac Destination'])
		versionItem.setText(header['Version'])
		headerItem.setText(header['Header Length'])
		ttlItem.setText(header['TTL'])
		protocolItem.setText(header['Protocol'])
		ipSItem.setText(header['IP Source'])
		ipDItem.setText(header['IP Destination'])
		# injectItem.setText('Click here to modify this packet with the ID: ' + str(header['ID']))
		img = QtGui.QImage();
		img.load('go_button_icon_logo.jpg');
		injectItem.setData(QtCore.Qt.DecorationRole, QtGui.QPixmap.fromImage(img))


		self.tableWidget.setItem(header['ID'] - 1, 0, idItem)
		self.tableWidget.setItem(header['ID'] - 1, 1, dateItem)
		self.tableWidget.setItem(header['ID'] - 1, 2, timeItem)
		self.tableWidget.setItem(header['ID'] - 1, 3, macSItem)
		self.tableWidget.setItem(header['ID'] - 1, 4, macDItem)
		self.tableWidget.setItem(header['ID'] - 1, 5, versionItem)
		self.tableWidget.setItem(header['ID'] - 1, 6, headerItem)
		self.tableWidget.setItem(header['ID'] - 1, 7, ttlItem)
		self.tableWidget.setItem(header['ID'] - 1, 8, protocolItem)
		self.tableWidget.setItem(header['ID'] - 1, 9, ipSItem)
		self.tableWidget.setItem(header['ID'] - 1, 10, ipDItem)
		self.tableWidget.setItem(header['ID'] - 1, 11, injectItem)
		return

	# current/previous QTableWidgetItem
	def affPacket(self, currentRow, currentColumn, previousRow, previousColumn):
		if currentColumn == 10:
			self.loadPacketToInjection(self.packetList[currentRow - 1])
		else:
			# self.plainTextEdit.setPlainText(str(self.packetList[currentRow - 1][1]))
			text = str()
			for k,v in self.packetList[currentRow][1].items():
				text += k + ': ' + v + '\r\n'
			self.plainTextEdit.setPlainText(text)
		return

	def loadPacketToInjection(self, packet):
		return

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