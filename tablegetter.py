__author__ = 'arash'

from HTMLParser import HTMLParser
import json

class TableParser (HTMLParser) :
    def __init__(self , parent = None):
        HTMLParser.__init__(self)
        self.res = []
    def handle_starttag(self, tag, attrs):
        if (len(self.res) == 0) :
            self.res.append({'tag':tag , 'attrs':[attrs,] , 'data':None})
        if (len(self.res) > 0 ) :
            if self.res[len(self.res)-1]['data'] != None :
                self.res.append({'tag':tag , 'attrs':attrs , 'data':None})
            else :
                self.res[len(self.res)-1]['attrs'] = self.res[len(self.res)-1]['attrs']+attrs

    def handle_data(self, data):
        if (len(self.res) > 0) :
            if self.res[len(self.res)-1]['data'] == None :
                self.res[len(self.res)-1]['data'] = data
            else :
                self.res[len(self.res)-1]['data'] = self.res[len(self.res)-1]['data']+data
    def getRes (self) :
        return self.res

def getJSonData (html) :
    t = TableParser ()
    t.feed(html)

    dataTable = []

    for i in t.getRes() :
        if i['tag'] == 'div' :
             for j in i['attrs'] :
                if j[1] == 'box-over-content-a' :
                    dataTable.append({'header' : i['data']})

    for i in t.getRes() :
        if i['tag'] == 'td' :
            if len(i['attrs']) > 0 :
                for j in i['attrs'] :
                    if j[1] == 'time' :
                        dataTable.append({'time':str(i['data']).strip() ,
                                          'timer':None ,
                                          'home':None ,
                                          'away':None ,
                                          'score':None ,
                                          'guess':[] ,
                                          })
                    elif len(dataTable) > 0 :
                        if j[1] == 'timer' :
                            if dataTable[len(dataTable)-1]['timer'] == None :
                                dataTable[len(dataTable)-1]['timer'] = str(i['data']).strip()
                        if str(j[1]).find("team-home") != -1 :
                            if dataTable[len(dataTable)-1]['home'] == None :
                                dataTable[len(dataTable)-1]['home'] = str(i['data']).strip()
                        if str(j[1]).find("team-away") != -1 :
                            if dataTable[len(dataTable)-1]['away'] == None :
                                dataTable[len(dataTable)-1]['away'] = str(i['data']).strip()
                        if str(j[1]).find("score") != -1 :
                            if dataTable[len(dataTable)-1]['score'] == None :
                                dataTable[len(dataTable)-1]['score'] = str(i['data']).strip()
                        if j[0] == 'alt' :
                            dataTable[len(dataTable)-1]['guess'].append(str(j[1]).strip()[:str(j[1]).find('[')])

    jsonData = json.dumps(dataTable)
    return jsonData