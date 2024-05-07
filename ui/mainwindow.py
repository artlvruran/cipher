from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(1798, 1175)

        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 30, 1511, 781))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.messageEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.messageEdit.setObjectName("messageEdit")
        self.gridLayout.addWidget(self.messageEdit, 4, 1, 1, 2)

        self.DecodeButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.DecodeButton.setStyleSheet("")
        self.DecodeButton.setObjectName("DecodeButton")
        self.gridLayout.addWidget(self.DecodeButton, 6, 2, 1, 1)

        self.keyEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.keyEdit.setObjectName("keyEdit")
        self.gridLayout.addWidget(self.keyEdit, 2, 1, 1, 2)

        self.radioVigenere = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioVigenere.setMinimumSize(QtCore.QSize(500, 0))
        self.radioVigenere.setObjectName("radioVigenere")
        self.gridLayout.addWidget(self.radioVigenere, 1, 1, 1, 1)

        self.radioCrypto = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioCrypto.setMinimumSize(QtCore.QSize(0, 0))
        self.radioCrypto.setObjectName("radioCrypto")
        self.gridLayout.addWidget(self.radioCrypto, 0, 1, 1, 1)

        self.radioCaesar = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioCaesar.setMinimumSize(QtCore.QSize(0, 0))
        self.radioCaesar.setMaximumSize(QtCore.QSize(500, 16777215))
        self.radioCaesar.setObjectName("radioCaesar")
        self.gridLayout.addWidget(self.radioCaesar, 1, 0, 1, 1)

        self.radioStega = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioStega.setObjectName("radioStega")
        self.gridLayout.addWidget(self.radioStega, 0, 0, 1, 1)

        self.SelectFileButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.SelectFileButton.setMouseTracking(True)
        self.SelectFileButton.setStyleSheet("")
        self.SelectFileButton.setObjectName("SelectFileButton")
        self.gridLayout.addWidget(self.SelectFileButton, 3, 0, 1, 3)

        self.keyLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.keyLabel.setObjectName("keyLabel")
        self.gridLayout.addWidget(self.keyLabel, 2, 0, 1, 1)

        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.messageLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.messageLabel.setObjectName("messageLabel")
        self.gridLayout.addWidget(self.messageLabel, 4, 0, 1, 1)

        self.radioVernam = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioVernam.setMinimumSize(QtCore.QSize(0, 0))
        self.radioVernam.setObjectName("radioVernam")
        self.gridLayout.addWidget(self.radioVernam, 1, 2, 1, 1)

        self.EncodeButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.EncodeButton.setMouseTracking(True)
        self.EncodeButton.setStyleSheet("")
        self.EncodeButton.setObjectName("EncodeButton")
        self.gridLayout.addWidget(self.EncodeButton, 6, 0, 1, 1)

        self.filenameEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.filenameEdit.setObjectName("filenameEdit")
        self.gridLayout.addWidget(self.filenameEdit, 5, 1, 1, 2)

        self.Output = QtWidgets.QTextBrowser(parent=self.gridLayoutWidget)
        self.Output.setObjectName("Output")
        self.gridLayout.addWidget(self.Output, 7, 0, 1, 3)

        self.hackButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.hackButton.setObjectName("hackButton")
        self.gridLayout.addWidget(self.hackButton, 6, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1798, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DecodeButton.setText(_translate("MainWindow", "Decode"))
        self.radioVigenere.setText(_translate("MainWindow", "Vigenere"))
        self.radioCrypto.setText(_translate("MainWindow", "Cryptography"))
        self.radioCaesar.setText(_translate("MainWindow", "Caesar"))
        self.radioStega.setText(_translate("MainWindow", "Steganography"))
        self.SelectFileButton.setText(_translate("MainWindow", "Select file"))
        self.keyLabel.setText(_translate("MainWindow", "Enter the key"))
        self.label.setText(_translate("MainWindow", "Enter the output filename"))
        self.messageLabel.setText(_translate("MainWindow", "Enter your message"))
        self.radioVernam.setText(_translate("MainWindow", "Vernam"))
        self.EncodeButton.setText(_translate("MainWindow", "Encode"))
        self.hackButton.setText(_translate("MainWindow", "Hack"))
