from ui_MainWindow_wrapper import Ui_MainWindow_wrapper
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
import signal


class UiApp(QApplication):
	def __init__(self, parent=None):
		super(UiApp, self).__init__(sys.argv)

		self.window = QMainWindow()

		self._ui = Ui_MainWindow_wrapper(self.window)

		self.window.show()

		self.exec()

if __name__ == "__main__":
	try:
		signal.signal(signal.SIGINT, signal.SIG_DFL)

		app = UiApp();

	except KeyboardInterrupt:
		print("SIGINT")

	except Exception as e:
		print(str(e))
