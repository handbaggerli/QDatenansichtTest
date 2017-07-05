# -*- coding: utf-8 -*-

##
## Delegate for a combo box in the a QTableView widget
##

from PyQt5 import QtWidgets
from MyData import MyData

class ComboDelegate(QtWidgets.QItemDelegate):

    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)


    def paint(self, painter, option, index):
        combo = QtWidgets.QComboBox(self.parent())
        # give the combo box a name, used to find out with combo box has bin changed, because currentIndex()
        # of the cell is not always correct.
        combo.setObjectName("cbo_{0}:{1}".format(index.row(), index.column()))
        combo.addItems(MyData.cbo_auswahl)

        if not self.parent().indexWidget(index):
            combo.setCurrentText(index.data())
            self.parent().setIndexWidget(index, combo)

        # connect event in Table Widget
        combo.currentIndexChanged.connect(self.parent().currentIndexChanged)
