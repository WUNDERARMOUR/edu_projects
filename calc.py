# from distutils.log import error
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(400, 400)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label_result = QtWidgets.QLabel(self.centralwidget)
#         self.label_result.setGeometry(QtCore.QRect(0, 0, 400, 80))
#         font = QtGui.QFont()
#         font.setFamily("Nirmala UI")
#         font.setPointSize(16)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(9)
#         self.label_result.setFont(font)
#         self.label_result.setStyleSheet("background-color: rgb(169, 166, 170);\n"
# "font: 75 16pt \"Nirmala UI\";\n"
# "background-color: rgb(231, 231, 231);")
#         self.label_result.setObjectName("label_result")
#         self.pushButton0 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton0.setGeometry(QtCore.QRect(0, 320, 100, 80)) # это ноль
#         self.pushButton0.setStyleSheet("background-color: rgb(251, 241, 180);\n"
# "font: 75 16pt \"Nirmala UI\";")
#         self.pushButton0.setObjectName("pushButton0")
#         self.pushButton_res = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_res.setGeometry(QtCore.QRect(100, 320, 100, 80)) #это равно
#         self.pushButton_res.setStyleSheet("background-color: rgb(255, 173, 93);\n"
# "background-color: rgb(255, 97, 97);\n"
# "background-color: rgb(197, 234, 32);\n"
# "font: 75 16pt \"MS Shell Dlg 2\";")
#         self.pushButton_res.setObjectName("pushButton_res")
#         self.pushButtonc = QtWidgets.QPushButton(self.centralwidget) 
#         self.pushButtonc.setGeometry(QtCore.QRect(200, 320, 100, 80)) # это С
#         self.pushButtonc.setStyleSheet("font: 75 16pt \"Nirmala UI\";\n"
# "background-color: rgb(255, 88, 47);")
#         self.pushButtonc.setObjectName("pushButtonc")
#         self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton9.setGeometry(QtCore.QRect(200, 80, 100, 80))
#         self.pushButton9.setStyleSheet("font: 75 16pt \"Nirmala UI\";\n"
# "background-color: rgb(251, 241, 180);")
#         self.pushButton9.setObjectName("pushButton9")
#         self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton8.setGeometry(QtCore.QRect(100, 80, 100, 80))
#         self.pushButton8.setStyleSheet("background-color: rgb(255, 173, 93);\n"
# "background-color: rgb(251, 241, 180);\n"
# "font: 75 16pt \"Nirmala UI\";")
#         self.pushButton8.setObjectName("pushButton8")
#         self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton5.setGeometry(QtCore.QRect(100, 160, 100, 80))
#         self.pushButton5.setStyleSheet("font: 75 16pt \"Nirmala UI\";\n"
# "background-color: rgb(251, 241, 180);")
#         self.pushButton5.setObjectName("pushButton5")
#         self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton7.setGeometry(QtCore.QRect(0, 80, 100, 80))
#         self.pushButton7.setStyleSheet("background-color: rgb(251, 241, 180);\n"
# "font: 75 16pt \"Nirmala UI\";")
#         self.pushButton7.setObjectName("pushButton7")
#         self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton2.setGeometry(QtCore.QRect(100, 240, 100, 80))
#         self.pushButton2.setStyleSheet("background-color: rgb(251, 241, 180);\n"
# "font: 75 16pt \"Nirmala UI\";")
#         self.pushButton2.setObjectName("pushButton2")
#         self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton4.setGeometry(QtCore.QRect(0, 160, 100, 80))
#         self.pushButton4.setStyleSheet("font: 75 16pt \"Nirmala UI\";\n"
# "background-color: rgb(255, 173, 93);\n"
# "background-color: rgb(251, 241, 180);")
#         self.pushButton4.setObjectName("pushButton4")
#         self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton1.setGeometry(QtCore.QRect(0, 240, 100, 80))
#         self.pushButton1.setStyleSheet("background-color: rgb(251, 241, 180);\n"
# "font: 75 16pt \"Nirmala UI\";")
#         self.pushButton1.setObjectName("pushButton1")
#         self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton3.setGeometry(QtCore.QRect(200, 240, 100, 80))
#         self.pushButton3.setStyleSheet("background-color: rgb(251, 241, 180);\n"
# "font: 75 16pt \"Nirmala UI\";")
#         self.pushButton3.setObjectName("pushButton3")
#         self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton6.setGeometry(QtCore.QRect(200, 160, 100, 80))
#         self.pushButton6.setStyleSheet("font: 75 16pt \"Nirmala UI\";\n"
# "background-color: rgb(251, 241, 180);")
#         self.pushButton6.setObjectName("pushButton6")
#         self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_plus.setGeometry(QtCore.QRect(300, 80, 100, 80))
#         self.pushButton_plus.setStyleSheet("font: 75 16pt \"Nirmala UI\";\n"
# "font: 75 16pt \"MS Shell Dlg 2\";\n"
# "background-color: rgb(157, 209, 191);")
#         self.pushButton_plus.setObjectName("pushButton_plus")
#         self.pushButton_umnozh = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_umnozh.setGeometry(QtCore.QRect(300, 240, 100, 80))
#         self.pushButton_umnozh.setStyleSheet("font: 17pt \"MS Shell Dlg 2\";\n"
# "background-color: rgb(157, 209, 191);")
#         self.pushButton_umnozh.setObjectName("pushButton_umnozh")
#         self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_minus.setGeometry(QtCore.QRect(300, 160, 100, 80))
#         self.pushButton_minus.setStyleSheet("font: 75 16pt \"Nirmala UI\";\n"
# "font: 18pt \"MS Shell Dlg 2\";\n"
# "background-color: rgb(157, 209, 191);")
#         self.pushButton_minus.setObjectName("pushButton_minus")
#         self.pushButton_delen = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_delen.setGeometry(QtCore.QRect(300, 320, 100, 80))
#         self.pushButton_delen.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
# "background-color: rgb(157, 209, 191);")
#         self.pushButton_delen.setObjectName("pushButton_delen")
#         MainWindow.setCentralWidget(self.centralwidget)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#         self.add_functions()


