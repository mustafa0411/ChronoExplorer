import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon


class ChronoBrowser(QMainWindow):

    # Project Compiles and functions correctly.
    # No errors that I know of
    # \[T]/ Solaire Approved
    def __init__(self):
        super(ChronoBrowser, self).__init__()

        # These are the UI funcitonalities and what happens when they are interacted with

        self.setWindowTitle('ChronoExplorer')  # Silly ahh name
        self.setWindowIcon(QIcon('Compass_icon.png'))

        # Explorer tab widgets
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)  # close tabs when clicked
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        # Browser toolbar, think 3 lines at top right
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # These are all the buttons that are common in most browsers

        # Back button
        back_btn = QAction('⮜', self)  # back button that takes you to the last state
        back_btn.triggered.connect(lambda: self.current_browser().back())
        toolbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('⮞', self)  # creates a forward button and if pressed then goes to next state
        forward_btn.triggered.connect(lambda: self.current_browser().forward())
        toolbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('⟳', self)  # Creates a reload button that resets the states
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        toolbar.addAction(reload_btn)

        # Home Button
        home_btn = QAction('⌂', self)  # Sends you to a specific page that basically starts you over
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)

        # Add tab button
        add_tab_btn = QAction('+', self)  # Create a new tab with the same funcitons
        add_tab_btn.triggered.connect(self.add_tab)
        toolbar.addAction(add_tab_btn)

        self.add_tab()  # First tab for the browser

        # URL search bar code
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)  # URL bar to search for websites
        toolbar.addWidget(self.url_bar)
        # Connect signals after adding the initial tab
        self.current_browser().urlChanged.connect(self.update_url)

    # Methods for the implementation of the browser functionality
    def add_tab(self):
        browser = QWebEngineView()
        browser.setUrl(QUrl('https://google.com'))  # Main URL, for homepage as well
        self.tabs.addTab(browser, 'New Tab')  # Creates a new tab using the keyword
        self.tabs.setCurrentWidget(browser)
        self.tabs.setTabText(self.tabs.currentIndex(), 'Loading...')
        browser.titleChanged.connect(  # Tab Title changes that gets set depending on the website or title of the page
            lambda title, new_browser=browser: self.tabs.setTabText(self.tabs.indexOf(browser), title))
        browser.urlChanged.connect(
            lambda url, new_browser=browser: self.update_url(url) if self.tabs.currentWidget() == browser else None)

    def close_tab(self, index):
        # Gets the browser widget at the specific index
        browser_widget = self.tabs.widget(index)

        # Condition for playing video, pause function. could add other video streaming platforms as well
        if browser_widget.url().host() == 'www.youtube.com':  # Uses javascript to pause the video on youtube
            browser_widget.page().runJavaScript(
                "document.getElementsByTagName('video')[0].pause();")  # Ok this is lowkey poggers

        # closing tab functionality for last tabs
        if self.tabs.count() < 2:  # Close the whole window if the close tab button is pressed for the last tab
            self.close()
        else:
            # Removes the tab and deletes its browser widgets as well.
            self.tabs.removeTab(index)
            browser_widget.deleteLater()

    def navigate_home(self):  # navigates home to a specified url
        self.current_browser().setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):  # method for URL search bar functionality
        url = self.url_bar.text()
        if 'http' not in url:
            url = 'https://' + url  # adds https:// to make sure the user is sent to the correct site
        self.current_browser().setUrl(QUrl(url))

    # Update URL method that changes the url bar based on what the user searches
    def update_url(self, q):
        if self.sender() == self.current_browser():
            self.url_bar.setText(q.toString())
            self.url_bar.setCursorPosition(0)

    def current_browser(self):
        return self.tabs.currentWidget()


# Main method for running the browser window
if __name__ == '__main__':
    app = QApplication(sys.argv)

    browser_window = ChronoBrowser()
    browser_window.showMaximized()

    sys.exit(app.exec_())
