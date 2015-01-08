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
import binascii

from dpkt.ip import IP
from dpkt.tcp import TCP
from dpkt.udp import UDP
from dpkt.ethernet import Ethernet

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
	def __init__(self, parent, ip='127.0.0.1', port=4242):
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
                        self.s.connect((ip, port))

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
		self.commandLinkButtonRunAnalyze.setText('Run Analyze on IP: [' + ip + ':' + str(port)+']')
		self.tableWidget.currentCellChanged.connect(self.affPacket)
		self.commandLinkButtonSendPacket.clicked.connect(self.sendPacket)
		self.commandLinkButtonRunAnalyze.clicked.connect(self.play)
		self.pushButtonInterrupt.clicked.connect(self.pause)
		self.pushButtonDeleteProbe.clicked.connect(self.__exit__)

	def init(self):
		self.packetList = list()
		self.packetNumber = 0
		# TEST
		# END OF TEST
		pass

	def addReceivedPacket(self, packet):
		try:
			self.packetNumber += 1
			packet[0]['ID'] = self.packetNumber
			self.packetList.append(packet)
			if self.comboBoxFilter.currentText() == 'All':
				self.addPacketLine(packet[0])
			elif self.comboBoxFilter.currentText() == 'TCP' and packet[0]['Protocol'] == 'TCP':
				self.addPacketLine(packet[0])
			elif self.comboBoxFilter.currentText() == 'UDP' and packet[0]['Protocol'] == 'UDP':
				self.addPacketLine(packet[0])
		except:
			print("pass")
			pass
		return

	def addPacketLine(self, header):
		idItem = QtGui.QTableWidgetItem()
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

		timeItem.setText(header['Time'])
		macSItem.setText(header['Mac Source'])
		macDItem.setText(header['Mac Destination'])
		versionItem.setText(header['Version'])
		headerItem.setText(header['Header Length'])
		ttlItem.setText(header['TTL'])
		protocolItem.setText(header['Protocol'])
		ipSItem.setText(header['IP Source'])
		ipDItem.setText(header['IP Destination'])

		injectItem.setText('Click here to modify this packet with the ID: ' + str(header['ID']))
		# img = QtGui.QImage();
		# img.load('go_button_icon_logo.jpg');
		# injectItem.setData(QtCore.Qt.DecorationRole, QtGui.QPixmap.fromImage(img))

		self.tableWidget.setItem(header['ID'] - 1, 0, timeItem)
		self.tableWidget.setItem(header['ID'] - 1, 1, macSItem)
		self.tableWidget.setItem(header['ID'] - 1, 2, macDItem)
		self.tableWidget.setItem(header['ID'] - 1, 3, versionItem)
		self.tableWidget.setItem(header['ID'] - 1, 4, headerItem)
		self.tableWidget.setItem(header['ID'] - 1, 5, ttlItem)
		self.tableWidget.setItem(header['ID'] - 1, 6, protocolItem)
		self.tableWidget.setItem(header['ID'] - 1, 7, ipSItem)
		self.tableWidget.setItem(header['ID'] - 1, 8, ipDItem)
		self.tableWidget.setItem(header['ID'] - 1, 9, injectItem)
		return

	# current/previous QTableWidgetItem
	def affPacket(self, currentRow, currentColumn, previousRow, previousColumn):
		if currentColumn == 9:
			self.loadPacketToInjection(self.packetList[currentRow])
		else:
			# self.plainTextEdit.setPlainText(str(self.packetList[currentRow - 1][1])) 195.154.71.44
			text = str()
			for k,v in self.packetList[currentRow][1].items():
				if k == 'Data' or k == 'DATA' or k == 'data':
					try:
						# text += k + ':' + hex(int(v, 2)) + '\r\n'
						text += k + ': ' + binascii.hexlify(v) + '\r\n'
					except:
						print('[ERROR] Data is not a binary code')
						text += '[ERROR] Data is not a binary code. Simple show' + ': ' + v + ' \r\n'
				else:
					text += k + ': ' + v + ' \r\n'
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
		self.lineEditReconnaissance.setText(packet[1]['Acknowledgement'])
		self.lineEditHeaderTCP.setText(packet[1]['TCP Header Length'])
		return

	def loadUDP(self, packet):
		self.lineEditSourcePortUDP.setText(packet[1]['Source Port'])
		self.lineEditDestinationPortUDP.setText(packet[1]['Destination Port'])
		self.lineEditSizeUDP.setText(packet[1]['Size'])
		self.lineEditChecksumUDP.setText(packet[1]['Checksum'])
		return

	def loadHeader(self, packet):
		self.lineEditTime.setText(packet[0]['Time'])
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
		document.setPlainText(binascii.unhexlify(document.toPlainText()))
		documentLayout = QtGui.QPlainTextDocumentLayout(document)
		document.setDocumentLayout(documentLayout)
		self.plainTextEditData.setDocument(document)
		self.tabWidget.setCurrentIndex(1)
		return

	def sendPacket(self):
		packet = [{}, {}]

                p = Ethernet()
		packet[0]['Mac Destination'] = self.lineEditMacDestination.text()
		packet[0]['Mac Source'] = self.lineEditMacSource.text()

                p.dst = binascii.unhexlify("".join(packet[0]['Mac Destination'].split(':')))
                p.src = binascii.unhexlify("".join(packet[0]['Mac Source'].split(":")))
                p.data = IP()
                p.type = 0x0800

                print(p)

                packet[0]['Time'] = self.lineEditTime.text()
		packet[0]['Version'] = int(self.lineEditVersion.text())
		packet[0]['Header Length'] = int(self.lineEditHeaderLength.text())
		packet[0]['TTL'] = int(self.lineEditTTL.text())
		packet[0]['Protocol'] = self.lineEditProtocol.text()
		packet[0]['IP Source'] = self.lineEditIPSource.text()
		packet[0]['IP Destination'] = self.lineEditIPDestination.text()

                p.data.ttl = packet[0]['TTL']
 
                p.data.src=socket.inet_aton(packet[0]['IP Source'])
                p.data.dst=socket.inet_aton(packet[0]['IP Destination'] )

                
                if self.groupBoxTCPPart.isEnabled():
                        payload = TCP()
                        packet[1]['Source Port'] = int(self.lineEditSourcePort.text())
                        payload.seq = int(self.lineEditSequence.text())
                        packet[1]['Destination Port'] = int(self.lineEditDestinationPort.text())
                        packet[1]['Sequence'] = self.lineEditSequence.text()
                        packet[1]['Reconnaissance'] = self.lineEditReconnaissance.text()
                        packet[1]['Header TCP'] = self.lineEditHeaderTCP.text()
                elif self.groupBoxUDPPart.isEnabled():
                        payload = UDP()
                        packet[1]['Source Port'] = int(self.lineEditSourcePortUDP.text())
                        packet[1]['Destination Port'] = int(self.lineEditDestinationPortUDP.text())
                        packet[1]['Header Length'] = int(self.lineEditSizeUDP.text())
                        packet[1]['Checksum'] = hex(self.lineEditChecksumUDP.text())
                document = self.plainTextEditData.document()
                payload.data = document.toPlainText()
                payload.dport = packet[1]['Source Port']
                payload.sport = packet[1]['Destination Port']
                        
                        
#                except:
#                        print("error")
#                        pass
                self.s.send("INJECT"+str(p))

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
		h_size = eth_length + iph_length + tcph_length * 4
		data_size = len(packet) - h_size

		TCPdict = {'Source Port':str(source_port), 'Destination Port':str(dest_port), 'Sequence':str(sequence), 'Acknowledgement':str(acknowledgement), 'TCP Header Length':str(data_size)}

		data = packet[h_size:]
		TCPdict['Data'] = data
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

		h_size = eth_length + iph_length + udph_length
		data_size = len(packet) - h_size

		UDPdict = {'Source Port':str(source_port), 'Destination Port':str(dest_port), 'Header Length':str(length), 'Checksum':str(checksum), "Size":str(data_size)}      

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

			headerdict = {'Time':'time', 'Mac Destination':eth_addr(packet[0:6]), 'Mac Source':eth_addr(packet[6:12]), 'header protocol':str(name_proto(eth_protocol)), 'Version':str(version), 'IPH':str(ihl), 'Header Length':str("24"), 'TTL':str(ttl), 'Protocol':str(name_proto(protocol)), 'IP Source':str(s_addr), 'IP Destination':str(d_addr)}
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
		port = int(self.lineEditNewPortProb.text())
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
