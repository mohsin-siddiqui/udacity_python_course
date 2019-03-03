

from urllib.request import urlopen
from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urlopen(wiki)
#soup = BeautifulSoup(page, "html.parser").encode('UTF-8')

print(page)
