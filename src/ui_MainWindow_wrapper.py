from ui_MainWindow import Ui_MainWindow

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import time
import subprocess


class Ui_MainWindow_wrapper(Ui_MainWindow):
	def __init__(self, window):
		super(Ui_MainWindow_wrapper, self).__init__()
		self.parent = window

		self.path = "~/Downloads"
		self.urls = []

		#argument to insertPlainText() method
		self.logText = ""

		self.setupUi(window)
		self.setupSignals()

		self.__updateUi()

	def setupSignals(self):
		self.actionQuit.triggered.connect(self.quit)
		self.actionDownload.triggered.connect(self.handleDownloadButton)
		self.actionClean.triggered.connect(self.handleCleanButton)

		self.destinationButton.clicked.connect(self.handleDestinationButton)
		self.downloadButton.clicked.connect(self.handleDownloadButton)
		self.cleanButton.clicked.connect(self.handleCleanButton)
		self.urlButton.clicked.connect(self.handleUrlButton)
		self.urlLineEdit.returnPressed.connect(self.handleUrlButton)

	def quit(self):
		sys.exit()


	def handleUrlButton(self):
		url = self.urlLineEdit.text()

		if not url == "":
			self.urls.append(url)

			self.logText = "Added URL: " + url + "\n"
			self.urlLineEdit.setText("")

			self.__updateUi()
		

	def handleDestinationButton(self):
		path = QFileDialog.getExistingDirectory(self.parent, "Select a destination folder")

		self.path = path

		self.logText = "Destination folder: " + self.path + "\n"
		self.__updateUi()

	def handleDownloadButton(self):
		for link in self.urls:
			print(link)

			#check if list is playlist or just one video
			if 'playlist' in link:
				print("downloading playlist")

				cmd = "cd " + self.path + " && yt-dlp --extract-audio --audio-format mp3 " + link
				print(cmd)

				try:
					log = subprocess.check_output(cmd, shell=True)
					self.logText = log.decode('utf-8')
					self.__updateUi()

				except Exception as e:
					self.logText = "FAILED!!!\n" + str(e)

			else:
				print("downloading a song")

				cmd = ["cd", self.path, "&&", "yt-dlp", "--extract-audio", "--audio-format", "mp3", "--no-playlist", link]
				print(cmd)

				p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				data,stderr  = p.communicate()
				print(data, stderr)

				"""
				cmd = "cd " + self.path + " && yt-dlp --extract-audio --audio-format mp3 --no-playlist " + link
				print(cmd)

				try:
					log = subprocess.check_output(cmd, shell=True)
					self.logText = log.decode('utf-8')
					self.__updateUi()

				except Exception as e:
					self.logText = "FAILED!!!\n" + str(e)
				"""

		self.urls = []
		self.logText = "Finished\n"
		self.__updateUi()

	def handleCleanButton(self):
		self.log.setPlainText("----	Cleaned up		----\n")
		self.urls = []

	def __updateUi(self):
		self.destinationLabel.setText(self.path)
		self.log.insertPlainText(self.logText)
