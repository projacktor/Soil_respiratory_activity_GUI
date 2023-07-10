import sys

from PyQt5 import QtWidgets

from MainWindowUI import Ui_MainWindow


class MainWindow(object):
    def __init__(self):
        self.main_widow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_widow)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.lab_btn.clicked.connect(self.switch_to_lab)
        self.ui.field_btn.clicked.connect(self.switch_to_field)
        self.ui.field_back_btn.clicked.connect(self.back_home_from_field)
        self.ui.lab_back_btn.clicked.connect(self.back_home_from_lab)

    def show(self):
        self.main_widow.show()

    def switch_to_lab(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.lab)

    def switch_to_field(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.field)

    def back_home_from_field(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

    def back_home_from_lab(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
