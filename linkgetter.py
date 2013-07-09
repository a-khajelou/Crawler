__author__ = 'arash'

from HTMLParser import HTMLParser
from firstpagegetter import getHtml

links = []
data = getHtml("http://www.results24.co.uk")

class LinkParser (HTMLParser) :
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'href' :
                if attr[1].find ('/football/') != -1 :
                    links.append(("http://www.results24.co.uk"+attr[1],))

def getLinks () :
    lp = LinkParser ()
    lp.feed(data)
    return links