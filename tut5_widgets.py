import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwars):
        super(MainWindow, self).__init__(*args, **kwars)

        self.setWindowTitle('Mon bébé Marion')

        widget = QLabel('aa')
        font = widget.font()
        font.setPointSize(60)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

# starts event loop
app.exec_()
