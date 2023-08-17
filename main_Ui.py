from PyQt5 import QtWidgets
from App_UI import Ui_MainWindow
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
        self.ui.lab_gkh_btn.clicked.connect(self.switch_to_lab_gkh)
        self.ui.lab_titr_btn.clicked.connect(self.switch_to_lab_titr)
        self.ui.field_co2_btn.clicked.connect(self.switch_to_field_co2)
        self.ui.field_gkh_btn.clicked.connect(self.switch_to_field_gkh)
        self.ui.Exel.clicked.connect(self.switch_to_exel)
        # back buttons
        self.ui.lab_gkh_back_home_btn.clicked.connect(self.back_home)
        self.ui.lab_titr_back_home_btn.clicked.connect(self.back_home)
        self.ui.field_co2_back_home_btn.clicked.connect(self.back_home)
        self.ui.field_gkh_back_home_btn.clicked.connect(self.back_home)
        self.ui.exel_back_home_btn.clicked.connect(self.back_home)
        # input buttons
        self.ui.input_lab_gkh.clicked.connect(self.input_lab_gkh)
        self.ui.input_lab_titr_btn.clicked.connect(self.input_lab_titr)
        self.ui.input_field_co2_btn.clicked.connect(self.input_field_co2)
        self.ui.input_field_gkh_btn.clicked.connect(self.input_field_gkh)

    def input_lab_gkh(self):
        try:
            if all(float(i) for i in [self.ui.cCO2_lab_gkh_hol_le.text(), self.ui.cCO2_lab_gkh_soil_le.text(),
                                      self.ui.air_vol_lab_gkh_le.text(), self.ui.inc_temp_lab_gkh_le.text(),
                                      self.ui.pres_lab_gkh_le.text(), self.ui.soil_nav_lab_gkh_le.text(),
                                      self.ui.soil_hum_lab_gkh_le.text(), self.ui.inc_time_lab_gkh_le.text()]):
                x = float(self.ui.cCO2_lab_gkh_hol_le.text())
                o = float(self.ui.cCO2_lab_gkh_soil_le.text())
                b1 = float(self.ui.air_vol_lab_gkh_le.text())
                t = float(self.ui.inc_temp_lab_gkh_le.text())
                d = float(self.ui.pres_lab_gkh_le.text())
                m = float(self.ui.soil_nav_lab_gkh_le.text())
                b2 = float(self.ui.soil_hum_lab_gkh_le.text())
                e = float(self.ui.inc_time_lab_gkh_le.text())
                RA = lab_gkh(x, o, b1, t, d, m, b2, e) # measure in mcgCO2/(g*h)
                if self.ui.gram_lab_gkh_RB.isChecked():
                    self.ui.output_lab_gkh_te.clear()
                    self.ui.output_lab_gkh_te.setText(str(RA))
                elif self.ui.sq_meters_lab_gkh_RB.isChecked():
                    # function that will convert mcg_of_CO2/(gr*h) to g_of_CO2/(m2*h)
                    RA = converter_from_GPerGH_to_GPerM2H(RA, "micro")
                    self.ui.output_lab_gkh_te.clear()
                    self.ui.output_lab_gkh_te.setText(str(RA))
                elif self.ui.mcg_sq_meters_lab_gkh_RB.isChecked(): # convert mcgCO2/(g*h) to mcgCO2/(m2*h)
                    self.ui.output_lab_gkh_te.clear()
                    RA = converter_from_GPerGH_to_GPerM2H(RA, "no")
                    self.ui.output_lab_gkh_te.setText(str(RA))
        except ValueError:
            self.ui.output_lab_gkh_te.clear()
            self.ui.output_lab_gkh_te.setText('Введите цифры или же используйте точку, вместо запятой!')

    def input_lab_titr(self):
        try:
            if all(float(i) for i in [self.ui.vol_titr_lab_hol_le.text(), self.ui.vol_titr_lab_exp_le.text(),
                                      self.ui.soil_m_lab_titr_le.text(), self.ui.inc_temp_lab_titr_le.text()]):
                x = float(self.ui.vol_titr_lab_hol_le.text())
                o = float(self.ui.vol_titr_lab_exp_le.text())
                m = float(self.ui.soil_m_lab_titr_le.text())
                e = float(self.ui.inc_temp_lab_titr_le.text())
                RA = lab_titr(x, o, m, e) # measure in mgCO2/(g*h)
                if self.ui.gram_lab_titr_RB.isChecked():
                    self.ui.output_lab_titr_te.clear()
                    self.ui.output_lab_titr_te.append(str(RA))
                elif self.ui.mcg_gram_lab_titr_RB.isChecked(): # convert mgCO2/(g*h) to mcgCO2/(g*h)
                    self.ui.output_lab_titr_te.clear()
                    RA *= 1000
                    self.ui.output_lab_titr_te.append(str(RA))
                elif self.ui.sq_meters_lab_titr_RB.isChecked(): # convert mgCO2/(g*h) to gCO2/(m2*h)
                    self.ui.output_lab_titr_te.clear()
                    RA = converter_from_GPerGH_to_GPerM2H(RA, "milli")
                    self.ui.output_lab_titr_te.append(str(RA))
                elif self.ui.mcg_sq_meters_lab_titr_RB.isChecked(): # convert mgCO2/(g*h)to mcgCo2/(m2 * h)
                    self.ui.output_lab_titr_te.clear()
                    RA = converter_from_GPerGH_to_GPerM2H(RA, "mcgPerM")
                    self.ui.output_lab_titr_te.append(str(RA))
        except ValueError:
            self.ui.output_lab_titr_te.clear()
            self.ui.output_lab_titr_te.append('Введите цифры или же используйте точку, вместо запятой!')

    def input_field_co2(self):
        try:
            if all(float(i) for i in [self.ui.cCO2_before_field_co2_le.text(), self.ui.cCO2_after_field_co2_le.text(),
                                      self.ui.camera_h_field_co2_le.text(), self.ui.camera_d_field_co2_le.text(),
                                      self.ui.temp_field_co2_le.text(), self.ui.inc_time_field_co2_le.text()]):
                x = float(self.ui.cCO2_before_field_co2_le.text())
                o = float(self.ui.cCO2_after_field_co2_le.text())
                h = float(self.ui.camera_h_field_co2_le.text())
                d = float(self.ui.camera_d_field_co2_le.text())
                t = float(self.ui.temp_field_co2_le.text())
                e = float(self.ui.inc_time_field_co2_le.text())
                RA = field_co2(x, o, h, d, t, e) # measure in gCO2/(m2*h)
                if self.ui.sq_meters_field_co2_RB.isChecked():
                    self.ui.output_field_co2_te.clear()
                    self.ui.output_field_co2_te.append(str(RA))

                if self.ui.mcg_gram_field_co2_RB.isChecked(): # convert gCO2/(m2*h) to mcgCO2/(g*h)
                    self.ui.output_field_co2_te.clear()
                    RA = converter_from_GPerM2H_to_GPerGH(RA, "micro")
                    self.ui.output_field_co2_te.append(str(RA))

                if self.ui.mg_gram_field_co2_RB.isChecked(): # convert gCO2/(m2*h) to mgCO2/(m2*h)
                    self.ui.output_field_co2_te.clear()
                    RA = converter_from_GPerM2H_to_GPerGH(RA, "milli")
                    self.ui.output_field_co2_te.append(str(RA))

                if self.ui.g_gram_field_co2_RB.isChecked(): # convert gCO2/(m2*h) to gCO2/(g*h)
                    self.ui.output_field_co2_te.clear()
                    RA = converter_from_GPerM2H_to_GPerGH(RA, "no")
                    self.ui.output_field_co2_te.append(str(RA))

                if self.ui.mcg_sq_meters_field_co2_RB.isChecked(): # convert gCO2/(m2*h) to mcgCO2/(m2*h)
                    self.ui.output_field_co2_te.clear()
                    RA *= 10**6
                    self.ui.output_field_co2_te.append(str(RA))
        except ValueError:
            self.ui.output_field_co2_te.clear()
            self.ui.output_field_co2_te.append('Введите цифры или же используйте точку, вместо запятой!')

    def input_field_gkh(self):
        try:
            if all(float(i) for i in [self.ui.cCO2_before_field_gkh_le.text(), self.ui.cCO2_after_field_gkh_le.text(),
                                      self.ui.camera_high_field_gkh_le.text(), self.ui.camera_l1_field_gkh_le.text(),
                                      self.ui.camera_l2_field_gkh_le.text(), self.ui.temp_field_gkh_le.text(),
                                      self.ui.inc_time_field_gkh_le.text()]):
                x = float(self.ui.cCO2_before_field_gkh_le.text())
                o = float(self.ui.cCO2_after_field_gkh_le.text())
                h = float(self.ui.camera_high_field_gkh_le.text())
                l1 = float(self.ui.camera_l1_field_gkh_le.text())
                l2 = float(self.ui.camera_l2_field_gkh_le.text())
                t = float(self.ui.temp_field_gkh_le.text())
                e = float(self.ui.inc_time_field_gkh_le.text())
                RA = field_gkh(x, o, h, l1, l2, t, e) # measure in gCO2/(m2*h)
                if self.ui.sq_meters_field_gkh_RB.isChecked():
                    self.ui.output_field_gkh_te.clear()
                    self.ui.output_field_gkh_te.append(str(RA))

                if self.ui.mcg_gram_field_gkh_RB.isChecked(): # convert gCO2/(m2*h) to mcgCO2/(g*h)
                    self.ui.output_field_gkh_te.clear()
                    RA = converter_from_GPerM2H_to_GPerGH(RA, "micro")
                    self.ui.output_field_gkh_te.append(str(RA))

                if self.ui.mg_gram_field_gkh_RB.isChecked(): # convert gCO2/(m2*h) to mgCO2/(g*h)
                    self.ui.output_field_gkh_te.clear()
                    RA = converter_from_GPerM2H_to_GPerGH(RA, "milli")
                    self.ui.output_field_gkh_te.append(str(RA))

                if self.ui.g_gram_field_gkh_RB.isChecked(): # convert gCO2/(m2*h) to gCO2/(g*h)
                    self.ui.output_field_gkh_te.clear()
                    RA = converter_from_GPerM2H_to_GPerGH(RA, "no")
                    self.ui.output_field_gkh_te.append(str(RA))

                if self.ui.mcg_sq_meters_field_gkh_RB.isChecked(): # convert gCO2/(m2*h) to mcgCO2/(m2*h)
                    self.ui.output_field_gkh_te.clear()
                    RA *= 10**6
                    self.ui.output_field_gkh_te.append(str(RA))

        except ValueError:
            self.ui.output_field_gkh_te.clear()
            self.ui.output_field_gkh_te.append('Введите цифры или же используйте точку, вместо запятой!')

    def switch_to_lab_gkh(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.lab_gkh_eval_lt)

    def switch_to_lab_titr(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.lab_titr_eval_lt)

    def switch_to_field_gkh(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.field_gkh_eval_lt)

    def switch_to_field_co2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.field_co2_eval_lt)

    def switch_to_exel(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EXEL)

    def back_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
