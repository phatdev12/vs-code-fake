# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(323, 395)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 40, 301, 341))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.frame.setStyleSheet("border-style: none;\n"
"background-color: rgb(199, 216, 195);\n"
"border-radius: 10px;\n"
"border-bottom: 3px solid rgb(122, 132, 119);\n"
"border-top: 3px solid rgb(122, 132, 119);\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(1, 330, 299, 8))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    color: white;\n"
"    text-align: center;\n"
"    border-style: none;\n"
"    border-radius: 4px;\n"
"    background-color:rgb(122, 132, 119);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 3px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(214, 232, 209, 255), stop:1 rgba(180, 195, 176, 255));\n"
"\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(97, 292, 111, 21))
        self.label.setStyleSheet("border-style: none;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(122, 132, 119);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(59, 70, 181, 181))
        self.label_2.setStyleSheet("border-radius: 0px;\n"
"border-style: none;\n"
"background: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("python_3.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(94, 2, 111, 31))
        self.label_3.setStyleSheet("border-radius: 0px;\n"
"border-style: none;\n"
"color:rgb(199, 216, 195);\n"
"background: rgb(122, 132, 119)")
        self.label_3.setObjectName("label_3")
        self.label_2.raise_()
        self.progressBar.raise_()
        self.label.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">PYCOS VISUAL</p></body></html>reui.py"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">RESET APP</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
