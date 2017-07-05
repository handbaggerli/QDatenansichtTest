# -*- coding: utf-8 -*-

##
## Delegate for a check box in the a QTableView widget
##

from PyQt5 import QtWidgets

class CheckboxDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)


    def paint(self, painter, option, index):
        checkbox = QtWidgets.QCheckBox(self.parent())

        # give the check box a name, used to find out with check box has bin clicked, because currentIndex()
        # of the cell is not always correct.
        checkbox.setObjectName("chk_{0}:{1}".format(index.row(), index.column()))

        if index.data():
            checkbox.setChecked(True)
        if not self.parent().indexWidget(index):
            self.parent().setIndexWidget(index, checkbox)

        # connect event to Table Widget
        checkbox.clicked.connect(self.parent().checkbox_clicked)

