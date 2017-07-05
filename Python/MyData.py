# -*- coding: utf-8 -*-

##
## Simple Class for Storing the Data.
##

class MyData():

    cbo_auswahl = ["Choice 1", "Choice 2", "Choice 3", "Choice 4"]

    def __init__(self, rows):

        self.header_data = ["FixText", "ChangeText", "State", "Choice", "Debug"]
        self.data = []
        self.__buildData(rows=rows)

    def get_header_data(self):
        return self.header_data

    def get_data(self):
        return self.data

    def __buildData(self, rows):
        for i in range(rows-1):
            fixText = "Fix Text {000:3d}".format(i)
            changeText = "Variable and Mutable Text {000:3d}".format(i)
            self.data.append([fixText, changeText, False, "Choice 1", "Info"])
        self.data.append(["Other Fix Text", "Other Mutable Text", True, "Choice 2", "An other Info"])
