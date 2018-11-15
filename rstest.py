import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

wiki = "http://oldschoolrunescape.wikia.com/wiki/Category:Shops?from=*"

wikiText = requests.get(wiki)
soup = BeautifulSoup(wikiText.text, features="lxml")

links = [a.get('href') for a in soup.find_all('a', href=True)]
urlBegin = "http://oldschoolrunescape.wikia.com/wiki/Aaron%27s_Archery_Appendages"
urlEnd = "http://oldschoolrunescape.wikia.com/wiki/Perry%27s_Chop-chop_Shop"
listIndexes = [0,0,0,0]
allLinks = []
for link in links:
    url = "http://oldschoolrunescape.wikia.com%s" % link
    url = url.strip()
    if url == urlBegin:
        listIndexes[0]=links.index(link)

    if url == urlEnd:
        listIndexes[1] = links.index(link)
print(listIndexes)


links = links[listIndexes[0]:listIndexes[1]]
print(links)
for link in links:
    url = "http://oldschoolrunescape.wikia.com%s" % link


    # url = "http://oldschoolrunescape.wikia.com/wiki/Aaron%27s_Archery_Appendages"

    print(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    table = soup.find("table", {"class": "wikitable sortable"})
    if table:
        dft = pd.read_html(str(table), header=0,index_col=0, flavor = 'bs4')
        df = dft[0]
        if 'Item' in df:
            print(df)

url = "http://oldschoolrunescape.wikia.com/wiki/Bob%27s_Brilliant_Axes"
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
table = soup.find("table", {"class": "wikitable sortable"})
dfTemp2 = pd.read_html(str(table))
dfTemp = dfTemp2[0]
print(dfTemp)

# df_new = pd.concat([df, dfTemp])
# print(df_new)
