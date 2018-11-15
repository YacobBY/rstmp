import pandas as pd
from bs4 import BeautifulSoup
import requests

wiki = "http://oldschoolrunescape.wikia.com/wiki/Category:Shops?from=*"

wikiText = requests.get(wiki)
soup = BeautifulSoup(wikiText.text, features="lxml")

links = [a.get('href') for a in soup.find_all('a', href=True)]
for link in links:

    print(link)




# get a table
url = "http://oldschoolrunescape.wikia.com/wiki/Davon%27s_Amulet_Store"
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
table = soup.find("table", {"class": "wikitable sortable"})
dft = pd.read_html(str(table))
print(links)
df = dft[0]
print(df)

print("aAaaaa")

url = "http://oldschoolrunescape.wikia.com/wiki/Bob%27s_Brilliant_Axes"
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
table = soup.find("table", {"class": "wikitable sortable"})
dfTemp2 = pd.read_html(str(table))
dfTemp = dfTemp2[0]
print(dfTemp)

df_new = pd.concat([df, dfTemp])
print(df_new)
