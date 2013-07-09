from PySide.QtCore import *
from PySide.QtWebKit import *
import time

from tablegetter import getJSonData


class Downloader(QObject):
    # To be emitted when every items are downloaded
    done = Signal()

    def __init__(self, urlList , parent = None):
        super(Downloader, self).__init__(parent)
        self.urlList = urlList
        self.counter = 0
        # As you probably don't need to display the page
        # you can use QWebPage instead of QWebView
        self.page = QWebPage(self)
        self.page.loadFinished.connect(self.save)
        self.startNext()
        self.jasonDataList = []
        self.responseCounter = 0


    def currentUrl(self):
        return self.urlList[self.counter][0]

    def startNext(self):
        print "Downloading %s..."%self.currentUrl()
        self.page.mainFrame().load(self.currentUrl())

    def save(self, ok):
        if ok:
            data = self.page.mainFrame().toHtml()
            self.jasonDataList.append(getJSonData(data.encode('utf8')))
            print "Saving ...."
            time.sleep(5)
        else:
            print "Error while downloading %s\nSkipping."%self.currentUrl()
            time.sleep(5)
        self.counter += 1
        if self.counter < len(self.urlList):
            self.startNext()
        else:
            for i in self.jasonDataList :
                print i
            self.done.emit()
    def getData (self) :
        if len(self.jasonDataList) > self.responseCounter :
            self.responseCounter+=1
            return self.jasonDataList[self.responseCounter-1]
        else :
            return None
    def getAllData (self) :
        return self.jasonDataList