#         self.is_equal = False


#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
#         self.label_result.setText(_translate("MainWindow", "0"))
#         self.pushButton0.setText(_translate("MainWindow", "0"))
#         self.pushButton_res.setText(_translate("MainWindow", "="))
#         self.pushButton9.setText(_translate("MainWindow", "9"))
#         self.pushButton8.setText(_translate("MainWindow", "8"))
#         self.pushButton5.setText(_translate("MainWindow", "5"))
#         self.pushButton7.setText(_translate("MainWindow", "7"))
#         self.pushButton2.setText(_translate("MainWindow", "2"))
#         self.pushButton4.setText(_translate("MainWindow", "4"))
#         self.pushButton1.setText(_translate("MainWindow", "1"))
#         self.pushButton3.setText(_translate("MainWindow", "3"))
#         self.pushButton6.setText(_translate("MainWindow", "6"))
#         self.pushButton_plus.setText(_translate("MainWindow", "+"))
#         self.pushButton_umnozh.setText(_translate("MainWindow", "*"))
#         self.pushButton_minus.setText(_translate("MainWindow", "-"))
#         self.pushButton_delen.setText(_translate("MainWindow", "/"))
#         self.pushButtonc.setText(_translate("MainWindow", "C"))

#     def add_functions(self):
#         self.pushButton0.clicked.connect(lambda: self.write_number(self.pushButton0.text()))
#         self.pushButton1.clicked.connect(lambda: self.write_number(self.pushButton1.text()))
#         self.pushButton2.clicked.connect(lambda: self.write_number(self.pushButton2.text()))
#         self.pushButton3.clicked.connect(lambda: self.write_number(self.pushButton3.text()))
#         self.pushButton4.clicked.connect(lambda: self.write_number(self.pushButton4.text()))
#         self.pushButton5.clicked.connect(lambda: self.write_number(self.pushButton5.text()))
#         self.pushButton6.clicked.connect(lambda: self.write_number(self.pushButton6.text()))
#         self.pushButton7.clicked.connect(lambda: self.write_number(self.pushButton7.text()))
#         self.pushButton8.clicked.connect(lambda: self.write_number(self.pushButton8.text()))
#         self.pushButton9.clicked.connect(lambda: self.write_number(self.pushButton9.text()))
#         self.pushButton_plus.clicked.connect(lambda: self.write_number(self.pushButton_plus.text()))
#         self.pushButton_minus.clicked.connect(lambda: self.write_number(self.pushButton_minus.text()))
#         self.pushButton_umnozh.clicked.connect(lambda: self.write_number(self.pushButton_umnozh.text()))
#         self.pushButton_delen.clicked.connect(lambda: self.write_number(self.pushButton_delen.text()))
        
#         self.pushButton_res.clicked.connect(self.results)

#         # self.pushButtonc.clicked.connect(lambda: self.results(self.pushButtonc.text()))
        
        



#     def write_number(self, number):
#         if self.label_result.text() == "0" or self.is_equal:
#             self.label_result.setText(number)
#             self.is_equal = False
#         else:
#             self.label_result.setText(self.label_result.text() + number)

#     def results(self):
#         if not self.is_equal:
#             res = eval(self.label_result.text())
#             self.label_result.setText('Результат: ' + str(res))
#             self.is_equal = True
#         else:
#             error = QMessageBox()
#             error.setWindowTitle('Ошибка')
#             error.setText('Невозможно выполнить данное действие')
#             error.setIcon(QMessageBox.Warning)
#             error.setStandardButtons(QMessageBox.OK|QMessageBox.Cancel)
#             error.exec_()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

from art import*
import pdfplumber
from gtts import gTTS
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        return 'File exists!'

        with pdfplumber.PDF(open(file=file_path, mode = 'rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)

        with open('text1.txt', 'w') as file:
            file.write(text)

        text = text.replace("\n", '')

        with open('text2.txt', 'w') as file:
            file.write(text)
    else:
        return 'File not exists, check the file path'

def main():
    print(pdf_to_mp3(file_path='C:\\Users\iphed\PycharmProjects\pythonProject\pdftomp3\pdf_files\pdf.pdf'))

if __name__ =='__main__':
    main()
