# PyQt import
from PyQt5 import QtWidgets

# Additional modules import
from App_UI import Ui_MainWindow
import eval_functools as evf
import exel_functools as exf


# GUI executable class
class MainWindow(object):
    """TODO: make src files for img"""
    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.stackedWidget.showFullScreen()
        self.ui.home.showFullScreen()

        self.buttons()

    # showing application
    def show(self):
        self.main_window.show()

    # initializing buttons
    def buttons(self):
        # home screen buttons
        self.ui.lab_gkh_btn.clicked.connect(self.switch_to_lab_gkh)
        self.ui.lab_titr_btn.clicked.connect(self.switch_to_lab_titr)
        self.ui.field_co2_btn.clicked.connect(self.switch_to_field_co2)
        self.ui.field_gkh_btn.clicked.connect(self.switch_to_field_gkh)
        self.ui.exel_menu_btn.clicked.connect(self.switch_to_exel)
        # exel menu buttons
        self.ui.exel_lab_gkh_btn.clicked.connect(self.switch_exel_lab_gkh)
        self.ui.exel_lab_titr_btn.clicked.connect(self.switch_exel_lab_titr)
        self.ui.exel_field_co2_btn.clicked.connect(self.switch_exel_field_co2)
        # back buttons
        self.ui.lab_gkh_back_home_btn.clicked.connect(self.back_home)
        self.ui.lab_titr_back_home_btn.clicked.connect(self.back_home)
        self.ui.field_co2_back_home_btn.clicked.connect(self.back_home)
        self.ui.field_gkh_back_home_btn.clicked.connect(self.back_home)
        self.ui.exel_back_home_btn.clicked.connect(self.back_home)
        self.ui.exel_lab_gkh_back_btn.clicked.connect(self.back_home)
        self.ui.exel_lab_titr_back_btn.clicked.connect(self.back_home)
        self.ui.exel_field_co2_back_btn.clicked.connect(self.back_home)
        # input buttons
        self.ui.input_lab_gkh.clicked.connect(self.input_lab_gkh)
        self.ui.input_lab_titr_btn.clicked.connect(self.input_lab_titr)
        self.ui.input_field_co2_btn.clicked.connect(self.input_field_co2)
        self.ui.input_field_gkh_btn.clicked.connect(self.input_field_gkh)
        # load file buttons
        self.ui.exel_lab_gkh_loadfile_btn.clicked.connect(self.exel_lab_gkh_open_file_dialog)
        self.ui.exel_lab_titr_loadfile_btn.clicked.connect(self.exel_lab_titr_open_file_dialog)
        self.ui.exel_field_co2_loadfile_btn.clicked.connect(self.exel_field_co2_open_file_dialog)
        # calculate buttons
        self.ui.exel_lab_gkh_startcalculate_btn.clicked.connect(self.lab_gkh_calculate_exel_tabel)
        self.ui.exel_lab_titr_startcalculate_btn.clicked.connect(self.lab_titr_calculate_exel_table)
        self.ui.exel_field_co2_startcalculate_btn.clicked.connect(self.field_co2_calculate_exel_table)

    def input_lab_gkh(self):
        # use try-except in order to check user's input
        try:
            if all(float(i) for i in [self.ui.cCO2_lab_gkh_hol_le.text(), self.ui.cCO2_lab_gkh_soil_le.text(),
                                      self.ui.air_vol_lab_gkh_le.text(), self.ui.inc_temp_lab_gkh_le.text(),
                                      self.ui.pres_lab_gkh_le.text(), self.ui.soil_nav_lab_gkh_le.text(),
                                      self.ui.soil_hum_lab_gkh_le.text(), self.ui.inc_time_lab_gkh_le.text()]):
                # convert all string type to float
                x = float(self.ui.cCO2_lab_gkh_hol_le.text())
                o = float(self.ui.cCO2_lab_gkh_soil_le.text())
                b1 = float(self.ui.air_vol_lab_gkh_le.text())
                t = float(self.ui.inc_temp_lab_gkh_le.text())
                d = float(self.ui.pres_lab_gkh_le.text())
                m = float(self.ui.soil_nav_lab_gkh_le.text())
                b2 = float(self.ui.soil_hum_lab_gkh_le.text())
                e = float(self.ui.inc_time_lab_gkh_le.text())
                ra = evf.lab_gkh(x, o, b1, t, d, m, b2, e)   # measure in mcgCO2/(g*h)
                if self.ui.gram_lab_gkh_RB.isChecked():
                    self.ui.output_lab_gkh_te.clear()
                    self.ui.output_lab_gkh_te.setText(str(ra))
                elif self.ui.sq_meters_lab_gkh_RB.isChecked():
                    # function that will convert mcg_of_CO2/(gr*h) to g_of_CO2/(m2*h)
                    ra = evf.converter_from_GPerGH_to_GPerM2H(ra, "micro")
                    self.ui.output_lab_gkh_te.clear()
                    self.ui.output_lab_gkh_te.setText(str(ra))
                elif self.ui.mcg_sq_meters_lab_gkh_RB.isChecked():   # convert mcgCO2/(g*h) to mcgCO2/(m2*h)
                    self.ui.output_lab_gkh_te.clear()
                    ra = evf.converter_from_GPerGH_to_GPerM2H(ra, "no")
                    self.ui.output_lab_gkh_te.setText(str(ra))
        except ValueError:
            self.ui.output_lab_gkh_te.clear()
            self.ui.output_lab_gkh_te.setText('Введите цифры или же используйте точку, вместо запятой!')

    def input_lab_titr(self):
        # use try-except in order to check user's input
        try:
            if all(float(i) for i in [self.ui.vol_titr_lab_hol_le.text(), self.ui.vol_titr_lab_exp_le.text(),
                                      self.ui.soil_m_lab_titr_le.text(), self.ui.inc_temp_lab_titr_le.text()]):
                # convert all string type to float
                x = float(self.ui.vol_titr_lab_hol_le.text())
                o = float(self.ui.vol_titr_lab_exp_le.text())
                m = float(self.ui.soil_m_lab_titr_le.text())
                e = float(self.ui.inc_temp_lab_titr_le.text())
                ra = evf.lab_titr(x, o, m, e)    # measure in mgCO2/(g*h)
                if self.ui.gram_lab_titr_RB.isChecked():
                    self.ui.output_lab_titr_te.clear()
                    self.ui.output_lab_titr_te.append(str(ra))
                elif self.ui.mcg_gram_lab_titr_RB.isChecked():   # convert mgCO2/(g*h) to mcgCO2/(g*h)
                    self.ui.output_lab_titr_te.clear()
                    ra *= 1000
                    self.ui.output_lab_titr_te.append(str(ra))
                elif self.ui.sq_meters_lab_titr_RB.isChecked():  # convert mgCO2/(g*h) to gCO2/(m2*h)
                    self.ui.output_lab_titr_te.clear()
                    ra = evf.converter_from_GPerGH_to_GPerM2H(ra, "milli")
                    self.ui.output_lab_titr_te.append(str(ra))
                elif self.ui.mcg_sq_meters_lab_titr_RB.isChecked():  # convert mgCO2/(g*h)to mcgCo2/(m2 * h)
                    self.ui.output_lab_titr_te.clear()
                    ra = evf.converter_from_GPerGH_to_GPerM2H(ra, "mcgPerM")
                    self.ui.output_lab_titr_te.append(str(ra))

        except ValueError:
            self.ui.output_lab_titr_te.clear()
            self.ui.output_lab_titr_te.append('Введите цифры или же используйте точку, вместо запятой!')

    def input_field_co2(self):
        # use try-except in order to check user's input
        try:
            if all(float(i) for i in [self.ui.cCO2_before_field_co2_le.text(), self.ui.cCO2_after_field_co2_le.text(),
                                      self.ui.camera_h_field_co2_le.text(), self.ui.camera_d_field_co2_le.text(),
                                      self.ui.temp_field_co2_le.text(), self.ui.inc_time_field_co2_le.text()]):
                # convert all string type to float
                x = float(self.ui.cCO2_before_field_co2_le.text())
                o = float(self.ui.cCO2_after_field_co2_le.text())
                h = float(self.ui.camera_h_field_co2_le.text())
                d = float(self.ui.camera_d_field_co2_le.text())
                t = float(self.ui.temp_field_co2_le.text())
                e = float(self.ui.inc_time_field_co2_le.text())
                ra = evf.field_co2(x, o, h, d, t, e)     # measure in gCO2/(m2*h)
                if self.ui.sq_meters_field_co2_RB.isChecked():
                    self.ui.output_field_co2_te.clear()
                    self.ui.output_field_co2_te.append(str(ra))

                if self.ui.mcg_gram_field_co2_RB.isChecked():    # convert gCO2/(m2*h) to mcgCO2/(g*h)
                    self.ui.output_field_co2_te.clear()
                    ra = evf.converter_from_GPerM2H_to_GPerGH(ra, "micro")
                    self.ui.output_field_co2_te.append(str(ra))

                if self.ui.mg_gram_field_co2_RB.isChecked():     # convert gCO2/(m2*h) to mgCO2/(m2*h)
                    self.ui.output_field_co2_te.clear()
                    ra = evf.converter_from_GPerM2H_to_GPerGH(ra, "milli")
                    self.ui.output_field_co2_te.append(str(ra))

                if self.ui.g_gram_field_co2_RB.isChecked():  # convert gCO2/(m2*h) to gCO2/(g*h)
                    self.ui.output_field_co2_te.clear()
                    ra = evf.converter_from_GPerM2H_to_GPerGH(ra, "no")
                    self.ui.output_field_co2_te.append(str(ra))

                if self.ui.mcg_sq_meters_field_co2_RB.isChecked():   # convert gCO2/(m2*h) to mcgCO2/(m2*h)
                    self.ui.output_field_co2_te.clear()
                    ra *= 10**6
                    self.ui.output_field_co2_te.append(str(ra))
        except ValueError:
            self.ui.output_field_co2_te.clear()
            self.ui.output_field_co2_te.append('Введите цифры или же используйте точку, вместо запятой!')

    def input_field_gkh(self):
        # use try-except in order to check user's input
        try:
            if all(float(i) for i in [self.ui.cCO2_before_field_gkh_le.text(),
                                      self.ui.cCO2_after_field_gkh_le.text(),
                                      self.ui.camera_high_field_gkh_le.text(),
                                      self.ui.camera_l1_field_gkh_le.text(),
                                      self.ui.camera_l2_field_gkh_le.text(),
                                      self.ui.temp_field_gkh_le.text(),
                                      self.ui.inc_time_field_gkh_le.text()]):
                x = float(self.ui.cCO2_before_field_gkh_le.text())
                o = float(self.ui.cCO2_after_field_gkh_le.text())
                h = float(self.ui.camera_high_field_gkh_le.text())
                l1 = float(self.ui.camera_l1_field_gkh_le.text())
                l2 = float(self.ui.camera_l2_field_gkh_le.text())
                t = float(self.ui.temp_field_gkh_le.text())
                e = float(self.ui.inc_time_field_gkh_le.text())
                ra = evf.field_gkh(x, o, h, l1, l2, t, e)    # measure in gCO2/(m2*h)
                if self.ui.sq_meters_field_gkh_RB.isChecked():
                    self.ui.output_field_gkh_te.clear()
                    self.ui.output_field_gkh_te.append(str(ra))

                if self.ui.mcg_gram_field_gkh_RB.isChecked():    # convert gCO2/(m2*h) to mcgCO2/(g*h)
                    self.ui.output_field_gkh_te.clear()
                    ra = evf.converter_from_GPerM2H_to_GPerGH(ra, "micro")
                    self.ui.output_field_gkh_te.append(str(ra))

                if self.ui.mg_gram_field_gkh_RB.isChecked():     # convert gCO2/(m2*h) to mgCO2/(g*h)
                    self.ui.output_field_gkh_te.clear()
                    ra = evf.converter_from_GPerM2H_to_GPerGH(ra, "milli")
                    self.ui.output_field_gkh_te.append(str(ra))

                if self.ui.g_gram_field_gkh_RB.isChecked():  # convert gCO2/(m2*h) to gCO2/(g*h)
                    self.ui.output_field_gkh_te.clear()
                    ra = evf.converter_from_GPerM2H_to_GPerGH(ra, "no")
                    self.ui.output_field_gkh_te.append(str(ra))

                if self.ui.mcg_sq_meters_field_gkh_RB.isChecked():   # convert gCO2/(m2*h) to mcgCO2/(m2*h)
                    self.ui.output_field_gkh_te.clear()
                    ra *= 10**6
                    self.ui.output_field_gkh_te.append(str(ra))

        except ValueError:
            self.ui.output_field_gkh_te.clear()
            self.ui.output_field_gkh_te.append('Введите цифры или же используйте точку, вместо запятой!')

    def exel_lab_gkh_open_file_dialog(self):
        """TODO: make error_widgets for errors during handling exel-files"""
        filepath = QtWidgets.QFileDialog.getOpenFileName()
        if filepath[0]:
            self.ui.exel_lab_gkh_filepath_le.clear()
            self.ui.exel_lab_gkh_filepath_le.setText(filepath[0])
        else:
            self.ui.exel_lab_gkh_filepath_le.clear()
            self.ui.exel_lab_gkh_filepath_le.setText("Вы не выбрали файл")

    def exel_lab_titr_open_file_dialog(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName()
        if filepath[0]:
            self.ui.exel_lab_titr_filepath_le.clear()
            self.ui.exel_lab_titr_filepath_le.setText(filepath[0])
        else:
            self.ui.exel_lab_titr_filepath_le.clear()
            self.ui.exel_lab_titr_filepath_le.setText("Вы не выбрали файл")

    def exel_field_co2_open_file_dialog(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName()
        if filepath[0]:
            self.ui.exel_field_co2_filepath_le.clear()
            self.ui.exel_field_co2_filepath_le.setText(filepath[0])
        else:
            self.ui.exel_field_co2_filepath_le.clear()
            self.ui.exel_field_co2_filepath_le.setText("Вы не выбрали файл")

    # switch buttons from home page
    def switch_to_lab_gkh(self):
        self.ui.lab_gkh_eval_lt.showFullScreen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.lab_gkh_eval_lt)

    def switch_to_lab_titr(self):
        self.ui.lab_titr_eval_lt.showFullScreen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.lab_titr_eval_lt)

    def switch_to_field_gkh(self):
        self.ui.field_gkh_eval_lt.showFullScreen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.field_gkh_eval_lt)

    def switch_to_field_co2(self):
        self.ui.field_co2_eval_lt.showFullScreen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.field_co2_eval_lt)

    def switch_to_exel(self):
        self.ui.exel_menu_lt.showFullScreen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.exel_menu_lt)

    # switch buttons from exel page
    def switch_exel_lab_gkh(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.exel_lab_gkh_lt)

    def switch_exel_lab_titr(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.exel_lab_titr_lt)

    def switch_exel_field_co2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.exel_field_co2_lt)

    # calculation buttons
    def lab_gkh_calculate_exel_tabel(self):
        measure = None
        if self.ui.exel_mcg_lab_gkh_rb.isChecked():
            measure = "no"
        elif self.ui.exel_sq_meters_lab_gkh_rb.isChecked():
            measure = "gCO2perM2H"
        elif self.ui.exe_mcg_sq_meters_lab_gkh_rb.isChecked():
            measure = "mcgCO2perM2H"
        exf.exel_lab_gkh_eval(rf"{self.ui.exel_lab_gkh_filepath_le.text()}", measure)

    def lab_titr_calculate_exel_table(self):
        measure = None
        if self.ui.exel_mg_lab_titr_rb.isChecked():
            measure = "no"
        elif self.ui.exel_mcg_lab_titr_rb.isChecked():
            measure = "mcgCO2perGH"
        elif self.ui.exel_sq_meters_lab_titr_rb.isChecked():
            measure = "gCO2perM2H"
        elif self.ui.exel_mcg_sq_meters_lab_titr_rb.isChecked():
            measure = "mcgCO2perM2H"
        exf.exel_lab_titr_eval(rf"{self.ui.exel_lab_titr_filepath_le.text()}", measure)

    def field_co2_calculate_exel_table(self):
        measure = None
        if self.ui.exel_sq_meters_field_co2_RB.isChecked():
            measure = "no"
        elif self.ui.exel_mcg_gram_field_co2_RB.isChecked():
            measure = "mcgCO2perGH"
        elif self.ui.exel_mg_gram_field_co2_RB.isChecked():
            measure = "mgCO2perGH"
        elif self.ui.exel_g_gram_field_co2_RB.isChecked():
            measure = "gCO2perGH"
        elif self.ui.exel_mcg_sq_meters_field_co2_RB.isChecked():
            measure = "mcgCO2perM2H"
        exf.exel_field_co2_eval(rf"{self.ui.exel_field_co2_filepath_le.text()}", measure)

    # back to home button
    def back_home(self):
        self.ui.home.showFullScreen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
