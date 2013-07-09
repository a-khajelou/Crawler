__author__ = 'arash'

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

class Render(QWebPage):
    def __init__(self, urls):
        self.urls = urls
        self.currentUrl = ""
        self.counter = 0
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.currentUrl = self.urls.pop()
        self.counter += 1
        self.mainFrame().load(QUrl(self.currentUrl))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        file = open ("htmlFiles/%d.html"%self.counter,'w')
        file.writelines(self.frame.toHtml().__str__())
        file.close()
        if self.urls :
            self.currentUrl = self.urls.pop()
            self.counter += 1
            self.mainFrame().load(QUrl(self.currentUrl))
        else :
            self.app.quit()