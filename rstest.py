import pandas as pd
# match = 'item'
# url = 'http://oldschoolrunescape.wikia.com/wiki/Brian%27s_Archery_Supplies'
#
# dfs =  pd.read_html(url, match=match)
#
# print(dfs)

from bs4 import BeautifulSoup
import urllib3.request
import requests

wiki = "http://oldschoolrunescape.wikia.com/wiki/Davon%27s_Amulet_Store"
# header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia`enter code here`
# req = urllib3.request(wiki, headers=header)
# page = urllib3.urlopen(wiki)
url = "http://oldschoolrunescape.wikia.com/wiki/Davon%27s_Amulet_Store"
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")


table = soup.find("table", {"class": "wikitable sortable"})
df = pd.read_html(str(table))
print(df)

