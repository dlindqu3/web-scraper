import requests 
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# anchors= soup.find_all("a")
# print(results)

# print(anchors)

def get_citations_needed_count (URL): 
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  list_items = soup.find_all("a", attrs={"title": "Wikipedia:Citation needed"})
  print("list_items length: ", len(list_items))
  for link in list_items:  
    return link
   
print(get_citations_needed_count(URL))

