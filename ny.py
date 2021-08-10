import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def get_headlines():
    response=requests.get("https://www.cbc.ca/news/world")

    soup = BeautifulSoup(response.content, "html.parser")
    s=soup.get_text()
    k = soup.find_all("a", {"class": "card"})
   
    headdict = {}


    i=0
    while i < len(k):
        link='https://www.cbc.ca' + k[i].get('href')
        english=k[i].find('h3').get_text()
        to_translate = k[i].find('h3').get_text()
        chinese = GoogleTranslator(source='auto', target='zh-cn').translate(to_translate)
        
        #print(chH)

        headdict[i] = [english,chinese,link]
        print(headdict[i])
        i=i+1
    
    return headdict
    
def translateArt():
    print(link)
    #driver.get(link)
    soup2 = BeautifulSoup(driver.page_source, "html.parser")
    e = soup2.find("h2", {"class": "deck"})
    print(e.get_text())

    d = soup2.find_all("p")

    while i < 13:
        print(d[i].get_text())
        i = i+1
        to_translate = d[i].get_text()
        translated = GoogleTranslator(source='auto', target='zh-cn').translate(to_translate)
        print("Headline " + str(i) + ": " + translated)

def getheadlines():


    response=requests.get("https://www.cbc.ca/news/world")

    soup = BeautifulSoup(response.content, "html.parser")
    s=soup.get_text()
    #print(s)

    k = soup.find_all("h3", {"class": "headline"})
   
    links = soup.find_all("a", {"id": "headline"})

    headline=0
    i=0
    h=0

    headlines = {}
    engchHeadlines=[]
    while headline < len(k):  
        
        engH="Headline " + str(headline) + ": " + k[headline].get_text()
        to_translate = k[headline].get_text()
        translated = GoogleTranslator(source='auto', target='zh-cn').translate(to_translate)
        chH="Headline " + str(headline) + ": " + translated
        headline = headline+1

        headlines[headline]= [engH, chH]
    
        #print(headlines)
    return headlines


if __name__ == '__main__':

    get_headlines()