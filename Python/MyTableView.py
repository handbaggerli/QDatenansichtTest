# -*- coding: utf-8 -*-

##
## Overrite QTableView for using custom widgets in cell
##

from PyQt5 import QtWidgets, QtCore

from CheckboxDelegate import CheckboxDelegate
from ComboDelegate import ComboDelegate
from MyData import MyData

class myTableView(QtWidgets.QTableView):

    def __init__(self, *args, **kwargs):
        QtWidgets.QTableView.__init__(self, *args, **kwargs)
        self.setItemDelegateForColumn(2, CheckboxDelegate(self))
        self.setItemDelegateForColumn(3, ComboDelegate(self))

        self.show_debug = True

    #
    # Implements currentIndexChanged event from the combo box
    #
    def currentIndexChanged(self, ind):
        combo_name = self.sender().objectName()
        current_index = self.currentIndex()
        index = None

        # Search for the correct index by name of the check box
        # I think, self.currentIndex() should be correct!
        for row in range(self.model().rowCount()):
            if combo_name == "cbo_{0}:{1}".format(row, 3):
                index = self.model().index(row, 3)
                break

        if self.show_debug:
            print("current index = {0}:{1} - recalculated index {2}:{3}".format(current_index.row(), current_index.column(), index.row(), index.column()))

        self.print_debug(index)
        value = MyData.cbo_auswahl[ind]
        self.model().setData(index=index, value=value, role=QtCore.Qt.EditRole)
        self.resizeColumnsToContents()
        self.print_debug(index)

    #
    # Implements clicked event from the check box
    #
    def checkbox_clicked(self, value):
        checkbox_name = self.sender().objectName()
        current_index = self.currentIndex()
        index = None

        # Search for the correct index by name of the check box
        # I think, self.currentIndex() should be correct!
        for row in range(self.model().rowCount()):
            if checkbox_name == "chk_{0}:{1}".format(row, 2):
                index = self.model().index(row, 2)
                break

        if self.show_debug:
            print("current index = {0}:{1} - recalculated index {2}:{3}".format(current_index.row(), current_index.column(), index.row(), index.column()))

        self.print_debug(index)
        self.model().setData(index=index, value=value, role=QtCore.Qt.EditRole)
        self.resizeColumnsToContents()
        self.print_debug(index)


    #
    # just print some info,
    #
    def print_debug(self, index):
        if self.show_debug:
            print("Check {0}:{1} Value: {2}".format(index.row(), index.column(), index.data()))