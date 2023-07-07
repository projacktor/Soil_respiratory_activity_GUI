
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainWindow import Ui_MainWindow


def application():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
