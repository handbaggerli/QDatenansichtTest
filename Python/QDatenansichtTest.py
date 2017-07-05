# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
from MyData import MyData
import sys

if __name__ == "__main__":

    data = MyData(rows=5)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connect_user_signals()
    ui.initData(table_data=data)

    MainWindow.show()
    sys.exit(app.exec_())
