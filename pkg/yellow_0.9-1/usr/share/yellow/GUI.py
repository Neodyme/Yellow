# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Wed Jan  7 18:42:32 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(895, 850)
        self.gridLayout_2 = QtGui.QGridLayout(GUI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxPackets = QtGui.QGroupBox(GUI)
        self.groupBoxPackets.setObjectName("groupBoxPackets")
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBoxPackets)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabWidget = QtGui.QTabWidget(self.groupBoxPackets)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 800))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.AnalyzeTraffic = QtGui.QWidget()
        self.AnalyzeTraffic.setObjectName("AnalyzeTraffic")
        self.gridLayout = QtGui.QGridLayout(self.AnalyzeTraffic)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtGui.QTableWidget(self.AnalyzeTraffic)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
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
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.AnalyzeTraffic)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.AnalyzeTraffic)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.tabWidget.addTab(self.AnalyzeTraffic, "")
        self.PacketsModifications = QtGui.QWidget()
        self.PacketsModifications.setObjectName("PacketsModifications")
        self.gridLayout_3 = QtGui.QGridLayout(self.PacketsModifications)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtGui.QScrollArea(self.PacketsModifications)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 383, 673))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBoxUDPPart = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxUDPPart.setObjectName("groupBoxUDPPart")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBoxUDPPart)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.labelSourcePortUDP = QtGui.QLabel(self.groupBoxUDPPart)
        self.labelSourcePortUDP.setObjectName("labelSourcePortUDP")
        self.gridLayout_7.addWidget(self.labelSourcePortUDP, 0, 0, 1, 1)
        self.lineEditSourcePortUDP = QtGui.QLineEdit(self.groupBoxUDPPart)
        self.lineEditSourcePortUDP.setObjectName("lineEditSourcePortUDP")
        self.gridLayout_7.addWidget(self.lineEditSourcePortUDP, 0, 1, 1, 1)
        self.lineEditSizeUDP = QtGui.QLineEdit(self.groupBoxUDPPart)
        self.lineEditSizeUDP.setObjectName("lineEditSizeUDP")
        self.gridLayout_7.addWidget(self.lineEditSizeUDP, 2, 1, 1, 1)
        self.lineEditChecksumUDP = QtGui.QLineEdit(self.groupBoxUDPPart)
        self.lineEditChecksumUDP.setObjectName("lineEditChecksumUDP")
        self.gridLayout_7.addWidget(self.lineEditChecksumUDP, 3, 1, 1, 1)
        self.lineEditDestinationPortUDP = QtGui.QLineEdit(self.groupBoxUDPPart)
        self.lineEditDestinationPortUDP.setObjectName("lineEditDestinationPortUDP")
        self.gridLayout_7.addWidget(self.lineEditDestinationPortUDP, 1, 1, 1, 1)
        self.labelDestinationPortUDP = QtGui.QLabel(self.groupBoxUDPPart)
        self.labelDestinationPortUDP.setObjectName("labelDestinationPortUDP")
        self.gridLayout_7.addWidget(self.labelDestinationPortUDP, 1, 0, 1, 1)
        self.labelSizeUDP = QtGui.QLabel(self.groupBoxUDPPart)
        self.labelSizeUDP.setObjectName("labelSizeUDP")
        self.gridLayout_7.addWidget(self.labelSizeUDP, 2, 0, 1, 1)
        self.labelChecksumUDP = QtGui.QLabel(self.groupBoxUDPPart)
        self.labelChecksumUDP.setObjectName("labelChecksumUDP")
        self.gridLayout_7.addWidget(self.labelChecksumUDP, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxUDPPart, 2, 0, 1, 1)
        self.groupBoxTCPPart = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxTCPPart.setObjectName("groupBoxTCPPart")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBoxTCPPart)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEditSequence = QtGui.QLineEdit(self.groupBoxTCPPart)
        self.lineEditSequence.setObjectName("lineEditSequence")
        self.gridLayout_6.addWidget(self.lineEditSequence, 2, 1, 1, 1)
        self.lineEditSourcePort = QtGui.QLineEdit(self.groupBoxTCPPart)
        self.lineEditSourcePort.setObjectName("lineEditSourcePort")
        self.gridLayout_6.addWidget(self.lineEditSourcePort, 0, 1, 1, 1)
        self.lineEditDestinationPort = QtGui.QLineEdit(self.groupBoxTCPPart)
        self.lineEditDestinationPort.setObjectName("lineEditDestinationPort")
        self.gridLayout_6.addWidget(self.lineEditDestinationPort, 1, 1, 1, 1)
        self.labelSourcePort = QtGui.QLabel(self.groupBoxTCPPart)
        self.labelSourcePort.setObjectName("labelSourcePort")
        self.gridLayout_6.addWidget(self.labelSourcePort, 0, 0, 1, 1)
        self.labelDestinationPort = QtGui.QLabel(self.groupBoxTCPPart)
        self.labelDestinationPort.setObjectName("labelDestinationPort")
        self.gridLayout_6.addWidget(self.labelDestinationPort, 1, 0, 1, 1)
        self.labelSequence = QtGui.QLabel(self.groupBoxTCPPart)
        self.labelSequence.setObjectName("labelSequence")
        self.gridLayout_6.addWidget(self.labelSequence, 2, 0, 1, 1)
        self.lineEditReconnaissance = QtGui.QLineEdit(self.groupBoxTCPPart)
        self.lineEditReconnaissance.setObjectName("lineEditReconnaissance")
        self.gridLayout_6.addWidget(self.lineEditReconnaissance, 3, 1, 1, 1)
        self.labelReconnaissance = QtGui.QLabel(self.groupBoxTCPPart)
        self.labelReconnaissance.setObjectName("labelReconnaissance")
        self.gridLayout_6.addWidget(self.labelReconnaissance, 3, 0, 1, 1)
        self.labelHeaderTCP = QtGui.QLabel(self.groupBoxTCPPart)
        self.labelHeaderTCP.setObjectName("labelHeaderTCP")
        self.gridLayout_6.addWidget(self.labelHeaderTCP, 4, 0, 1, 1)
        self.lineEditHeaderTCP = QtGui.QLineEdit(self.groupBoxTCPPart)
        self.lineEditHeaderTCP.setObjectName("lineEditHeaderTCP")
        self.gridLayout_6.addWidget(self.lineEditHeaderTCP, 4, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxTCPPart, 1, 0, 1, 1)
        self.groupBoxHeaderPart = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxHeaderPart.setObjectName("groupBoxHeaderPart")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBoxHeaderPart)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelProtocol = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelProtocol.setObjectName("labelProtocol")
        self.gridLayout_5.addWidget(self.labelProtocol, 7, 0, 1, 1)
        self.labelIPSource = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelIPSource.setObjectName("labelIPSource")
        self.gridLayout_5.addWidget(self.labelIPSource, 8, 0, 1, 1)
        self.lineEditIPSource = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditIPSource.setObjectName("lineEditIPSource")
        self.gridLayout_5.addWidget(self.lineEditIPSource, 8, 1, 1, 1)
        self.lineEditTTL = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditTTL.setObjectName("lineEditTTL")
        self.gridLayout_5.addWidget(self.lineEditTTL, 6, 1, 1, 1)
        self.lineEditProtocol = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditProtocol.setObjectName("lineEditProtocol")
        self.gridLayout_5.addWidget(self.lineEditProtocol, 7, 1, 1, 1)
        self.labelTTL = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelTTL.setObjectName("labelTTL")
        self.gridLayout_5.addWidget(self.labelTTL, 6, 0, 1, 1)
        self.labelMacDestination = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelMacDestination.setObjectName("labelMacDestination")
        self.gridLayout_5.addWidget(self.labelMacDestination, 2, 0, 1, 1)
        self.labelHeaderLength = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelHeaderLength.setObjectName("labelHeaderLength")
        self.gridLayout_5.addWidget(self.labelHeaderLength, 5, 0, 1, 1)
        self.lineEditHeaderLength = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditHeaderLength.setObjectName("lineEditHeaderLength")
        self.gridLayout_5.addWidget(self.lineEditHeaderLength, 5, 1, 1, 1)
        self.labelTime = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelTime.setObjectName("labelTime")
        self.gridLayout_5.addWidget(self.labelTime, 1, 0, 1, 1)
        self.labelMacSource = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelMacSource.setObjectName("labelMacSource")
        self.gridLayout_5.addWidget(self.labelMacSource, 3, 0, 1, 1)
        self.labelVersion = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelVersion.setObjectName("labelVersion")
        self.gridLayout_5.addWidget(self.labelVersion, 4, 0, 1, 1)
        self.lineEditTime = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditTime.setObjectName("lineEditTime")
        self.gridLayout_5.addWidget(self.lineEditTime, 1, 1, 1, 1)
        self.lineEditMacDestination = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditMacDestination.setObjectName("lineEditMacDestination")
        self.gridLayout_5.addWidget(self.lineEditMacDestination, 2, 1, 1, 1)
        self.lineEditMacSource = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditMacSource.setObjectName("lineEditMacSource")
        self.gridLayout_5.addWidget(self.lineEditMacSource, 3, 1, 1, 1)
        self.lineEditVersion = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditVersion.setObjectName("lineEditVersion")
        self.gridLayout_5.addWidget(self.lineEditVersion, 4, 1, 1, 1)
        self.labelIPDestination = QtGui.QLabel(self.groupBoxHeaderPart)
        self.labelIPDestination.setObjectName("labelIPDestination")
        self.gridLayout_5.addWidget(self.labelIPDestination, 9, 0, 1, 1)
        self.lineEditIPDestination = QtGui.QLineEdit(self.groupBoxHeaderPart)
        self.lineEditIPDestination.setObjectName("lineEditIPDestination")
        self.gridLayout_5.addWidget(self.lineEditIPDestination, 9, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxHeaderPart, 0, 0, 1, 1)
        self.commandLinkButtonSendPacket = QtGui.QCommandLinkButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButtonSendPacket.sizePolicy().hasHeightForWidth())
        self.commandLinkButtonSendPacket.setSizePolicy(sizePolicy)
        self.commandLinkButtonSendPacket.setObjectName("commandLinkButtonSendPacket")
        self.gridLayout_4.addWidget(self.commandLinkButtonSendPacket, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.scrollArea_2 = QtGui.QScrollArea(self.PacketsModifications)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 383, 673))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_8 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.plainTextEditData = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEditData.setObjectName("plainTextEditData")
        self.gridLayout_8.addWidget(self.plainTextEditData, 1, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 0, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.PacketsModifications, "")
        self.gridLayout_9.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxPackets, 1, 0, 1, 1)
        self.groupBoxCommands = QtGui.QGroupBox(GUI)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxCommands.sizePolicy().hasHeightForWidth())
        self.groupBoxCommands.setSizePolicy(sizePolicy)
        self.groupBoxCommands.setObjectName("groupBoxCommands")
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBoxCommands)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButtonInterrupt = QtGui.QPushButton(self.groupBoxCommands)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInterrupt.sizePolicy().hasHeightForWidth())
        self.pushButtonInterrupt.setSizePolicy(sizePolicy)
        self.pushButtonInterrupt.setObjectName("pushButtonInterrupt")
        self.gridLayout_10.addWidget(self.pushButtonInterrupt, 0, 1, 1, 1)
        self.pushButtonDeleteProbe = QtGui.QPushButton(self.groupBoxCommands)
        self.pushButtonDeleteProbe.setObjectName("pushButtonDeleteProbe")
        self.gridLayout_10.addWidget(self.pushButtonDeleteProbe, 0, 2, 1, 1)
        self.commandLinkButtonRunAnalyze = QtGui.QCommandLinkButton(self.groupBoxCommands)
        self.commandLinkButtonRunAnalyze.setObjectName("commandLinkButtonRunAnalyze")
        self.gridLayout_10.addWidget(self.commandLinkButtonRunAnalyze, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxCommands, 0, 0, 1, 1)

        self.retranslateUi(GUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GUI)
        GUI.setTabOrder(self.commandLinkButtonRunAnalyze, self.pushButtonInterrupt)
        GUI.setTabOrder(self.pushButtonInterrupt, self.pushButtonDeleteProbe)
        GUI.setTabOrder(self.pushButtonDeleteProbe, self.tabWidget)
        GUI.setTabOrder(self.tabWidget, self.tableWidget)
        GUI.setTabOrder(self.tableWidget, self.plainTextEdit)
        GUI.setTabOrder(self.plainTextEdit, self.lineEditSourcePortUDP)
        GUI.setTabOrder(self.lineEditSourcePortUDP, self.lineEditSizeUDP)
        GUI.setTabOrder(self.lineEditSizeUDP, self.lineEditChecksumUDP)
        GUI.setTabOrder(self.lineEditChecksumUDP, self.scrollArea)
        GUI.setTabOrder(self.scrollArea, self.lineEditDestinationPortUDP)
        GUI.setTabOrder(self.lineEditDestinationPortUDP, self.lineEditSequence)
        GUI.setTabOrder(self.lineEditSequence, self.lineEditSourcePort)
        GUI.setTabOrder(self.lineEditSourcePort, self.lineEditDestinationPort)
        GUI.setTabOrder(self.lineEditDestinationPort, self.lineEditReconnaissance)
        GUI.setTabOrder(self.lineEditReconnaissance, self.lineEditHeaderTCP)
        GUI.setTabOrder(self.lineEditHeaderTCP, self.lineEditIPSource)
        GUI.setTabOrder(self.lineEditIPSource, self.lineEditTTL)
        GUI.setTabOrder(self.lineEditTTL, self.lineEditProtocol)
        GUI.setTabOrder(self.lineEditProtocol, self.lineEditHeaderLength)
        GUI.setTabOrder(self.lineEditHeaderLength, self.lineEditTime)
        GUI.setTabOrder(self.lineEditTime, self.lineEditMacDestination)
        GUI.setTabOrder(self.lineEditMacDestination, self.lineEditMacSource)
        GUI.setTabOrder(self.lineEditMacSource, self.lineEditVersion)
        GUI.setTabOrder(self.lineEditVersion, self.lineEditIPDestination)
        GUI.setTabOrder(self.lineEditIPDestination, self.commandLinkButtonSendPacket)
        GUI.setTabOrder(self.commandLinkButtonSendPacket, self.scrollArea_2)
        GUI.setTabOrder(self.scrollArea_2, self.plainTextEditData)

    def retranslateUi(self, GUI):
        GUI.setWindowTitle(QtGui.QApplication.translate("GUI", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxPackets.setTitle(QtGui.QApplication.translate("GUI", "Packets", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("GUI", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("GUI", "Mac Source", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("GUI", "Mac Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("GUI", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("GUI", "Header Length", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("GUI", "TTL", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("GUI", "Protocol", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("GUI", "IP Source", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("GUI", "IP Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(9).setText(QtGui.QApplication.translate("GUI", "Injection", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GUI", "Packet Content", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnalyzeTraffic), QtGui.QApplication.translate("GUI", "Analyze Traffic", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxUDPPart.setTitle(QtGui.QApplication.translate("GUI", "UDP Part", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSourcePortUDP.setText(QtGui.QApplication.translate("GUI", "Source Port", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDestinationPortUDP.setText(QtGui.QApplication.translate("GUI", "Destination Port", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSizeUDP.setText(QtGui.QApplication.translate("GUI", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.labelChecksumUDP.setText(QtGui.QApplication.translate("GUI", "Checksum", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxTCPPart.setTitle(QtGui.QApplication.translate("GUI", "TCP Part", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSourcePort.setText(QtGui.QApplication.translate("GUI", "Source Port", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDestinationPort.setText(QtGui.QApplication.translate("GUI", "Destination Port", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSequence.setText(QtGui.QApplication.translate("GUI", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReconnaissance.setText(QtGui.QApplication.translate("GUI", "Reconnaissance", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHeaderTCP.setText(QtGui.QApplication.translate("GUI", "Header TCP", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxHeaderPart.setTitle(QtGui.QApplication.translate("GUI", "Header Part", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProtocol.setText(QtGui.QApplication.translate("GUI", "Protocol", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIPSource.setText(QtGui.QApplication.translate("GUI", "IP Source", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTTL.setText(QtGui.QApplication.translate("GUI", "TTL", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMacDestination.setText(QtGui.QApplication.translate("GUI", "Mac Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHeaderLength.setText(QtGui.QApplication.translate("GUI", "Header Length", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTime.setText(QtGui.QApplication.translate("GUI", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMacSource.setText(QtGui.QApplication.translate("GUI", "Mac Source", None, QtGui.QApplication.UnicodeUTF8))
        self.labelVersion.setText(QtGui.QApplication.translate("GUI", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIPDestination.setText(QtGui.QApplication.translate("GUI", "IP Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButtonSendPacket.setText(QtGui.QApplication.translate("GUI", "Send Packet", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("GUI", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PacketsModifications), QtGui.QApplication.translate("GUI", "Packets Modifications", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxCommands.setTitle(QtGui.QApplication.translate("GUI", "Commands", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonInterrupt.setText(QtGui.QApplication.translate("GUI", "Interrupt", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteProbe.setText(QtGui.QApplication.translate("GUI", "Delete this Probe Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButtonRunAnalyze.setText(QtGui.QApplication.translate("GUI", "Run Analyze", None, QtGui.QApplication.UnicodeUTF8))

