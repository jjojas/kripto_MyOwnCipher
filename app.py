import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

import modules.encrypt as encr

from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


cipherCache = ""

class rc4Widget(qtw.QWidget):
    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)   
        self.initUI()
    
    def initUI(self):
        def encrypt():
            cipherCache = encr.encryptText(ptextBox.text(),ktextBox.text())
            # splitted = vig.splitStringTo5Chars(rep)
            ctextBox.setText(cipherCache)
            # options = qtw.QFileDialog.Options()
            # options |= qtw.QFileDialog.DontUseNativeDialog
            # fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
            # if fileName:
            #     print(fileName)

        def decrypt():
            c = encr.decryptText(ctextBox.text(),ktextBox.text())
            rep = repr(c)
            # splitted = vig.splitStringTo5Chars(rep)
            ptextBox.setText(rep[:-1][1:])

        def save():
            encr.saveCipherToTextfile(ctextBox.text(),saveLine.text())
            msg = QMessageBox()
            msg.setText("File tersimpan!")
            msg.setInformativeText(f'Cipherteks berhasil disimpan pada direktori cipher/text/{saveLine.text()}.txt')
            msg.setWindowTitle("Simpan berhasil")
            msg.exec_()

        def encryptBinaryFile():
            if (len(ktextBox.text()) != 0):
                options = qtw.QFileDialog.Options()
                options |= qtw.QFileDialog.DontUseNativeDialog
                fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
                if fileName:
                    # try:
                    encr.encryptBinaryFile(fileName,ktextBox.text())
                    msg = QMessageBox()
                    msg.setText(f"Filemu berhasil dienkripsi di cipher/files/encrypted_{fileName.split('/')[-1]}")
                    msg.setWindowTitle("Enkripsi Berhasil")
                    msg.exec_()
                    # except Exception as e:
                    #     print(e)
            else:
                msg = QMessageBox()
                msg.setText("Cipher key tidak boleh kosong!")
                msg.setWindowTitle("Enkripsi gagal")
                msg.exec_()

        def decryptBinaryFile():
            if (len(ktextBox.text()) != 0):
                options = qtw.QFileDialog.Options()
                options |= qtw.QFileDialog.DontUseNativeDialog
                fileName, _ = qtw.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
                if fileName:
                    try:
                        encr.decryptBinaryFile(fileName,ktextBox.text())
                        msg = QMessageBox()
                        msg.setText(f"Filemu berhasil dienkripsi di cipher/files/decrypted_{fileName.split('/')[-1]}")
                        msg.setWindowTitle("Enkripsi Berhasil")
                        msg.exec_()
                    except Exception as e:
                        print(e)
            else:
                msg = QMessageBox()
                msg.setText("Cipher key tidak boleh kosong!")
                msg.setWindowTitle("Dekripsi gagal")
                msg.exec_()

        self.layout = qtw.QGridLayout(self)
        self.setLayout(self.layout)

        ptextLabel = qtw.QLabel("Plaintext:", self)
        ptextBox = qtw.QLineEdit(self)

        self.layout.addWidget(ptextLabel,0,0)
        self.layout.addWidget(ptextBox,1,0)

        ktextLabel = qtw.QLabel("Key:", self)
        ktextBox = qtw.QLineEdit(self)

        self.layout.addWidget(ktextLabel,0,1)
        self.layout.addWidget(ktextBox,1,1)

        ctextLabel = qtw.QLabel("Ciphertext:", self)
        ctextBox = qtw.QLineEdit(self)

        self.layout.addWidget(ctextLabel,0,2)
        self.layout.addWidget(ctextBox,1,2)

        buttonFileLayout = qtw.QGroupBox()
        buttonFileLayout.setLayout(qtw.QHBoxLayout())

        encryptFileButton = qtw.QPushButton("Encrypt File Binary")
        encryptFileButton.clicked.connect(lambda: encryptBinaryFile())
        buttonFileLayout.layout().addWidget(encryptFileButton,0,Qt.AlignHCenter)

        decryptFileButton = qtw.QPushButton("Decrypt File Binary")  
        decryptFileButton.clicked.connect(lambda: decryptBinaryFile()) 
        buttonFileLayout.layout().addWidget(decryptFileButton,1,Qt.AlignHCenter)

        self.layout.addWidget(buttonFileLayout,2,0)

        buttonLayout = qtw.QGroupBox()
        buttonLayout.setLayout(qtw.QHBoxLayout())
    
        encryptButton = qtw.QPushButton("Encrypt")
        encryptButton.clicked.connect(lambda: encrypt())
        buttonLayout.layout().addWidget(encryptButton,0,Qt.AlignHCenter)

        decryptButton = qtw.QPushButton("Decrypt")  
        decryptButton.clicked.connect(lambda: decrypt()) 
        buttonLayout.layout().addWidget(decryptButton,1,Qt.AlignHCenter)

        self.layout.addWidget(buttonLayout,2,1)

        saveBoxLayout = qtw.QGroupBox()
        saveBoxLayout.setLayout(qtw.QVBoxLayout())
        saveLabel = qtw.QLabel("Filename:", self)
        saveLine = qtw.QLineEdit(self)
        saveButton = qtw.QPushButton("Save Ciphertext")  
        saveButton.clicked.connect(lambda: save()) 

        saveBoxLayout.layout().addWidget(saveLabel,0,Qt.AlignHCenter)
        saveBoxLayout.layout().addWidget(saveLine,1,Qt.AlignHCenter)
        saveBoxLayout.layout().addWidget(saveButton,2,Qt.AlignHCenter)

        self.layout.addWidget(saveBoxLayout,2,2)


class mainWidget(qtw.QWidget):
    def __init__(self, parent):
        super(qtw.QWidget, self).__init__(parent)   
        self.initUI()
    
    def initUI(self):
        '''
        Menginisialisasi antarmuka utama
        '''
        self.layout = qtw.QHBoxLayout(self)
        self.tabs = qtw.QTabWidget()
        self.tabs.setFont(QFont('Roboto', 14))
        self.tabs.addTab(rc4Widget(self),"RC4")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)    

class MainWindow(qtw.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Tugas Kecil 2 - My Own Cipher")
        # self.setGeometry(0, 0, 1920, 1080)
        self.mainWidget = mainWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.show()

suppress_qt_warnings()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
