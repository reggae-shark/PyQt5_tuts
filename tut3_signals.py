import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Signal = signals allow you to ‘listen’ for notifications of specific occurrences within your application
# Slots =  Data can also be sent alongside a signal - so as well as being notified of the updated text you can also receive it.

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwars):
        super(MainWindow, self).__init__(*args, **kwars)

        #  SIGNAL: The connected function will be called whenever the window
        #  title is changed. The new title will be passed to the function.
        # self.windowTitleChanged.connect(self.onWindowTitleChange)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is discarded in the lambda and the
        # function is called without parameters
        # self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter. Extra data is passed from
        # within the lambda.
        # self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        # This sets the window title which will trigger all the above signals
        # sending the new title to the attached functions or lambdas as the
        # first parameter.
        self.setWindowTitle("window Title")

        label = QLabel('Marion')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    # SLOT: This accepts a string, e.g. the window title, and prints it
    def onWindowTitleChange(self, s):
        print(s)

    # SLOT: This has default parameters and can be called without a value

    def my_custom_fn(self, a="HELLLO!", b=5):

        print(a, b)


app = QApplication(sys.argv)
window = MainWindow()

window.show()


# starts event loop
app.exec_()
