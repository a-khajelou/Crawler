import gtk
import webkit
import warnings

warnings.filterwarnings('ignore')

class WebView(webkit.WebView):
    def get_html(self):
        self.execute_script('oldtitle=document.title;document.title=document.documentElement.innerHTML;')
        html = self.get_main_frame().get_title()
        self.execute_script('document.title=oldtitle;')
        return html

class Crawler(gtk.Window):
    def __init__(self, url):
        self._htmlContent = ""
        gtk.Window.__init__(self)
        self._url = url
        self._file = file

    def crawl(self):
        view = WebView()
        view.open(self._url)
        view.connect('load-finished', self._finished_loading)
        self.add(view)
        gtk.main()

    def _finished_loading(self, view, frame):
        self._htmlContent = view.get_html()
        gtk.main_quit()
    def getHtmlContent (self) :
        return self._htmlContent

def getHtml (url) :
    crawler = Crawler(url)
    crawler.crawl()
    return crawler.getHtmlContent()