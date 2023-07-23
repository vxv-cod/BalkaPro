from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from okno_ui import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

if __name__ == "__main__":
    sys.exit(app.exec_())