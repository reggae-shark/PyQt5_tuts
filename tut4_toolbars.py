import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwars):
        super(MainWindow, self).__init__(*args, **kwars)

        self.setWindowTitle('Mon bébé Marion')
        label = QLabel('22 ocotobre')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        # create object tool bar
        toolbar = QToolBar('My Tool Bar')
        self.addToolBar(toolbar)

        # create button (lenght of your sting)
        button_action = QAction('your button', self)
        # Message dispayed when hover
        button_action.setStatusTip('this  is yours')
        self.setStatusBar(QStatusBar(self))

        # Signal
        button_action.triggered.connect(self.onMyToolBarClick)

        # Making button toggle rather tyhen momentary
        button_action.setCheckable(True)

        # Adding button to tool bar
        toolbar.addAction(button_action)

    # Custom def. S will return Boolean
    def onMyToolBarClick(self, s):
        print('click', s)


app = QApplication(sys.argv)
window = MainWindow()

window.show()


# starts event loop
app.exec_()
