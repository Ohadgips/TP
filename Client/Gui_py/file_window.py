# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Files_Window(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(774, 568)
        Dialog.setMinimumSize(QtCore.QSize(774, 568))
        Dialog.setMaximumSize(QtCore.QSize(774, 568))
        Dialog.setStyleSheet("QDialog{\n"
"color: rgb(255, 255, 255);\n"
"background: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setMinimumSize(QtCore.QSize(770, 53))
        self.widget_3.setMaximumSize(QtCore.QSize(779, 53))
        self.widget_3.setStyleSheet("QWidget {\n"
"        background-color: rgb(0, 44, 65);\n"
"        border: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.238636 rgba(255, 255, 255, 0));\n"
"    }\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setAccessibleName("")
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("QLabel {\n"
"font: 63 28pt \"Open Sans Semibold\";\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QWidget {\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.977273, y2:0, stop:0.136364 rgba(0, 44, 65, 255), stop:0.511364 rgba(10, 161, 93, 255), stop:0.892045 rgba(0, 44, 65, 255));\n"
"        border: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.238636 rgba(255, 255, 255, 0));\n"
"    }")
        self.label_3.setLineWidth(1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setStyleSheet("QListWidget\n"
"{\n"
"background : rgb(255, 255, 255);\n"
"}\n"
"      QListWidget QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"            background-color: rgb(255, 255, 255);\n"
"            width:10px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"     QListWidget QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 0px solid red;\n"
"            border-radius: 4px;\n"
"            background-color: rgb(15, 161, 95);\n"
"        }\n"
"        QListWidget QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QListWidget QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"\n"
" QListView::item:selected\n"
"{\n"
"background : rgb(197, 197, 197);\n"
"}\n"
" QListView::item{\n"
"color: rgb(0, 44, 65);\n"
" font: 63 10pt \"Open Sans Semibold\";\n"
"}")
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget_2.setLineWidth(0)
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setBatchSize(1)
        self.listWidget_2.setWordWrap(False)
        self.listWidget_2.setSelectionRectVisible(True)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 4, 4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setMinimumSize(QtCore.QSize(40, 40))
        self.ok_button.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        self.ok_button.setFont(font)
        self.ok_button.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"width: 45px;\n"
"height: 45px;\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.977273, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255));\n"
"}")
        self.ok_button.setIconSize(QtCore.QSize(16, 16))
        self.ok_button.setCheckable(True)
        self.ok_button.setAutoExclusive(True)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 0, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setMinimumSize(QtCore.QSize(100, 40))
        self.cancel_button.setMaximumSize(QtCore.QSize(100, 40))
        self.cancel_button.setBaseSize(QtCore.QSize(0, 0))
        self.cancel_button.setAutoExclusive(True)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"width: 45px;\n"
"height: 45px;\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.977273, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255));\n"
"}")
        self.cancel_button.setIconSize(QtCore.QSize(16, 16))
        self.cancel_button.setCheckable(True)
        self.cancel_button.setAutoExclusive(False)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.listWidget_2.itemSelectionChanged.connect(self.ok_button_change)
        self.listWidget_2.setCurrentRow(-1)
        self.cancel_button.toggled['bool'].connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #self.ok_button.clicked.connect(self.on_button_clicked)
        self.ok_button.clicked.connect(Dialog.accept)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Available Files"))
        self.listWidget_2.setSortingEnabled(True)
        self.ok_button.setAccessibleDescription(_translate("Dialog", "download from available files"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setAccessibleDescription(_translate("Dialog", "download from available files"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))

    def ok_button_change(self):
        if self.listWidget_2.selectedItems():
            self.ok_button.setEnabled(True)
        else:
            self.ok_button.setEnabled(False)
        
        
           
import icons_rc


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Files_Window()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""