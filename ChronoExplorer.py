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

        # Back button
        back_btn = QAction('⮜', self) # back button that takes you to the last state
        back_btn.triggered.connect(lambda: self.current_browser().back())
        toolbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('⮞', self) # creates a forward button and if pressed then goes to next state
        forward_btn.triggered.connect(lambda: self.current_browser().foward())
        toolbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('⟳', self) # Creates a reload button that resets the states
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        toolbar.addAction(reload_btn)

        # Home BUtton
        home_btn = QAction('⌂', self)
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)



















