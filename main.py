import sys
import os
import subprocess
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import QFont, QFontDatabase
from mainwindow import Ui_MainWindow
from src.text_file_decoder import TextFileDecoder
from src.audio_steganograph import AudioSteganograph
from src.image_steganograph import ImageSteganograph


class MyWindow(QMainWindow, Ui_MainWindow):
    inputFileName: str
    outputFileName: str
    fileType: str

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        id = QFontDatabase.addApplicationFont("static/SFUIDisplay-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(id)
        self.setFont(QFont(families[0], 15))

        self.setWindowTitle('Cipher')

        self.radioCrypto.setChecked(True)
        self.messageEdit.hide()
        self.messageLabel.hide()

        self.typeRadioGroup = QButtonGroup(self)

        self.radioCrypto.clicked.connect(self.crypto_clicked)
        self.radioStega.clicked.connect(self.stega_clicked)
        self.typeRadioGroup.addButton(self.radioCrypto)
        self.typeRadioGroup.addButton(self.radioStega)

        self.cipherRadioGroup = QButtonGroup(self)

        self.radioCaesar.clicked.connect(self.caesar)
        self.radioVernam.clicked.connect(self.vernam)
        self.radioVigenere.clicked.connect(self.vigenere)
        self.cipherRadioGroup.addButton(self.radioCaesar)
        self.cipherRadioGroup.addButton(self.radioVernam)
        self.cipherRadioGroup.addButton(self.radioVigenere)
        self.radioCaesar.setChecked(True)

        self.SelectFileButton.clicked.connect(self.select_file)

        self.EncodeButton.clicked.connect(self.encode)
        self.DecodeButton.clicked.connect(self.decode)

    def crypto_clicked(self):
        self.radioStega.setChecked(False)
        self.messageEdit.hide()
        self.messageLabel.hide()

        self.radioCaesar.show()
        self.radioVernam.show()
        self.radioVigenere.show()

        self.keyLabel.show()
        self.keyEdit.show()

    def stega_clicked(self):
        self.radioCrypto.setChecked(False)
        self.messageEdit.show()
        self.messageLabel.show()

        self.radioCaesar.hide()
        self.radioVernam.hide()
        self.radioVigenere.hide()

        self.keyLabel.hide()
        self.keyEdit.hide()

    def caesar(self):
        self.radioVernam.setChecked(False)
        self.radioVigenere.setChecked(False)

    def vernam(self):
        self.radioCaesar.setChecked(False)
        self.radioVigenere.setChecked(False)

    def vigenere(self):
        self.radioVernam.setChecked(False)
        self.radioCaesar.setChecked(False)

    def select_file(self):
        if self.radioStega.isChecked():
            fltr = "Images (*.png *.jpg) ;;Audio (*.wav)"
        else:
            fltr = "Text files (*.txt)"
        self.inputFileName = QFileDialog.getOpenFileName(self, filter=fltr)[0]
        self.fileType = self.inputFileName[self.inputFileName.rfind('.') + 1:]

    def encode(self):
        self.outputFileName = self.filenameEdit.text()

        cipher: str
        if self.radioCaesar.isChecked():
            cipher = 'caesar'
        elif self.radioVernam.isChecked():
            cipher = 'vernam'
        elif self.radioVigenere.isChecked():
            cipher = 'vigenere'

        if self.fileType in ['txt']:
            if cipher == 'caesar':
                result = os.system(f"python cipher.py --mode=encode"
                                   f"                 --type=text"
                                   f"                 --cipher='{cipher}' "
                                   f"                 --key={self.keyEdit.text()}"
                                   f"                 --input='{self.inputFileName}'"
                                   f"                 --output='{self.outputFileName}'")
            else:
                result = os.system(f"python cipher.py --mode=encode"
                                   f"                 --type=text"
                                   f"                 --cipher='{cipher}' "
                                   f"                 --key='{self.keyEdit.text()}'"
                                   f"                 --input='{self.inputFileName}'"
                                   f"                 --output='{self.outputFileName}'")

        elif self.fileType in ['png', 'jpg']:
            os.system(f"python cipher.py --mode=encode"
                      f"                 --type=image"
                      f"                 --input='{self.inputFileName}'"
                      f"                 --output='{self.outputFileName}'"
                      f"                 --message='{self.messageEdit.text()}'")
        elif self.fileType in ['wav']:
            os.system(f"python cipher.py --mode=encode"
                      f"                 --type=audio"
                      f"                 --input='{self.inputFileName}'"
                      f"                 --output='{self.outputFileName}'"
                      f"                 --message='{self.messageEdit.text()}'")

    def decode(self):
        self.outputFileName = self.filenameEdit.text()

        cipher: str
        if self.radioCaesar.isChecked():
            cipher = 'caesar'
        elif self.radioVernam.isChecked():
            cipher = 'vernam'
        elif self.radioVigenere.isChecked():
            cipher = 'vigenere'

        if self.fileType in ['txt']:
            if cipher == 'caesar:':
                result = os.popen(f"python cipher.py --mode=decode"
                                  f"                 --type=text"
                                  f"                 --cipher={cipher}"
                                  f"                 --key={self.keyEdit.text()}"
                                  f"                 --input='{self.inputFileName}'"
                                  f"                 --output='{self.outputFileName}'").read()
            else:
                result = os.popen(f"python cipher.py --mode=decode"
                                  f"                 --type=text"
                                  f"                 --cipher={cipher}"
                                  f"                 --key='{self.keyEdit.text()}'"
                                  f"                 --input='{self.inputFileName}'"
                                  f"                 --output='{self.outputFileName}'").read()
            self.Output.setText(result)
        elif self.fileType in ['png', 'jpg']:
            result = os.popen(f"python cipher.py --mode=decode"
                              f"                 --type=image"
                              f"                 --input='{self.inputFileName}'"
                              f"                 --output='{self.outputFileName}'").read()
            self.Output.setText(result)
        elif self.fileType in ['wav']:
            result = os.popen(f"python cipher.py --mode=decode"
                              f"                 --type=audio"
                              f"                 --input='{self.inputFileName}'"
                              f"                 --output='{self.outputFileName}'").read()
            self.Output.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())
