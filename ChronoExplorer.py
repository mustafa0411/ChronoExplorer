import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Window Properties
        self.setWindowTitle('ChronoExplorer') # Silly ahh name
        self.setWindowIcon(QIcon('icon.png')) # Will replace with something soon

        # Explorer tab widgets
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True) # close tabs when clicked
        self.tabs.tabCloseRequested(self.close_tab)
        self.setCentalWidget(self.tabs)

        # Browser toolbar, think 3 lines at top right
        toolbar = QToolBar()
        self.addToolBar(toolbar)










