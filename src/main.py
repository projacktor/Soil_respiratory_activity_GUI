from PyQt5 import QtWidgets
from src.ui.main_Ui import MainWindow


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
