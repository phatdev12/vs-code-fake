# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'White.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 547)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QMainWindow{\n"
"border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(" background: #fff;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(44, 18))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 41, 48))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background: #fff;\n"
"border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
" background: #fff;\n"
" border-left: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;\n"
"}\n"
"QPushButton:selected{\n"
" border-left: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 59, 41, 48))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background: #fff;\n"
"border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
"background: #fff;\n"
" border-left: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;\n"
"}\n"
"QPushButton:selected{\n"
" border-left: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;\n"
"}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("f9bb81e576c1a361c61a8c08945b2c48-search-icon-by-vexels.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 122, 41, 48))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background: #fff;\n"
"border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
"background: #fff;\n"
" border-left: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;\n"
"}\n"
"QPushButton:selected{\n"
" border-left: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;\n"
"}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 47, 50))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background: #fff;\n"
"border-style: none;\n"
"}\n"
"QPushButton:hover{\n"
"background: #fff;\n"
" border-left: 3px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;\n"
"}")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("acc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.frame)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"border-style: none;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_2)
        self.treeWidget.setStyleSheet("QTreeView{\n"
"border-style: none;\n"
"}\n"
"QTreeView::branch {\n"
"    background-color: white;\n"
"}\n"
"QHeaderView {\n"
"    color: #fff;\n"
"font-size: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 145, 255, 255));\n"
"}")
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"   border: 1px solid gray;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: none;\n"
"  background: #3d4557;\n"
"    text-align: left;\n"
"    top: 0px;\n"
"  \n"
"    \n"
"    \n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(207, 207, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
"  padding: 7px 60px;\n"
" }\n"
"QTabBar::tab:hover {\n"
"  background: #1d2028;\n"
"    font-size: 10px;\n"
" }\n"
"\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: #fff;\n"
"  border-bottom: 2.4px solid  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;\n"
"transition-duration: 0.5s;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
" }\n"
"QTabWidget::pane { \n"
"   border: none;\n"
"}\n"
"QTabBar::close-button{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"    border-radius: 8px;\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background: #fff;\n"
"font-size: 20px;")
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("python.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setStyleSheet("border-style: none;")
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 2, 111, 21))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"font-size: 12x;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 144, 217, 255), stop:1 rgba(1, 96, 188, 255));\n"
"    font-size: 12x;\n"
"    color: white;\n"
"    background-color: rgb(0, 85, 127);\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 2, 111, 21))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"font-size: 12x;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 144, 217, 255), stop:1 rgba(1, 96, 188, 255));\n"
"    font-size: 12x;\n"
"    color: white;\n"
"    background-color: rgb(0, 85, 127);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_11.setGeometry(QtCore.QRect(240, 2, 111, 21))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"font-size: 12x;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 144, 217, 255), stop:1 rgba(1, 96, 188, 255));\n"
"    font-size: 12x;\n"
"    color: white;\n"
"    background-color: rgb(0, 85, 127);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_12.setGeometry(QtCore.QRect(360, 2, 111, 21))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"font-size: 12x;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 144, 217, 255), stop:1 rgba(1, 96, 188, 255));\n"
"    font-size: 12x;\n"
"    color: white;\n"
"    background-color: rgb(0, 85, 127);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.frame_5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("acc.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background:#2b303b;")
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.page)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_4.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.page)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.page)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_4.addWidget(self.pushButton_15)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(35, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_6.setStyleSheet("border-style: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(198, 4, 46, 255), stop:1 rgba(171, 91, 122, 255));\n"
"border-radius: 12px;")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_7.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_7.setStyleSheet("border-style: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(162, 162, 0, 255), stop:1 rgba(252, 255, 63, 255));\n"
"border-radius: 12px;")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_8.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_8.setStyleSheet("border-style: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(161, 161, 0, 255));\n"
"border-radius: 12px;")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setStyleSheet("border-style: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(174, 255, 0, 255), stop:1 rgba(72, 145, 26, 255));\n"
"border-radius: 12px;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.horizontalLayout_2.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMinimumSize(QtCore.QSize(100, 40))
        self.menubar.setMaximumSize(QtCore.QSize(1222222, 40))
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setStyleSheet("QMenuBar{\n"
"top: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background: #3d4557;\n"
"font-size: 13px;\n"
"font-family: arial;\n"
"border-bottom: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"border-top: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}\n"
"QMenuBar::icon{\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QMenuBar::item {\n"
" right: 20px;\n"
"left: 10px;\n"
"margin-right: 14px;\n"
"margin-top : 18px;\n"
" }\n"
"QMenuBar::item:pressed {\n"
"    background-color: #58647d;\n"
"border-bottom: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}\n"
"QMenuBar::item:selected  {\n"
"    height: 30px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.494, y1:1, x2:0.477273, y2:0.199, stop:0 rgba(3, 156, 255, 242), stop:0.431818 rgba(46, 61, 72, 255));\n"
"border-bottom: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setGeometry(QtCore.QRect(454, 158, 258, 119))
        self.menuFile.setStyleSheet("background: #3d4557;\n"
"border-radius: 5px;\n"
"")
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setGeometry(QtCore.QRect(489, 158, 135, 50))
        self.menuEdit.setObjectName("menuEdit")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuView.setObjectName("menuView")
        self.menuTheme = QtWidgets.QMenu(self.menuView)
        self.menuTheme.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuTheme.setObjectName("menuTheme")
        self.menuBuild = QtWidgets.QMenu(self.menubar)
        self.menuBuild.setObjectName("menuBuild")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuH_lp = QtWidgets.QMenu(self.menubar)
        self.menuH_lp.setObjectName("menuH_lp")
        self.menuG_t = QtWidgets.QMenu(self.menubar)
        self.menuG_t.setObjectName("menuG_t")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        self.menuX = QtWidgets.QMenu(self.menubar)
        self.menuX.setGeometry(QtCore.QRect(339, 158, 135, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuX.sizePolicy().hasHeightForWidth())
        self.menuX.setSizePolicy(sizePolicy)
        self.menuX.setMinimumSize(QtCore.QSize(25, 5))
        self.menuX.setMaximumSize(QtCore.QSize(16777215, 131))
        self.menuX.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menuX.setAutoFillBackground(False)
        self.menuX.setStyleSheet("")
        self.menuX.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.menuX.setTitle("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuX.setIcon(icon5)
        self.menuX.setSeparatorsCollapsible(False)
        self.menuX.setToolTipsVisible(False)
        self.menuX.setObjectName("menuX")
        self.menuDebug = QtWidgets.QMenu(self.menubar)
        self.menuDebug.setObjectName("menuDebug")
        self.menuForum = QtWidgets.QMenu(self.menubar)
        self.menuForum.setObjectName("menuForum")
        self.menuPycos_Visual = QtWidgets.QMenu(self.menubar)
        self.menuPycos_Visual.setStyleSheet("border-style: none;")
        self.menuPycos_Visual.setObjectName("menuPycos_Visual")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMinimumSize(QtCore.QSize(100, 0))
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.statusbar.setStatusTip("")
        self.statusbar.setStyleSheet("background: #3d4557;\n"
"border-bottom: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(3, 167, 255, 255), stop:1 rgba(199, 255, 248, 255));;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File_Ctrl_N = QtWidgets.QAction(MainWindow)
        self.actionOpen_File_Ctrl_N.setObjectName("actionOpen_File_Ctrl_N")
        self.actionOpen_Folder_Ctrl_Alt_N = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder_Ctrl_Alt_N.setObjectName("actionOpen_Folder_Ctrl_Alt_N")
        self.actionAdd_Tab = QtWidgets.QAction(MainWindow)
        self.actionAdd_Tab.setObjectName("actionAdd_Tab")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.menuFile.addAction(self.actionOpen_File_Ctrl_N)
        self.menuFile.addAction(self.actionOpen_Folder_Ctrl_Alt_N)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAdd_Tab)
        self.menuTheme.addAction(self.actionEdit)
        self.menuView.addAction(self.menuTheme.menuAction())
        self.menubar.addAction(self.menuX.menuAction())
        self.menubar.addAction(self.menuPycos_Visual.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())
        self.menubar.addAction(self.menuBuild.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuG_t.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuH_lp.menuAction())
        self.menubar.addAction(self.menuForum.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Open Files"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#7a7a7a;\">WELCOME</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#36938b;\">Ctrl + N</span><span style=\" font-size:12pt; color:#7a7a7a;\"> To </span><span style=\" font-size:12pt; color:#36938b;\">Open</span><span style=\" font-size:12pt; color:#7a7a7a;\"> File</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#36938b;\">Ctrl + S</span><span style=\" font-size:12pt; color:#7a7a7a;\"> To </span><span style=\" font-size:12pt; color:#36938b;\">Save</span><span style=\" font-size:12pt; color:#7a7a7a;\"> File</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#36938b;\">Ctrl + O</span><span style=\" font-size:12pt; color:#7a7a7a;\"> To </span><span style=\" font-size:12pt; color:#36938b;\">Create</span><span style=\" font-size:12pt; color:#7a7a7a;\"> Project</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#7a7a7a;\">Click Here To </span><a href=\"google.com\"><span style=\" font-size:12pt; text-decoration: underline; color:#36938b;\">Learn More</span></a></p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Open File"))
        self.pushButton_10.setText(_translate("MainWindow", "New File"))
        self.pushButton_11.setText(_translate("MainWindow", "Save File"))
        self.pushButton_12.setText(_translate("MainWindow", "Save as"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Welcome"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Welcome Tutorial"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme                            "))
        self.menuBuild.setTitle(_translate("MainWindow", "Build"))
        self.menuTool.setTitle(_translate("MainWindow", "Tools"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuH_lp.setTitle(_translate("MainWindow", "Help"))
        self.menuG_t.setTitle(_translate("MainWindow", "Goto"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuDebug.setTitle(_translate("MainWindow", "Debug"))
        self.menuForum.setTitle(_translate("MainWindow", "Forum"))
        self.menuPycos_Visual.setTitle(_translate("MainWindow", "Pycos Visual  |  "))
        self.actionOpen_File_Ctrl_N.setText(_translate("MainWindow", "Open File                                Ctrl+N"))
        self.actionOpen_Folder_Ctrl_Alt_N.setText(_translate("MainWindow", "Open Folder                           Ctrl+Alt+N"))
        self.actionAdd_Tab.setText(_translate("MainWindow", "Add Tab"))
        self.actionEdit.setText(_translate("MainWindow", "Edit                      "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
