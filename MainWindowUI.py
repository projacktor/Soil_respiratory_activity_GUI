# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Full.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 10, 771, 581))
        self.stackedWidget.setMinimumSize(QtCore.QSize(771, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(771, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.intro_label = QtWidgets.QLabel(self.home)
        self.intro_label.setGeometry(QtCore.QRect(40, 20, 681, 81))
        self.intro_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.intro_label.setObjectName("intro_label")
        self.field_btn = QtWidgets.QPushButton(self.home)
        self.field_btn.setGeometry(QtCore.QRect(30, 170, 270, 230))
        self.field_btn.setObjectName("field_btn")
        self.lab_btn = QtWidgets.QPushButton(self.home)
        self.lab_btn.setGeometry(QtCore.QRect(460, 170, 271, 231))
        self.lab_btn.setObjectName("lab_btn")
        self.stackedWidget.addWidget(self.home)
        self.lab = QtWidgets.QWidget()
        self.lab.setObjectName("lab")
        self.intr_lab_lable = QtWidgets.QLabel(self.lab)
        self.intr_lab_lable.setGeometry(QtCore.QRect(40, 20, 681, 81))
        self.intr_lab_lable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.intr_lab_lable.setObjectName("intr_lab_lable")
        self.gkh_lab_btn = QtWidgets.QPushButton(self.lab)
        self.gkh_lab_btn.setGeometry(QtCore.QRect(30, 170, 270, 230))
        self.gkh_lab_btn.setObjectName("gkh_lab_btn")
        self.lab_met_btn = QtWidgets.QPushButton(self.lab)
        self.lab_met_btn.setGeometry(QtCore.QRect(460, 170, 270, 230))
        self.lab_met_btn.setObjectName("lab_met_btn")
        self.lab_back_btn = QtWidgets.QPushButton(self.lab)
        self.lab_back_btn.setGeometry(QtCore.QRect(300, 450, 160, 80))
        self.lab_back_btn.setObjectName("lab_back_btn")
        self.stackedWidget.addWidget(self.lab)
        self.field = QtWidgets.QWidget()
        self.field.setObjectName("field")
        self.intr_field_lable = QtWidgets.QLabel(self.field)
        self.intr_field_lable.setGeometry(QtCore.QRect(40, 30, 681, 81))
        self.intr_field_lable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.intr_field_lable.setObjectName("intr_field_lable")
        self.analysis_btn = QtWidgets.QPushButton(self.field)
        self.analysis_btn.setGeometry(QtCore.QRect(460, 170, 270, 230))
        self.analysis_btn.setObjectName("analysis_btn")
        self.gkh_field_btn = QtWidgets.QPushButton(self.field)
        self.gkh_field_btn.setGeometry(QtCore.QRect(30, 170, 270, 230))
        self.gkh_field_btn.setObjectName("gkh_field_btn")
        self.field_back_btn = QtWidgets.QPushButton(self.field)
        self.field_back_btn.setGeometry(QtCore.QRect(300, 450, 160, 80))
        self.field_back_btn.setObjectName("field_back_btn")
        self.stackedWidget.addWidget(self.field)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.intro_label.setText(_translate("MainWindow", "Где было сделано  измерение?"))
        self.field_btn.setText(_translate("MainWindow", "Полевое измерение"))
        self.lab_btn.setText(_translate("MainWindow", "Лабороторное измерение"))
        self.intr_lab_lable.setText(_translate("MainWindow", "Какой метод был использован для измерения респераторной активности в лаборотории?"))
        self.gkh_lab_btn.setText(_translate("MainWindow", "ГХ"))
        self.lab_met_btn.setText(_translate("MainWindow", "титрование"))
        self.lab_back_btn.setText(_translate("MainWindow", "Назад в меню"))
        self.intr_field_lable.setText(_translate("MainWindow", "Какой метод был использован для измерения респераторной активности в поле?"))
        self.analysis_btn.setText(_translate("MainWindow", "Анализ углекислого газа"))
        self.gkh_field_btn.setText(_translate("MainWindow", "ГХ"))
        self.field_back_btn.setText(_translate("MainWindow", "Назад в меню"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())