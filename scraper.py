import requests 
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


def get_citations_needed_count (URL): 
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  list_items = soup.find_all("a", attrs={"title": "Wikipedia:Citation needed"})
  print("citations needed: ", len(list_items))

def get_citations_needed_report(URL): 
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  list_items = soup.find_all("a", attrs={"title": "Wikipedia:Citation needed"})
  for item in list_items: 
    print(item.parent.parent.parent.text)
 
get_citations_needed_report(URL)


get_citations_needed_count(URL)

