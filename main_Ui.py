from PyQt5 import QtWidgets

from App_UI import Ui_MainWindow

"""TODO: прописать ввод для line_edit
прописать вывод для text_edit"""


class MainWindow(object):
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.buttons()

    def show(self):
        self.main_window.show()

    def buttons(self):
        # home screen
        self.ui.LabGKHBtn.clicked.connect(self.switch_to_lab_gkh)
        self.ui.LabTitrBtn.clicked.connect(self.switch_to_lab_titr)
        self.ui.FieldGKHBtn.clicked.connect(self.switch_to_field_gkh)
        self.ui.FieldCO2Btn.clicked.connect(self.switch_to_field_co2)
        self.ui.Exel.clicked.connect(self.switch_to_exel)
        # back buttons
        self.ui.lab_gkh_back_home_btn.clicked.connect(self.back_home)
        self.ui.lab_titr_back_home_btn.clicked.connect(self.back_home)
        self.ui.field_GKH_back_home_btn.clicked.connect(self.back_home)
        self.ui.field_CO2_back_home_btn.clicked.connect(self.back_home)

    def switch_to_lab_gkh(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.lab_GKH_eval)

    def switch_to_lab_titr(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.lab_titrovaniye_eval)

    def switch_to_field_gkh(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.field_GKH_eval)

    def switch_to_field_co2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.field_CO2_eval)

    def switch_to_exel(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EXEL)

    def back_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)