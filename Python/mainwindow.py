# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitRepos\QDatenansichtTest2\GuiBuilder\QDatenansichtTest2\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MyData import MyData
from MyModel import MyModel
from MyTableView import myTableView


class Ui_MainWindow(object):
    def __init__(self):
        self.table_data = None
        self.table_view = None
        self.table_model = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 345)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        #        self.tableView = QtWidgets.QTableView(self.centralWidget) ---> Replace Gui Builder Widget with user Widget
        self.tableView = myTableView(self.centralWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Print = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Print.setObjectName("pushButton_Print")
        self.horizontalLayout.addWidget(self.pushButton_Print)
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.horizontalLayout.addWidget(self.pushButton_Reset)
        self.pushButton_Clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.horizontalLayout.addWidget(self.pushButton_Clear)
        self.pushButton_Load = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Load.setObjectName("pushButton_Load")
        self.horizontalLayout.addWidget(self.pushButton_Load)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 433, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ###################################
        # own Code
        ###################################
        # Enables Sorting
        self.tableView.setSortingEnabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Testansicht mit Table und Model"))
        self.pushButton_Print.setText(_translate("MainWindow", "Print"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_Load.setText(_translate("MainWindow", "Load"))
    #
    # extends initialisation
    #
    def initData(self, table_data):
        self.table_data = table_data
        self.table_model = MyModel(header=self.table_data.header_data, data=self.table_data.data)
        self.tableView.setModel(self.table_model)
        self.tableView.resizeColumnsToContents()


    #
    # connect signals to slot
    #
    def connect_user_signals(self):
        self.pushButton_Reset.clicked.connect(self.__reset)
        self.pushButton_Load.clicked.connect(self.__load)
        self.pushButton_Clear.clicked.connect(self.__clear)
        self.pushButton_Print.clicked.connect(self.__print)


    #
    # Reset button pressed
    #
    def __reset(self):
        new_table_data = MyData(rows=5)
        self.initData(table_data=new_table_data)


    #
    # Clear button pressed
    #
    def __clear(self):
        self.tableView.setModel(None)

    #
    # Load button pressed
    #
    def __load(self):
        self.tableView.setModel(self.table_model)


    #
    # Print button pressed
    #
    def __print(self):
        print("__print")
        for fix_text, change_text, state, choice, debug in self.table_data.get_data():
            print("{0} - {1} - {2} - {3} - {4}".format(fix_text, change_text, state, choice, debug))
