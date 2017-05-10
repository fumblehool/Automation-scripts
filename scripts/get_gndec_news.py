import requests
from bs4 import BeautifulSoup


url = "http://gndec.ac.in"

req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')

news = soup.select("#block-block-15")[0].select(".content")[0].find_all("p")

for i in news:
    print i.text
