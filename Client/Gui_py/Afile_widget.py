# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\download_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(759, 60)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(3, 9, 3, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_name = QtWidgets.QLabel(Form)
        self.file_name.setMinimumSize(QtCore.QSize(693, 40))
        self.file_name.setMaximumSize(QtCore.QSize(693, 40))
        self.file_name.setStyleSheet("QLabel {\n"
"font: 63 12pt \"Open Sans Semibold\";\n"
"    color:rgb(0, 44, 65);\n"
"}")
        self.file_name.setObjectName("file_name")
        self.horizontalLayout.addWidget(self.file_name)
        self.download_file_button = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_file_button.sizePolicy().hasHeightForWidth())
        self.download_file_button.setSizePolicy(sizePolicy)
        self.download_file_button.setMinimumSize(QtCore.QSize(40, 40))
        self.download_file_button.setMaximumSize(QtCore.QSize(40, 40))
        self.download_file_button.setStyleSheet("QPushButton {\n"
"color: #0FA15F;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"size: 45x45;\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.977273, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255))\n"
"}")
        self.download_file_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/data-transfer-download-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_file_button.setIcon(icon)
        self.download_file_button.setIconSize(QtCore.QSize(16, 16))
        self.download_file_button.setCheckable(True)
        self.download_file_button.setAutoExclusive(False)
        self.download_file_button.setObjectName("download_file_button")
        self.horizontalLayout.addWidget(self.download_file_button)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.file_name.setText(_translate("Form", "f"))
        self.download_file_button.setAccessibleDescription(_translate("Form", "download from available files"))
import icons_rc
