from PyQt5 import QtWidgets

from App_UI_old_1 import Ui_MainWindow
from eval import *


class MainWindow(object):
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.buttons()

    def show(self):
        self.main_window.show()

    # initializing buttons
    def buttons(self):
        # home screen buttons
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
        # input buttons
        self.ui.input_lab_gkh.clicked.connect(self.input_lab_gkh)
        self.ui.input_field_gkh.clicked.connect(self.input_field_gkh)
        self.ui.input_lab_titr.clicked.connect(self.input_lab_titr)
        self.ui.input_field_co2.clicked.connect(self.input_field_co2)

    def input_lab_gkh(self):
        try:
            if all(float(i) for i in [self.ui.bac_m_lab_gkh_lineEdit.text(), self.ui.volume_lab_gkh_lineEdit.text(), self.ui.time_lab_gkh_lineEdit.text()]):
                bac_m_lab_gkh = float(self.ui.bac_m_lab_gkh_lineEdit.text())
                volume_lab_gkh = float(self.ui.volume_lab_gkh_lineEdit.text())
                time_lab_gkh = float(self.ui.time_lab_gkh_lineEdit.text())
                lab_gkh_result = lab_gkh(bac_m_lab_gkh, volume_lab_gkh, time_lab_gkh)
                self.ui.lab_gkh_TE.clear()
                self.ui.lab_gkh_TE.append(str(lab_gkh_result))
                """TODO: сделать перевод между ЕИ"""
        except ValueError:
            self.ui.lab_gkh_TE.clear()
            self.ui.lab_gkh_TE.append('Введите цифры!')

    def input_field_gkh(self):
        try:
            if all(float(i) for i in [self.ui.height_field_gkh_lineEdit.text(), self.ui.len_field_gkh_lineEdit.text(), self.ui.time_field_gkh_lineEdit.text(), self.ui.ppm_filed_gkh_lineEdit.text()]):
                high_field_gkh = float(self.ui.height_field_gkh_lineEdit.text())
                len_field_gkh = float(self.ui.len_field_gkh_lineEdit.text())
                time_field_gkh = float(self.ui.time_field_gkh_lineEdit.text())
                ppm_filed_gkh = float(self.ui.ppm_filed_gkh_lineEdit.text())
                field_gkh_result = field_gkh(high_field_gkh, len_field_gkh, time_field_gkh, ppm_filed_gkh)
                self.ui.field_gkh_TE.clear()
                self.ui.field_gkh_TE.append(str(field_gkh_result))
        except ValueError:
            self.ui.field_gkh_TE.clear()
            self.ui.field_gkh_TE.append('Введите цифры!')

    def input_lab_titr(self):
        try:
            if all(float(i) for i in [self.ui.CHCl_lab_titr_lineEdit.text(), self.ui.CNaOH_lab_titr_lineEdit.text(), self.ui.bac_m_lab_titr_lineEdit.text()]):
                cNaOH_lab_titr = float(self.ui.CHCl_lab_titr_lineEdit.text())
                cHCl_lab_titr = float(self.ui.bac_m_lab_titr_lineEdit.text())
                bac_m_lab_titr = float(self.ui.CNaOH_lab_titr_lineEdit.text())
                lab_titr_result = lab_titr(cNaOH_lab_titr, cHCl_lab_titr, bac_m_lab_titr)
                self.ui.lab_titr_TE.clear()
                self.ui.lab_titr_TE.append(str(lab_titr_result))
                """TODO: сделать перевод между ЕИ"""
        except ValueError:
            self.ui.lab_titr_TE.clear()
            self.ui.lab_titr_TE.append('Введите цифры!')

    def input_field_co2(self):
        try:
            if all(float(i) for i in [self.ui.diametr_field_co2_lineEdit.text(), self.ui.height_field_co2_lineEdit.text(), self.ui.time_field_co2_lineEdit.text(), self.ui.ppm_field_co2_lineEdit.text()]):
                diametr_field_gkh = float(self.ui.diametr_field_co2_lineEdit.text())
                high_field_gkh = float(self.ui.height_field_co2_lineEdit.text())
                time_field_gkh = float(self.ui.time_field_co2_lineEdit.text())
                ppm_field_gkh = float(self.ui.ppm_field_co2_lineEdit.text())
                field_co2_result = field_co2(diametr_field_gkh, high_field_gkh, time_field_gkh, ppm_field_gkh)
                self.ui.field_co2_TE.clear()
                self.ui.field_co2_TE.append(str(field_co2_result))
        except ValueError:
            self.ui.field_co2_TE.clear()
            self.ui.field_co2_TE.append('Введите цифры!')

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