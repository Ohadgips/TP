from PyQt5 import QtCore, QtGui, QtWidgets
from file_window import Files_Window
import sys
sys.path.append("/Client/")
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 599)
        MainWindow.setMinimumSize(QtCore.QSize(1075, 599))
        MainWindow.setMaximumSize(QtCore.QSize(1075, 599))
        MainWindow.setStyleSheet("QMainWindow {\n"
"        background-color: #fff;\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icons_only = QtWidgets.QWidget(self.centralwidget)
        self.icons_only.setStyleSheet("QWidget {\n"
"        background-color: rgb(0, 44, 65);\n"
"        width:50px;\n"
"    }")
        self.icons_only.setObjectName("icons_only")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icons_only)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.icon_big = QtWidgets.QLabel(self.icons_only)
        self.icon_big.setMinimumSize(QtCore.QSize(50, 50))
        self.icon_big.setMaximumSize(QtCore.QSize(50, 50))
        self.icon_big.setBaseSize(QtCore.QSize(50, 50))
        self.icon_big.setStyleSheet("QLabel{\n"
"        height:50px;\n"
"        border:none;\n"
"/*border-bottom: 1px solid #b0b0b0;*/\n"
"}")
        self.icon_big.setText("")
        self.icon_big.setPixmap(QtGui.QPixmap(":/icons/icons/appiconpng.png"))
        self.icon_big.setScaledContents(True)
        self.icon_big.setObjectName("icon_big")
        self.horizontalLayout_3.addWidget(self.icon_big)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upload_button_ico = QtWidgets.QPushButton(self.icons_only)
        self.upload_button_ico.setStyleSheet("QPushButton{\n"
"        height:50px;\n"
"        border:none;\n"
"/*border-bottom: 1px solid #b0b0b0;*/\n"
"}\n"
"QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }")
        self.upload_button_ico.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/upload-3-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/upload-3-48 (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.upload_button_ico.setIcon(icon)
        self.upload_button_ico.setIconSize(QtCore.QSize(20, 20))
        self.upload_button_ico.setCheckable(True)
        self.upload_button_ico.setAutoExclusive(True)
        self.upload_button_ico.setObjectName("upload_button_ico")
        self.verticalLayout.addWidget(self.upload_button_ico)
        self.download_button_ico = QtWidgets.QPushButton(self.icons_only)
        self.download_button_ico.setStyleSheet("QPushButton{\n"
"        height:50px;\n"
"        border:none;\n"
"/*border-bottom: 1px solid #b0b0b0;*/\n"
"}\n"
"QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }")
        self.download_button_ico.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/download-2-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/white down.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.download_button_ico.setIcon(icon1)
        self.download_button_ico.setIconSize(QtCore.QSize(20, 20))
        self.download_button_ico.setCheckable(True)
        self.download_button_ico.setAutoExclusive(True)
        self.download_button_ico.setObjectName("download_button_ico")
        self.verticalLayout.addWidget(self.download_button_ico)
        self.history_button_ico = QtWidgets.QPushButton(self.icons_only)
        self.history_button_ico.setStyleSheet("QPushButton{\n"
"        height:50px;\n"
"        border:none;\n"
"/*border-bottom: 1px solid #b0b0b0;*/\n"
"}\n"
"QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }")
        self.history_button_ico.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/list-ingredients-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/list-ingredients-48 (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.history_button_ico.setIcon(icon2)
        self.history_button_ico.setIconSize(QtCore.QSize(20, 20))
        self.history_button_ico.setCheckable(True)
        self.history_button_ico.setAutoExclusive(True)
        self.history_button_ico.setObjectName("history_button_ico")
        self.verticalLayout.addWidget(self.history_button_ico)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 428, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.settings_button_ico = QtWidgets.QPushButton(self.icons_only)
        self.settings_button_ico.setStyleSheet("QPushButton{\n"
"        height:50px;\n"
"        border:none;\n"
"/*border-bottom: 1px solid #b0b0b0;*/\n"
"}\n"
"QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }")
        self.settings_button_ico.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/settingsG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/settingsW.ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.settings_button_ico.setIcon(icon3)
        self.settings_button_ico.setIconSize(QtCore.QSize(20, 20))
        self.settings_button_ico.setCheckable(True)
        self.settings_button_ico.setAutoExclusive(True)
        self.settings_button_ico.setObjectName("settings_button_ico")
        self.verticalLayout_3.addWidget(self.settings_button_ico)
        self.gridLayout.addWidget(self.icons_only, 0, 0, 1, 1)
        self.full_menu = QtWidgets.QWidget(self.centralwidget)
        self.full_menu.setStyleSheet("QWidget {\n"
"        background-color: rgb(0, 44, 65);\n"
"    }\n"
"QPushButton {\n"
"        border:none;\n"
"        border-radius: 3px;\n"
"        padding: 8px  8px 15px;\n"
"        text-align: left;\n"
"        color: #788596;\n"
"        font: 63 10pt \"Open Sans Semibold\";\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }\n"
"QPushButton:checked {\n"
"        color: #fff;\n"
"    }")
        self.full_menu.setObjectName("full_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icon_small = QtWidgets.QLabel(self.full_menu)
        self.icon_small.setMinimumSize(QtCore.QSize(42, 40))
        self.icon_small.setMaximumSize(QtCore.QSize(42, 40))
        self.icon_small.setStyleSheet("QLabel{\n"
"        padding: 5px;\n"
"        color: #fff;\n"
"}")
        self.icon_small.setText("")
        self.icon_small.setPixmap(QtGui.QPixmap(":/icons/icons/appiconpng.png"))
        self.icon_small.setScaledContents(True)
        self.icon_small.setObjectName("icon_small")
        self.horizontalLayout_2.addWidget(self.icon_small)
        self.menu_label = QtWidgets.QLabel(self.full_menu)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.menu_label.setFont(font)
        self.menu_label.setStyleSheet("QLabel{\n"
"        padding-right: 10px;\n"
"        color: #fff;\n"
"}")
        self.menu_label.setObjectName("menu_label")
        self.horizontalLayout_2.addWidget(self.menu_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.upload_button = QtWidgets.QPushButton(self.full_menu)
        self.upload_button.setIcon(icon)
        self.upload_button.setIconSize(QtCore.QSize(14, 14))
        self.upload_button.setCheckable(True)
        self.upload_button.setAutoExclusive(True)
        self.upload_button.setObjectName("upload_button")
        self.verticalLayout_2.addWidget(self.upload_button)
        self.download_button = QtWidgets.QPushButton(self.full_menu)
        self.download_button.setIcon(icon1)
        self.download_button.setIconSize(QtCore.QSize(14, 14))
        self.download_button.setCheckable(True)
        self.download_button.setAutoExclusive(True)
        self.download_button.setObjectName("download_button")
        self.verticalLayout_2.addWidget(self.download_button)
        self.history_button = QtWidgets.QPushButton(self.full_menu)
        self.history_button.setIcon(icon2)
        self.history_button.setIconSize(QtCore.QSize(14, 14))
        self.history_button.setCheckable(True)
        self.history_button.setAutoExclusive(True)
        self.history_button.setObjectName("history_button")
        self.verticalLayout_2.addWidget(self.history_button)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 422, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.settings_button = QtWidgets.QPushButton(self.full_menu)
        self.settings_button.setIcon(icon3)
        self.settings_button.setIconSize(QtCore.QSize(14, 14))
        self.settings_button.setCheckable(True)
        self.settings_button.setAutoExclusive(True)
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_4.addWidget(self.settings_button)
        self.gridLayout.addWidget(self.full_menu, 0, 1, 1, 1)
        self.main_window = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_window.sizePolicy().hasHeightForWidth())
        self.main_window.setSizePolicy(sizePolicy)
        self.main_window.setObjectName("main_window")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_window)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setWhatsThis("")
        self.widget.setStyleSheet("QWidget {\n"
"        background-color: #f9fafd;\n"
"        border: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.238636 rgba(255, 255, 255, 0))\n"
"    }\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu_button = QtWidgets.QPushButton(self.widget)
        self.menu_button.setStyleSheet("QPushButton {\n"
"        padding: 5px;\n"
"        border: none;\n"
"        width: 30px;\n"
"        height: 30px;\n"
"    }")
        self.menu_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/menu-4-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_button.setIcon(icon4)
        self.menu_button.setIconSize(QtCore.QSize(14, 14))
        self.menu_button.setCheckable(True)
        self.menu_button.setObjectName("menu_button")
        self.horizontalLayout_4.addWidget(self.menu_button)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_tab = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_tab.sizePolicy().hasHeightForWidth())
        self.search_tab.setSizePolicy(sizePolicy)
        self.search_tab.setMinimumSize(QtCore.QSize(0, 0))
        self.search_tab.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.search_tab.setStyleSheet("QLineEdit{\n"
"        border: none;\n"
"        padding: 5px 10px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"        background-color: rgb(229, 229, 229);\n"
"}")
        self.search_tab.setObjectName("search_tab")
        self.horizontalLayout.addWidget(self.search_tab)
        self.search_button = QtWidgets.QPushButton(self.widget)
        self.search_button.setStyleSheet("QPushButton{\n"
"        border: none;\n"
"}")
        self.search_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/search-3-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon5)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.widget)
        self.pages = QtWidgets.QStackedWidget(self.main_window)
        self.pages.setEnabled(True)
        self.pages.setMinimumSize(QtCore.QSize(911, 559))
        self.pages.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pages.setStyleSheet("QWidget {\n"
"        background-color:rgb(255, 255, 255);\n"
"    }")
        self.pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pages.setObjectName("pages")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.home_page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.home_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/icons/pngwing.com (1).png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.home_page)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"font: 63 20pt \"Open Sans Semibold\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.label_4 = QtWidgets.QLabel(self.home_page)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("QLabel {\n"
"font: 63 20pt \"Open Sans Semibold\";\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.pages.addWidget(self.home_page)
        self.Upload_page = QtWidgets.QWidget()
        self.Upload_page.setObjectName("Upload_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Upload_page)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scroll_and_button = QtWidgets.QFrame(self.Upload_page)
        self.scroll_and_button.setMinimumSize(QtCore.QSize(911, 559))
        self.scroll_and_button.setObjectName("scroll_and_button")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scroll_and_button)
        self.gridLayout_3.setContentsMargins(0, 0, 5, 5)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.upload_page_button = QtWidgets.QPushButton(self.scroll_and_button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_page_button.sizePolicy().hasHeightForWidth())
        self.upload_page_button.setSizePolicy(sizePolicy)
        self.upload_page_button.setMinimumSize(QtCore.QSize(40, 40))
        self.upload_page_button.setMaximumSize(QtCore.QSize(40, 40))
        self.upload_page_button.setAccessibleDescription("")
        self.upload_page_button.setStyleSheet("QPushButton {\n"
"color: #0FA15F;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"width: 45px;\n"
"height: 45px;\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.977273, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255))\n"
"}")
        self.upload_page_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/folder-7-48 (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_page_button.setIcon(icon6)
        self.upload_page_button.setIconSize(QtCore.QSize(16, 16))
        self.upload_page_button.setCheckable(True)
        self.upload_page_button.setAutoExclusive(False)
        self.upload_page_button.setObjectName("upload_page_button")
        self.gridLayout_3.addWidget(self.upload_page_button, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 2, 0, 1, 1)
        self.scrollArea_3 = CustomScrollArea(self.scroll_and_button)
        self.scrollArea_3.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea_3.setStyleSheet("QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"            background:white;\n"
"            width:10px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 0px solid red;\n"
"            border-radius: 4px;\n"
"            background-color: rgb(15, 161, 95);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"")
        self.scrollArea_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 894, 512))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_3.addWidget(self.scrollArea_3, 0, 0, 2, 2)
        self.gridLayout_4.addWidget(self.scroll_and_button, 0, 0, 1, 1)
        self.pages.addWidget(self.Upload_page)
        self.download_page = QtWidgets.QWidget()
        self.download_page.setObjectName("download_page")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.download_page)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scroll_and_button_2 = QtWidgets.QFrame(self.download_page)
        self.scroll_and_button_2.setMinimumSize(QtCore.QSize(911, 559))
        self.scroll_and_button_2.setObjectName("scroll_and_button_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scroll_and_button_2)
        self.gridLayout_8.setContentsMargins(0, 0, 5, 5)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollArea_4 = CustomScrollArea(self.scroll_and_button_2)
        self.scrollArea_4.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea_4.setStyleSheet("QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"            background:white;\n"
"            width:10px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"              border: 0px solid red;\n"
"            border-radius: 4px;\n"
"            background-color: rgb(15, 161, 95);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            \n"#subcontrol-position: bottom;subcontrol-origin: margin;
"            \n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0px;\n"
"            \n"#subcontrol-position: top;subcontrol-origin: margin;
"            \n"
"        }\n"
"")
        self.scrollArea_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 88, 28))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_8.addWidget(self.scrollArea_4, 0, 0, 2, 2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem9, 2, 0, 1, 1)
        self.download_page_button = QtWidgets.QPushButton(self.scroll_and_button_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_page_button.sizePolicy().hasHeightForWidth())
        self.download_page_button.setSizePolicy(sizePolicy)
        self.download_page_button.setMinimumSize(QtCore.QSize(40, 40))
        self.download_page_button.setMaximumSize(QtCore.QSize(40, 40))
        self.download_page_button.setStyleSheet("QPushButton {\n"
"color: #0FA15F;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"width: 45px;\n"
"height: 45px;\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.977273, y2:0, stop:0 rgba(10, 161, 93, 255), stop:1 rgba(0, 44, 65, 255))\n"
"}")
        self.download_page_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/data-transfer-download-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_page_button.setIcon(icon7)
        self.download_page_button.setIconSize(QtCore.QSize(16, 16))
        self.download_page_button.setCheckable(True)
        self.download_page_button.setAutoExclusive(True)
        self.download_page_button.setObjectName("download_page_button")
        self.gridLayout_8.addWidget(self.download_page_button, 2, 1, 1, 1)
        self.verticalLayout_11.addWidget(self.scroll_and_button_2)
        self.pages.addWidget(self.download_page)
        self.history_page = QtWidgets.QWidget()
        self.history_page.setObjectName("history_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.history_page)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem10 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.label_22 = QtWidgets.QLabel(self.history_page)
        self.label_22.setMinimumSize(QtCore.QSize(311, 92))
        self.label_22.setMaximumSize(QtCore.QSize(311, 92))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("QLabel {\n"
"font: 63 50pt \"Open Sans Semibold\";\n"
"    color:rgb(0, 44, 65);\n"
"}")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_19.addWidget(self.label_22)
        spacerItem11 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem11)
        self.gridLayout_7.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem12 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem12)
        self.label_23 = QtWidgets.QLabel(self.history_page)
        self.label_23.setMinimumSize(QtCore.QSize(311, 200))
        self.label_23.setMaximumSize(QtCore.QSize(311, 200))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_23.setFont(font)
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/icons/icons/work-in-progress (1).png"))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_20.addWidget(self.label_23)
        spacerItem13 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem13)
        self.gridLayout_7.addLayout(self.horizontalLayout_20, 1, 0, 1, 1)
        self.pages.addWidget(self.history_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.settings_page)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_5 = QtWidgets.QWidget(self.settings_page)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_25 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("QLabel {\n"
"font: 63 16pt \"Open Sans Semibold\";\n"
"    color:rgb(0, 44, 65);\n"
"}")
        self.label_25.setObjectName("label_25")
        self.gridLayout_14.addWidget(self.label_25, 0, 0, 1, 1)
        self.kb_slider_2 = QtWidgets.QSlider(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.kb_slider_2.setFont(font)
        self.kb_slider_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.kb_slider_2.setAutoFillBackground(False)
        self.kb_slider_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.kb_slider_2.setMinimum(50)
        self.kb_slider_2.setMaximum(50000)
        self.kb_slider_2.setSingleStep(250)
        self.kb_slider_2.setPageStep(250)
        self.kb_slider_2.setTracking(True)
        self.kb_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.kb_slider_2.setInvertedAppearance(False)
        self.kb_slider_2.setInvertedControls(False)
        self.kb_slider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.kb_slider_2.setTickInterval(10)
        self.kb_slider_2.setObjectName("kb_slider_2")
        self.gridLayout_14.addWidget(self.kb_slider_2, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem14, 1, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem15, 0, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem16, 1, 0, 1, 1)
        self.quit_button = QtWidgets.QPushButton(self.widget_5)
        self.quit_button.setMinimumSize(QtCore.QSize(40, 40))
        self.quit_button.setMaximumSize(QtCore.QSize(40, 40))
        self.quit_button.setStyleSheet("QPushButton {\n"
"color: #0FA15F;\n"
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
        self.quit_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/shutdown-icon-18-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/folder-7-48 (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.quit_button.setIcon(icon8)
        self.quit_button.setIconSize(QtCore.QSize(16, 16))
        self.quit_button.setCheckable(True)
        self.quit_button.setAutoExclusive(False)
        self.quit_button.setObjectName("quit_button")
        self.gridLayout_6.addWidget(self.quit_button, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget_5, 0, 0, 1, 1)
        self.pages.addWidget(self.settings_page)
        self.verticalLayout_5.addWidget(self.pages)
        self.gridLayout.addWidget(self.main_window, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionDownload = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(".\\../../../../../../.designer/backup/pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownload.setIcon(icon9)
        self.actionDownload.setObjectName("actionDownload")
        self.actionUpload = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(".\\../../../../../../.designer/backup/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpload.setIcon(icon10)
        self.actionUpload.setObjectName("actionUpload")
        self.actionStatus = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(".\\../../../../../../.designer/backup/icons8-status-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStatus.setIcon(icon11)
        self.actionStatus.setObjectName("actionStatus")
        self.actionno = QtWidgets.QAction(MainWindow)
        self.actionno.setObjectName("actionno")

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(1)
        self.menu_button.toggled['bool'].connect(self.icons_only.setHidden) # type: ignore
        self.menu_button.toggled['bool'].connect(self.full_menu.setVisible) # type: ignore
        self.upload_button_ico.toggled['bool'].connect(self.upload_button.setChecked) # type: ignore
        self.download_button_ico.toggled['bool'].connect(self.download_button.setChecked) # type: ignore
        self.history_button_ico.toggled['bool'].connect(self.history_button.setChecked) # type: ignore
        self.upload_button.toggled['bool'].connect(self.upload_button_ico.setChecked) # type: ignore
        self.download_button.toggled['bool'].connect(self.download_button_ico.setChecked) # type: ignore
        self.history_button.toggled['bool'].connect(self.history_button_ico.setChecked) # type: ignore
        self.settings_button.toggled['bool'].connect(self.settings_button_ico.setChecked) # type: ignore
        self.settings_button_ico.toggled['bool'].connect(self.settings_button.setChecked) # type: ignore
        self.quit_button.toggled['bool'].connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_label.setText(_translate("MainWindow", "Menu"))
        self.upload_button.setText(_translate("MainWindow", "Upload"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.history_button.setText(_translate("MainWindow", "History"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.search_tab.setPlaceholderText(_translate("MainWindow", "Search Here..."))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0fa15f;\">Welcome To Torrent</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans Semibold\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#002c41;\">Here you can download files from other people</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#002c41;\">And<br /><br />You can share you files with people in the app</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#002c41;\">Enjoy Your Time!<br /><br /><br /><br />Ohad Gips<br /></span></p></body></html>"))
        self.download_page_button.setAccessibleDescription(_translate("MainWindow", "download from available files"))
        self.label_22.setText(_translate("MainWindow", "In Work..."))
        self.label_25.setText(_translate("MainWindow", "Set limit for space usage:"))
        self.quit_button.setAccessibleDescription(_translate("MainWindow", "Quit"))
        self.actionDownload.setText(_translate("MainWindow", "Download"))
        self.actionUpload.setText(_translate("MainWindow", "Upload"))
        self.actionStatus.setText(_translate("MainWindow", "Status"))
        self.actionno.setText(_translate("MainWindow", "no"))
from customscrollarea import CustomScrollArea
import icons_rc
