# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'theme.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_theme(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 395)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 145, 255, 255));")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 511, 361))
        self.frame.setStyleSheet("background:#2b303b;\n"
"border-radius: 7px;\n"
"border-bottom: 4px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"border-top: 4px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 325, 311, 31))
        self.label.setStyleSheet("border-style: none;\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(360, 325, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-style: none;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius: 2px;\n"
"    background-color: ;\n"
"    background-color: rgb(31, 35, 43);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 325, 31, 31))
        self.label_2.setStyleSheet("border-style: none;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("des.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(450, 325, 61, 31))
        self.label_3.setStyleSheet("border-style: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setPixmap(QtGui.QPixmap("des.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(475, 12, 21, 21))
        self.toolButton.setStyleSheet("QToolButton{\n"
"border-style: none;\n"
"    font-size: 1px;\n"
"}\n"
"QToolButton:hover{\n"
"    font: 75 12pt \"Segoe UI Black\";\n"
"    background-color: rgb(35, 44, 63);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 60, 131, 91))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-style: none;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 0px;\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 60, 131, 91))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"border-style: none;\n"
"background-color: rgb(29, 29, 29);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 0px;\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 200, 131, 91))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border-style: none;\n"
"background-color: rgb(38, 38, 56);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 0px;\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 200, 131, 91))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"border-style: none;\n"
"background-color: rgb(0, 85, 127);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 0px;\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(230, 10, 51, 20))
        self.label_4.setStyleSheet("border-style: none;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "  Column | Theme Edit"))
        self.pushButton.setText(_translate("Form", "Pycos Visual"))
        self.label_3.setText(_translate("Form", " |  Plain"))
        self.toolButton.setText(_translate("Form", "X"))
        self.label_4.setText(_translate("Form", "Theme"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_theme()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
