#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
import sys
import socket
import GUI
import struct
from threading import Thread
import threading
import thread


def eth_addr (a):
	b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
	return b

def name_proto(proto):
	if proto == 1:
		return "ICMP";
	elif proto == 6:
		return "TCP";
	elif proto == 8:
		return "HEADER";
	elif proto == 17:
		return "UDP";
	else:
		return proto;


class Gui(QtGui.QWidget, GUI.Ui_GUI):
	def __init__(self, parent, ip, port):
		super(Gui, self).__init__(parent)
		self.daemon = True
		self.setupUi(self)
		self.init_Ui(ip, port)
		self.init()
		self.cancelled = False
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			print('Failed to create socket')
			sys.exit()

		print('Socket Created')

		try:
			# self.s.connect(('127.0.0.1', 1337))
                        print("'{}' '{}' >>{}".format(ip, port, type(ip)))                        
#                        self.s.connect(("195.154.71.44", 1337))
                        self.s.connect((ip, 1337))

		except socket.error:
			print('Failed to connect socket')

	def __exit__(self):
		self.cancel()
		self.close()

	def run(self):
		while not self.cancelled :
			packet = self.s.recv(1500)
			self.parse_packet(packet[16:])
		self.s.Close()

	def play(self):
                print("starting")
		self.s.send("start")
                thread.start_new_thread(self.run, ())

	def pause(self):
		self.s.send('stop')

	def cancel(self):
		"""End this timer thread"""
		self.cancelled = True
                
	def init_Ui(self, ip, port):
		# currentCellChanged ( int currentRow, int currentColumn, int previousRow, int previousColumn )
		# self.tableWidget.currentItemChanged.connect(self.affPacket)
		self.commandLinkButtonRunAnalyze.setText('Run Analyze on IP: ' + ip + ' with Port: ' + str(port))
		self.tableWidget.currentCellChanged.connect(self.affPacket)
		self.commandLinkButtonSendPacket.clicked.connect(self.sendPacket)
		self.commandLinkButtonRunAnalyze.clicked.connect(self.play)
		self.pushButtonInterrupt.clicked.connect(self.pause)
		self.pushButtonDeleteProbe.clicked.connect(self.__exit__)

	def init(self):
		self.packetList = list()
		self.packetNumber = 0
		# TEST
		#self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', 'ICIIIIIIIIIIIII'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '666'), ('Checksum', '666'), ('Data', 'DATA UQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDOHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZVUQDHGVVEZIUGRZV')])])
		# END OF TEST
		pass

	# refaire l'add avec les bonnes lists
	def addReceivedPacket(self, packet):
		try:
			self.packetNumber += 1
			packet[0]['ID'] = self.packetNumber
			self.packetList.append(packet)
			self.addPacketLine(packet[0])
		except:
			print("pass")
			pass
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
		headerItem.setText(header['Length'])
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
		if currentColumn == 11:
			print('prout')
			self.loadPacketToInjection(self.packetList[currentRow])
		else:
			# self.plainTextEdit.setPlainText(str(self.packetList[currentRow - 1][1]))
			text = str()
			for k,v in self.packetList[currentRow][1].items():
				text += k + ': ' + v + '\r\n'
			self.plainTextEdit.setPlainText(text)
		return

	def enableTCP(self, check=True):
		self.groupBoxTCPPart.setEnabled(check)
		self.labelSourcePort.setEnabled(check)
		self.labelDestinationPort.setEnabled(check)
		self.labelSequence.setEnabled(check)
		self.labelReconnaissance.setEnabled(check)
		self.labelHeaderTCP.setEnabled(check)
		self.lineEditSourcePort.setEnabled(check)
		self.lineEditDestinationPort.setEnabled(check)
		self.lineEditSequence.setEnabled(check)
		self.lineEditReconnaissance.setEnabled(check)
		self.lineEditHeaderTCP.setEnabled(check)
		return

	def enableUDP(self, check=True):
		self.groupBoxUDPPart.setEnabled(check)
		self.labelSourcePortUDP.setEnabled(check)
		self.labelDestinationPortUDP.setEnabled(check)
		self.labelSizeUDP.setEnabled(check)
		self.labelChecksumUDP.setEnabled(check)
		self.lineEditSourcePortUDP.setEnabled(check)
		self.lineEditDestinationPortUDP.setEnabled(check)
		self.lineEditSizeUDP.setEnabled(check)
		self.lineEditChecksumUDP.setEnabled(check)
		return

	def loadTCP(self, packet):
		self.lineEditSourcePort.setText(packet[1]['Source Port'])
		self.lineEditDestinationPort.setText(packet[1]['Destination Port'])
		self.lineEditSequence.setText(packet[1]['Sequence'])
		self.lineEditReconnaissance.setText(packet[1]['Reconnaissance'])
		self.lineEditHeaderTCP.setText(packet[1]['TCP Header'])
		return

	def loadUDP(self, packet):
		self.lineEditSourcePortUDP.setText(packet[1]['Source Port'])
		self.lineEditDestinationPortUDP.setText(packet[1]['Destination Port'])
		self.lineEditSizeUDP.setText(packet[1]['Size'])
		self.lineEditChecksumUDP.setText(packet[1]['Checksum'])
		return

	def loadHeader(self, packet):
		self.lineEditDate.setText(packet[0]['Date'])
		self.lineEditTime.setText(packet[0]['Time'])
		self.lineEditDate.setText(packet[0]['Date'])
		self.lineEditMacSource.setText(packet[0]['Mac Destination'])
		self.lineEditMacDestination.setText(packet[0]['Mac Source'])
		self.lineEditVersion.setText(packet[0]['Version'])
		self.lineEditHeaderLength.setText(packet[0]['Header Length'])
		self.lineEditTTL.setText(packet[0]['TTL'])
		self.lineEditProtocol.setText(packet[0]['Protocol'])
		self.lineEditIPSource.setText(packet[0]['IP Source'])
		self.lineEditIPDestination.setText(packet[0]['IP Destination'])
		return

	def loadPacketToInjection(self, packet):
		self.loadHeader(packet)
		if packet[0]['Protocol'] == 'TCP':
			self.enableTCP(True)
			self.enableUDP(False)
			self.loadTCP(packet)
		else:
			self.enableTCP(False)
			self.enableUDP(True)
			self.loadUDP(packet)

		document = QtGui.QTextDocument(self.plainTextEditData)
		document.setPlainText(packet[1]['Data'])
		documentLayout = QtGui.QPlainTextDocumentLayout(document)
		document.setDocumentLayout(documentLayout)
		self.plainTextEditData.setDocument(document)
		self.tabWidget.setCurrentIndex(1)
		return

	def sendPacket(self):
		# self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'TCP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Sequence', 'fyqgjczei'), ('Reconnaissance', 'bhvebrib'), ('TCP Header', 'uvhzyb'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		# self.addReceivedPacket([dict([('Date', '01-01-2015'), ('Time', '21-05-00'), ('Mac Source', '00:0a:95:9d:68:16'), ('Mac Destination', '00:0a:95:9d:68:72'), ('Version', '42'), ('Header Length', '666'), ('TTL', '13'), ('Protocol', 'UDP'), ('IP Source', '192.168.1.10'), ('IP Destination', '192.168.1.11')]), dict([('Source Port', '4242'), ('Destination Port', '3737'), ('Size', '55'), ('Checksum', '199'), ('Data', 'DATA UQDHGVVEZIUGRZV')])])
		packet = [dict([('', '')]), dict([('', '')])]
		packet[0]['Date'] = self.lineEditDate.text()
		packet[0]['Time'] = self.lineEditTime.text()
		packet[0]['Mac Destination'] = self.lineEditMacDestination.text()
		packet[0]['Mac Source'] = self.lineEditMacSource.text()
		packet[0]['Version'] = self.lineEditVersion.text()
		packet[0]['Header Length'] = self.lineEditHeaderLength.text()
		packet[0]['TTL'] = self.lineEditTTL.text()
		packet[0]['Protocol'] = self.lineEditProtocol.text()
		packet[0]['IP Source'] = self.lineEditIPSource.text()
		packet[0]['IP Destination'] = self.lineEditIPDestination.text()
		if self.groupBoxTCPPart.isEnabled():
			packet[1]['Source Port'] = self.lineEditSourcePort.text()
			packet[1]['Destination Port'] = self.lineEditDestinationPort.text()
			packet[1]['Sequence'] = self.lineEditSequence.text()
			packet[1]['Reconnaissance'] = self.lineEditReconnaissance.text()
			packet[1]['Header TCP'] = self.lineEditHeaderTCP.text()
		else:
			packet[1]['Source Port'] = self.lineEditSourcePortUDP.text()
			packet[1]['Destination Port'] = self.lineEditDestinationPortUDP.text()
			packet[1]['Size'] = self.lineEditSizeUDP.text()
			packet[1]['Checksum'] = self.lineEditChecksumUDP.text()
		document = self.plainTextEditData.document()
		packet[1]['Data'] = document.toPlainText()
		# puis envoie sur la socket
		return



	def parse_TCP(self, packet, iph_length, eth_length, l):
		t = iph_length + eth_length
		tcp_header = packet[t:t+20]

		TCPdict = {}

		tcph = struct.unpack('!HHLLBBHHH' , tcp_header)

		source_port = tcph[0]
		dest_port = tcph[1]
		sequence = tcph[2]
		acknowledgement = tcph[3]
		doff_reserved = tcph[4]
		tcph_length = doff_reserved >> 4

		TCPdict = {'PORT src':str(source_port), 'PORT dest':str(dest_port), 'Sequence':str(sequence), 'Acknowledgement':str(acknowledgement), 'TCP header length':str(tcph_length)}
		l.append(TCPdict)

		h_size = eth_length + iph_length + tcph_length * 4
		data_size = len(packet) - h_size

		data = packet[h_size:]
		TCPdict['DATA'] = data
		l.append(TCPdict)
		return

	def parse_ICMP(self, packet, iph_length, eth_length, l):
		u = iph_length + eth_length
		icmph_length = 4
		icmp_header = packet[u:u+4]

		ICMPdict = {}

		icmph = struct.unpack('!BBH' , icmp_header)

		icmp_type = icmph[0]
		code = icmph[1]
		checksum = icmph[2]

		ICMPdict = {'TYPE':str(icmp_type), 'Code':str(code), 'Checksum':str(checksum)}

		h_size = eth_length + iph_length + icmph_length
		data_size = len(packet) - h_size

		data = packet[h_size:]
		ICMPdict['DATA'] = data
		l.append(ICMPdict)
		return
                
	def parse_UDP(self, packet, iph_length, eth_length, l):
		u = iph_length + eth_length
		udph_length = 8
		udp_header = packet[u:u+8]
		UDPdict = {}

		udph = struct.unpack('!HHHH' , udp_header)

		source_port = udph[0]
		dest_port = udph[1]
		length = udph[2]
		checksum = udph[3]
		UDPdict = {'PORT src':str(source_port), 'PORT dest':str(dest_port), 'Length':str(length), 'Checksum':str(checksum)}      

		h_size = eth_length + iph_length + udph_length
		data_size = len(packet) - h_size

		data = packet[h_size:]
		UDPdict['data'] = data
		l.append(UDPdict)
		return

	def parse_packet(self, packet):

		print(len(packet))
		if(len(packet)) < 16:
			return
		l = []
		headerdict = {}

		eth_length = 14
		eth_header = packet[:eth_length]
		eth = struct.unpack('!6s6sH' , eth_header)
		eth_protocol = socket.ntohs(eth[2])

		print('proto - ' + str(eth_protocol))

		if eth_protocol == 8:
			print('proto 8')
			ip_header = packet[eth_length:20+eth_length]
			iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)
 
			version_ihl = iph[0]
			version = version_ihl >> 4
			ihl = version_ihl & 0xF
			iph_length = ihl * 4

			ttl = iph[5]
			protocol = iph[6]
			s_addr = socket.inet_ntoa(iph[8]);
			d_addr = socket.inet_ntoa(iph[9]);

			headerdict = {'Date':'date', 'Time':'time', 'Mac Destination':eth_addr(packet[0:6]), 'Mac Source':eth_addr(packet[6:12]), 'header protocol':name_proto(eth_protocol), 'Version':str(version), 'IPH':str(ihl), 'Length':str("24"), 'TTL':str(ttl), 'Protocol':name_proto(protocol), 'IP Source':str(s_addr), 'IP Destination':str(d_addr)}
			l.append(headerdict)

			if protocol == 6: #Protocol = 6 (TCP)
				self.parse_TCP(packet, iph_length, eth_length, l)        
			elif protocol == 1: #Protocol = 1 (ICMP)
				self.parse_ICMP(packet, iph_length, eth_length, l)        
			elif protocol == 17: #Protocol = 1 (UDP)
				self.parse_UDP(packet, iph_length, eth_length, l)

                        print(l)
                        self.addReceivedPacket(l)
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

		self.connectNewProb = QtGui.QGroupBox(self.window)
		self.connectNewProb.setTitle('New Probe Connection')
		self.connectNewProb.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)#horizontal/vertical
		self.hLayoutGroupBox = QtGui.QHBoxLayout()#self.connectNewProb

		self.labelNewIPProb = QtGui.QLabel()
		self.labelNewIPProb.setText('IP:')
		self.labelNewIPProb.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		self.lineEditNewIPProb = QtGui.QLineEdit(self.connectNewProb)
		self.lineEditNewIPProb.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		self.labelNewPortProb = QtGui.QLabel(self.connectNewProb)
		self.labelNewPortProb.setText('Port:')
		self.labelNewPortProb.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		self.lineEditNewPortProb = QtGui.QLineEdit(self.connectNewProb)
		self.lineEditNewPortProb.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		
		self.commandLinkButtonNewProb = QtGui.QCommandLinkButton()
		self.commandLinkButtonNewProb.setText('Create New Connection')
		self.commandLinkButtonNewProb.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		self.commandLinkButtonNewProb.clicked.connect(self.createNewTab)
		# 		self.tableWidget.currentCellChanged.connect(self.affPacket)


		self.labelNewIPProbAdjust = QtGui.QLabel()

		self.hLayoutGroupBox.addWidget(self.labelNewIPProb)
		self.hLayoutGroupBox.addWidget(self.lineEditNewIPProb)
		self.hLayoutGroupBox.addWidget(self.labelNewPortProb)
		self.hLayoutGroupBox.addWidget(self.lineEditNewPortProb)
		self.hLayoutGroupBox.addWidget(self.commandLinkButtonNewProb)
		self.hLayoutGroupBox.addWidget(self.labelNewIPProbAdjust)
		self.connectNewProb.setLayout(self.hLayoutGroupBox)

		self.tabProb = QtGui.QTabWidget(self.window)
		self.tabProb.setTabPosition(QtGui.QTabWidget.West)
		self.tabProb.setTabsClosable(True)
		self.tabProb.tabCloseRequested.connect(self.closeTab)

		self.tabList = list()
		# self.createNewTab()
		# self.createNewTab()
		# self.createNewTab()
		# self.createNewTab()
		# self.createNewTab()
		# self.createNewTab()

		self.mainLayout = QtGui.QVBoxLayout()
		self.mainLayout.setMenuBar(self.menuBar)
		self.mainLayout.addWidget(self.connectNewProb)
		self.mainLayout.addWidget(self.tabProb)

		self.window.setLayout(self.mainLayout)

	def closeTab(self, index):
		self.tabList[index - 1].__exit__()
		self.tabProb.removeTab(index)

	def createNewTab(self):
		ip = self.lineEditNewIPProb.text()
		port = len(self.lineEditNewPortProb.text())
		if self.lineEditNewPortProb.text() == '' or self.lineEditNewPortProb.text() == '':
			return
		g = Gui(self.tabProb, ip, port)
		self.tabList.append(g)
		self.tabProb.addTab(self.tabList[len(self.tabList) - 1], 'Probe' + str(len(self.tabList)))

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
