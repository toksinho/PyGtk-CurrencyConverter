import xml.etree.ElementTree as ET
from urlData import tecaj
class Xml:
        def neka(self):
                print self.y
        def __init__(self):
                tecaj()
                tree = ET.parse('downloaded_file.xml')
                root=tree.getroot()
                self.date ='Date: ' +  root[0][2].text
                self.kuna=1
                for x in root.iter('Currency'):
                        self.value = x.find('MeanRate').text
                        self.value=self.value.replace(",",".")
                        name = x.find('Name').text
                        print(name, self.value)
                        if name=='USD':
                                self.dollar=float(self.value)
                                
                        if name=='EUR':
                                self.euro=float(self.value)
                                
                        if name=='CHF':
                                self.chf=float(self.value)
                                x=str(self.chf)
                                
        def EurUsa(self):
                return self.euro/self.dollar

        def EurSui(self):
                return self.euro/self.chf

        def EurHr(self):
                return self.euro/self.kuna
        

        def UsaHr(self):
                return self.dollar/self.kuna

        def UsaSui(self):
                return self.dollar/self.chf

        def SuiHr(self):
                return self.chf/self.kuna


