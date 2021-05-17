#Sources used
#video tutorial here: https://www.youtube.com/watch?v=Vde5SH8e1OQ&ab_channel=TechWithTim
#https://www.youtube.com/watch?v=OGVuD0-5INY&t=116s&ab_channel=computingmrh
#https://pythonspot.com/pyqt5-buttons/
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

class Ui_MainWindow(object):
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 563)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(260, 200, 354, 34))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.enterButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.enterButton.setFont(font)
        self.enterButton.setObjectName("enterButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.enterButton)
        self.stockSearch = QtWidgets.QLabel(self.centralwidget)
        self.stockSearch.setGeometry(QtCore.QRect(290, 130, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Trajan Pro")
        font.setPointSize(25)
        self.stockSearch.setFont(font)
        self.stockSearch.setObjectName("stockSearch")
        self.bottomImage = QtWidgets.QLabel(self.centralwidget)
        self.bottomImage.setGeometry(QtCore.QRect(0, -50, 891, 591))
        self.bottomImage.setText("")
        self.bottomImage.setPixmap(QtGui.QPixmap("../bottomImage.png"))
        self.bottomImage.setScaledContents(True)
        self.bottomImage.setWordWrap(True)
        self.bottomImage.setObjectName("bottomImage")
        self.underText = QtWidgets.QLabel(self.centralwidget)
        self.underText.setGeometry(QtCore.QRect(150, 50, 561, 281))
        self.underText.setText("")
        self.underText.setPixmap(QtGui.QPixmap("../undertone.jpg"))
        self.underText.setScaledContents(True)
        self.underText.setObjectName("underText")
        self.bottomImage.raise_()
        self.underText.raise_()
        self.formLayoutWidget.raise_()
        self.formLayoutWidget.raise_()
        self.formLayoutWidget.raise_()
        self.stockSearch.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.enterButton.clicked.connect(self.clickme)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Stock Here"))
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        self.stockSearch.setText(_translate("MainWindow", "Stock Search"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

    def clickme(self): 
        stock_name = self.lineEdit.text()
        self.driver.get("https://www.tradingview.com/")
		#Element name for the search bar
        search = self.driver.find_element_by_name("query")

		# #This will send the keys of the stock you want to look up to the search bar.
        search.send_keys(stock_name)

		# #This will press enter.
        search.send_keys(Keys.RETURN)

		# #Captures a screenshot of the stock
        self.driver.save_screenshot(r"C:\Users\Gage Machado\Desktop\po1-gwm32\Screenshot\stocks.png")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())