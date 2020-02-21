import re
import requests
from bs4 import BeautifulSoup
import time #most sites will block multiple fast requests especially just to stop you from spamming their servers with scraping requests (it’s also just impolite to overload other people’s servers with requests)


def linkgenerator(string):
    new_string = string.replace(" ", "+")
    new_string2 = "https://www.ncbi.nlm.nih.gov/pubmed/?term={}".format(new_string)
    return new_string2

def pubmedscraper(pubmedlink):
    pagedata = requests.get(x)
    cleanpagedata = BeautifulSoup(pagedata.text, 'html.parser')
    pubmedIDsearch = re.compile(r'/pubmed/(\d+)')
    pubmedID = pubmedIDsearch.findall(str(cleanpagedata))
    pubmedArticleLinks = []
    for i in range(len(pubmedID)):
        pubmedArticleLinks.append("https://www.ncbi.nlm.nih.gov/pubmed/{}".format(pubmedID[i]))
    return pubmedArticleLinks
    #scrape individual pubmed article links now


print("Hi! I am Pubmed scrapper.")
g = input("What topic(s) would you like to scrape today? : ") # prostate cancer
x = linkgenerator(g) # generates https://www.ncbi.nlm.nih.gov/pubmed/?term=prostate+cancer
y = pubmedscraper(x) # generates list of links to most recent pubmed articles

results = []
for a in range(len(y)):
        pubmedArticleLinkData = requests.get(y[a])
        cleanpubmedArticleLinkData = BeautifulSoup(pubmedArticleLinkData.text, 'html.parser')
        abstract = cleanpubmedArticleLinkData.find(class_="rprt abstract").get_text()
        finalAbstract = abstract.split('[Indexed for MEDLINE]').pop(0)
        results.append(finalAbstract)
        #time.sleep(30)
print(results)

with open('pubmed.txt', 'w') as output:
    output.write(str(results))


