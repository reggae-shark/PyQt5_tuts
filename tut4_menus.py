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
        toolbar.setIconSize(QSize(16, 16))
        # ----------

        button_action = QAction(QIcon('terminal.gif'),
                                'Terminal Launcher', self)
        button_action.setStatusTip('Terminal')
        button_action.triggered.connect(self.onMyToolBarClick())
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        # ---------- Raccorci clavier
        # sur mac ctrl = cmd
        button_action.setShortcut(QKeySequence("Ctrl+,"))
        # ----------

        # ----------

        toolbar.addSeparator()
        # ----------
        button_action2 = QAction(QIcon("bug.png"),
                                 "Bug Seaker", self)
        button_action2.setStatusTip("BUG")
        button_action2.triggered.connect(self.onMyToolBarClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        # --------------MENU----------------

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

        #  ______SUBMENU___________

        sub_menu = file_menu.addMenu("Submenu")
        sub_menu.addAction(button_action)
        sub_menu.addAction(button_action2)

    # Custom def. S will return Boolean

    def onMyToolBarClick(self, s):
        print('click', s)


app = QApplication(sys.argv)
window = MainWindow()


window.show()


# starts event loop
app.exec_()
