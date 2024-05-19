import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)  # Increase the size of the window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Increase the size and position of the labels
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(50, 50, 331, 251))
        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setText("")
        self.label_1.setScaledContents(True)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 50, 331, 251))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # Increase the size and position of the buttons
        self.Button_start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start.setGeometry(QtCore.QRect(150, 350, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_start.setFont(font)
        self.Button_start.setObjectName("Button_start")

        self.Button_new = QtWidgets.QPushButton(self.centralwidget)
        self.Button_new.setGeometry(QtCore.QRect(450, 350, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_new.setFont(font)
        self.Button_new.setObjectName("Button_new")
        self.Button_new.clicked.connect(self.back)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_start.setText(_translate("MainWindow", "Chạy"))
        self.Button_new.setText(_translate("MainWindow", "Quay Lại"))

    def back(self):
        subprocess.Popen(['python', 'index.py'])
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
