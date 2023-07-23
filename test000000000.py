# # -*- coding: utf-8 -*-

# # Form implementation generated from reading ui file 'test000000000.ui'
# #
# # Created by: PyQt5 UI code generator 5.13.0
# #
# # WARNING! All changes made in this file will be lost!


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(583, 300)
#         self.gridLayout = QtWidgets.QGridLayout(Form)
#         self.gridLayout.setObjectName("gridLayout")
#         self.comboBox_2 = QtWidgets.QComboBox(Form)
#         self.comboBox_2.setObjectName("comboBox_2")
#         self.comboBox_2.addItem("")
#         self.comboBox_2.addItem("")
#         self.gridLayout.addWidget(self.comboBox_2, 1, 0, 1, 1)
#         self.comboBox = QtWidgets.QComboBox(Form)
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
#         self.pushButton_10 = QtWidgets.QPushButton(Form)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
#         self.pushButton_10.setSizePolicy(sizePolicy)
#         self.pushButton_10.setMinimumSize(QtCore.QSize(0, 22))
#         self.pushButton_10.setMaximumSize(QtCore.QSize(16777215, 22))
#         font = QtGui.QFont()
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton_10.setFont(font)
#         self.pushButton_10.setStyleSheet("")
#         self.pushButton_10.setCheckable(False)
#         self.pushButton_10.setDefault(True)
#         self.pushButton_10.setFlat(True)
#         self.pushButton_10.setObjectName("pushButton_10")
#         self.gridLayout.addWidget(self.pushButton_10, 2, 0, 1, 1)

#         self.retranslateUi(Form)
#         self.comboBox.currentIndexChanged['int'].connect(self.comboBox_2.setCurrentIndex)
#         self.comboBox_2.currentIndexChanged['int'].connect(self.comboBox.setCurrentIndex)
#         self.comboBox.activated['QString'].connect(self.pushButton_10.animateClick)
#         QtCore.QMetaObject.connectSlotsByName(Form)

#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.comboBox_2.setItemText(0, _translate("Form", "333"))
#         self.comboBox_2.setItemText(1, _translate("Form", "444"))
#         self.comboBox.setItemText(0, _translate("Form", "111"))
#         self.comboBox.setItemText(1, _translate("Form", "222"))
#         self.pushButton_10.setText(_translate("Form", "Расчет"))
#         self.pushButton_10.setShortcut(_translate("Form", "Return"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())


# p = 5
# def xx(x):
#     print(x + ' =', eval(x))
# # xx('p')
# # help(p)
# print(p.__var__)

# # print('pppp ===', p)

# import django
# print(django.get_version())

import math

# fff = '%.3e %'.format(0.0000123456789)
fff = '%.3e' % 0.0000123456789
# fff = round(fff, 2)
print('fff = ', fff)