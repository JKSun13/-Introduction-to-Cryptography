import sys
import string
import re
import nltk
import cv2
from collections import Counter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QMessageBox
import matplotlib.pyplot as plt

class Cipher_Substitution(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
    def replace_words(self, lst, dct):
        return [''.join([dct.get(c, c) for c in word]) for word in lst]
    def replace_string(self, s, dct):
        translation_table = str.maketrans(dct)
        return s.translate(translation_table)
    def anlysis(self):
        CipherText = self.textEdit.toPlainText().lower()
        key_test = self.lineEdit.text().lower()
        wordlist=re.split(r' |,|;|\.|-',CipherText)
        wordlist=[i for i in wordlist if i != '']
        text=''.join(wordlist)
        print('WORDLIST', wordlist)
        if key_test != '':
            key_test = key_test.split(',')
            key_test = dict([x.split('=') for x in key_test])
        frequency = nltk.FreqDist(text)
        Match_Dictionary = {}
        dictionary=[ 'be', 'as', 'at', 'so','of', 'is','to', 'in', 'it', 'he','we', 'by', 'or', 'on', 'do', 'if', 'me', 'my', 'up', 'an', 'go', 'no', 'us', 'am', 'll',"the","and","for","are","but","not","you","all","any","can","had","her","was","one","our","out","day","get","has","him","his","how","man","new","now","old","see","two","way","who","boy","did","its","let","put"]
        english_frequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z']
        for item in frequency:
            item_frequency = frequency[item]
            letters = english_frequency.pop(0)
            Match_Dictionary[item] = letters
        if key_test != '':
            for item in key_test:
                Match_Dictionary[item] = key_test[item]
        self.textEdit4.setText(''.join(['%s=%s ' % (k, v) for k, v in Match_Dictionary.items()]))
        DecodeList = self.replace_words(wordlist,Match_Dictionary)
        DecodeText = self.replace_string(CipherText,Match_Dictionary)
        print('DECODETEXT', DecodeText)
        DecodeText = DecodeText.lower()
        self.textEdit2.append(DecodeText)
        wordlist=re.split(r' |,|;|\.|-',CipherText)
        wordlist=[i for i in wordlist if i != '']
        text=''.join(wordlist)
        frequency = nltk.FreqDist(text)
        Advice=''
        Advice+="给出词频统计:\n"
        for letters in string.ascii_lowercase:
            Advice+=(letters + ': ' + str(frequency[letters]) + ' ')
        Advice+="\n给出特征建议："+"\n"
        Suggesting_Listform = [[], [], [], [], []]
        Suggesting_Words = ["(a) th（最常用的双字母组合）：", "\n(b)the（最常用的三字母组合）：", "\n(c)q的后面将近百分之百连接u：", "\n(d)x的前面几乎总是连接i和e：", "\n(e)在e与e之间，r的出现频率非常高："]
        for i in range(len(DecodeList)):
            word=DecodeList[i]
            for j in range(len(word)):
                if(word[j]=='t' and j!=len(word)-1):
                    Suggesting_Listform[0].append(wordlist[i][j:j+2]+'->th;')
                if(word[j]=='t'and j+2<=len(word)-1 and word[j+2]=='e'):
                    Suggesting_Listform[1].append(wordlist[i][j:j+3]+'->the;')
                if(word[j]=='q' and j!=len(word)-1):
                   Suggesting_Listform[2].append(wordlist[i][j:j+2]+'->qu;')
                if(word[j]=='x' and j!=0):
                    Suggesting_Listform[3].append(wordlist[i][j-1:j+1]+'->ix/ex;')
                if(word[j]=='e'and j+2<=len(word)-1 and word[j+2]=='e'):
                    Suggesting_Listform[4].append(wordlist[i][j:j+3]+'->ere;')
        for i in range(len(Suggesting_Listform)):
            Suggesting_Listform[i]=list(set(Suggesting_Listform[i]))
            Advice+=Suggesting_Words[i]+''.join(Suggesting_Listform[i])
        Suggesting_Listform=[]
        for word in DecodeList:
            for dic in dictionary:
                if len(dic) == len(word):
                    count = sum(1 for a, b in zip(dic, word) if a == b)
                    if count >= len(word) - 1:
                        Suggesting_Listform.append(word.lower() + '->' + dic.lower() + ';')
        print(Suggesting_Listform)
        Advice+=''.join(Suggesting_Listform).lower()
        self.textEdit3.setText(''.join(Advice.lower()))
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 260, 81, 30))
        self.pushButton.setObjectName("pushButton")
        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(440, 60, 321, 150))
        self.textEdit2.setReadOnly(True)
        self.textEdit2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 220, 251, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(190, 40, 60, 16))
        self.label2.setTextFormat(QtCore.Qt.PlainText)
        self.label2.setObjectName("label_2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(570, 40, 80, 16))
        self.label3.setObjectName("label_3")
        self.textEdit3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit3.setGeometry(QtCore.QRect(440, 250, 321, 120))
        self.textEdit3.setReadOnly(True)
        self.textEdit3.setObjectName("textEdit_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 60, 321, 150))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(44, 230, 98, 20))
        self.label.setObjectName("label")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(580, 230, 60, 16))
        self.label4.setObjectName("label_4")
        self.textEdit4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit4.setGeometry(QtCore.QRect(440, 410, 321, 110))
        self.textEdit4.setReadOnly(True)
        self.textEdit4.setObjectName("textEdit_4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(570, 380, 150, 20))
        self.label5.setObjectName("label_5")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(130, 330, 241, 170))
        self.label6.setAutoFillBackground(True)
        self.label6.setText("")
        self.label6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "单表代换破译工具"))
        self.pushButton.setText(_translate("MainWindow", "进行破译"))
        self.pushButton.clicked.connect(self.anlysis)
        self.label3.setText(_translate("MainWindow", "目前破译结果"))
        self.label4.setText(_translate("MainWindow", "破译建议"))
        self.label2.setText(_translate("MainWindow", "输入密文"))
        self.label5.setText(_translate("MainWindow", "字母可能对应"))
        self.label.setText(_translate("MainWindow", "输入已知密钥"))  

if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Cipher_Substitution()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

        
