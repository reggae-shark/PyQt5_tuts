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


class CustomButton(Qbutton):

    def keyPressEvent(self, e):
        # custom event handling
        super(CustomButton, self).keyPressEvent(e)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

# starts event loop
app.exec_()
