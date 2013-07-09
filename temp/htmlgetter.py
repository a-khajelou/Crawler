__author__ = 'arash'

import gtk
import webkit
import warnings

warnings.filterwarnings('ignore')

class WebView(webkit.WebView):
    def getHtml(self):
        self.execute_script('oldtitle=document.title;document.title=document.documentElement.innerHTML;')
        html = self.get_main_frame().get_title()
        self.execute_script('document.title=oldtitle;')
        return html

class Crawler(gtk.Window):
    def __init__(self, url):
        gtk.Window.__init__(self)
        self._url = url
        self.htmlContent = ""

    def crawl(self):
        view = WebView()
        view.open(self._url)
        # view.connect('load-finished', self._finishedLoading)
        view.connect('load-committed', self._finishedLoading)
        self.add(view)
        gtk.main()

    def getWholeHtml (self) :
        return self.htmlContent

    def _finishedLoading(self, view, frame):
        self.htmlContent = view.getHtml()
        gtk.main_quit()

def getHtml (url) :
    crawler = Crawler(url)
    crawler.crawl()
    return crawler.getWholeHtml()