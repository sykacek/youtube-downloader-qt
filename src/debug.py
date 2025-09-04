from ui_MainWindow_wrapper import Ui_MainWindow_wrapper
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

app = QApplication([])
window = QMainWindow()

_ui = Ui_MainWindow_wrapper(window)
