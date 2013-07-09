__author__ = 'arash'

from linkgetter import getLinks
import sys
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from crawler import *

if __name__ == '__main__' :
    urlList = [getLinks()[0:10]]
    app = QApplication(sys.argv)
    downloader = Downloader(urlList)
    downloader.done.connect(app.quit)
    web = QWebView()
    web.setDisabled(True)
    web.setPage(downloader.page)
    # web.show()
    sys.exit(app.exec_())
